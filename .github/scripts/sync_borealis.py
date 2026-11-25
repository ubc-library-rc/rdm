#!/usr/bin/env python3
"""Copy the latest published guide PDFs from Borealis into this repo.

Reads _data/borealis_guides.yml. For each guide it asks the Dataverse API for
the dataset's latest published version, finds the PDF in it (whatever its
current file ID is), and saves it to the guide's fixed path if it changed.
It also records version details in _data/borealis_versions.json so pages can
show which version is embedded.

Environment:
  BOREALIS_API_TOKEN  optional; only needed for restricted files or drafts
  BOREALIS_SERVER     optional; overrides `server` in the config (for testing)
"""

import fnmatch
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "_data" / "borealis_guides.yml"
STATE = ROOT / "_data" / "borealis_versions.json"
TOKEN = os.environ.get("BOREALIS_API_TOKEN") or None
HASHES = {"MD5": "md5", "SHA-1": "sha1", "SHA-256": "sha256", "SHA-512": "sha512"}


class _SameHostTokenRedirect(urllib.request.HTTPRedirectHandler):
    """Follow redirects (Borealis may hand off to storage) without leaking the API token."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None and urllib.parse.urlsplit(newurl).netloc != urllib.parse.urlsplit(req.full_url).netloc:
            new.remove_header("X-dataverse-key")
        return new


_opener = urllib.request.build_opener(_SameHostTokenRedirect)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ubc-rdm-guide-sync"})
    if TOKEN:
        req.add_header("X-Dataverse-key", TOKEN)
    with _opener.open(req, timeout=120) as resp:
        return resp.read()


def file_hash(data, algo):
    return hashlib.new(algo, data).hexdigest()


def citation_field(version, name):
    fields = version.get("metadataBlocks", {}).get("citation", {}).get("fields", [])
    return next((f["value"] for f in fields if f.get("typeName") == name), None)


def citation_title(version):
    return citation_field(version, "title")


def apa_name(name):
    """'Barsky, Eugene' -> 'Barsky, E.'; 'Hu, Mary-Jane' -> 'Hu, M.-J.'; organizations stay as written."""
    if "," not in name:
        return name.strip()
    last, given = (part.strip() for part in name.split(",", 1))
    initials = " ".join(
        "-".join(piece[0] + "." for piece in word.split("-") if piece)
        for word in given.replace(".", " ").split()
    )
    return f"{last}, {initials}" if initials else last


def apa_authors(version):
    authors = [apa_name(a.get("authorName", {}).get("value", "")) for a in citation_field(version, "author") or []]
    authors = [a for a in authors if a]
    if len(authors) > 20:  # APA 7: first 19, an ellipsis, then the last author
        return ", ".join(authors[:19]) + ", . . . " + authors[-1]
    if len(authors) > 1:
        return ", ".join(authors[:-1]) + ", & " + authors[-1]
    return authors[0] if authors else None


def citation_version(server, query):
    """The version exactly as Borealis's own citation shows it, e.g. 'V1' -> '1'."""
    try:
        text = json.loads(fetch(f"{server}/api/datasets/:persistentId/versions/:latest-published/citation?{query}"))["data"]["message"]
    except Exception:
        return None
    found = re.findall(r"\bV(\d+(?:\.\d+)?)\b", re.sub(r"<[^>]+>", "", text))
    return found[-1] if found else None


def publication_year(server, query, version):
    """Year the dataset was first published (as in Borealis's own citation); falls back to this version's year."""
    try:
        published = json.loads(fetch(f"{server}/api/datasets/:persistentId/?{query}"))["data"].get("publicationDate")
    except Exception:
        published = None
    return (published or version.get("releaseTime") or "")[:4] or None


def sync_guide(server, guide):
    gid, doi, rel_path = guide["id"], guide["doi"], guide["path"]
    pattern = guide.get("match", "*.pdf").lower()

    query = urllib.parse.urlencode({"persistentId": doi})
    version = json.loads(fetch(f"{server}/api/datasets/:persistentId/versions/:latest-published?{query}"))["data"]

    candidates = [
        f for f in version.get("files", [])
        if fnmatch.fnmatch(f["dataFile"]["filename"].lower(), pattern)
        and (TOKEN or not f.get("restricted"))
    ]
    if len(candidates) != 1:
        names = [
            f["dataFile"]["filename"] + (" (restricted)" if f.get("restricted") else "")
            for f in version.get("files", [])
        ]
        hint = (
            "Set `match` in the config to pick one." if len(candidates) > 1
            else "Check the file is a PDF and not restricted (or add a BOREALIS_API_TOKEN secret)."
        )
        raise RuntimeError(
            f"expected exactly one public file matching {pattern!r}, found {len(candidates)}; "
            f"files in latest published version: {names}. {hint}"
        )
    datafile = candidates[0]["dataFile"]
    checksum = datafile.get("checksum") or {}
    algo = HASHES.get(checksum.get("type"))

    target = ROOT / rel_path
    current = target.read_bytes() if target.exists() else None
    if current is not None and algo and file_hash(current, algo) == checksum["value"]:
        status = "unchanged"
    else:
        data = fetch(f"{server}/api/access/datafile/{datafile['id']}")
        if algo and file_hash(data, algo) != checksum["value"]:
            raise RuntimeError(f"downloaded {datafile['filename']} does not match its {checksum['type']} checksum")
        if not data.startswith(b"%PDF") and pattern.endswith(".pdf"):
            raise RuntimeError(f"downloaded {datafile['filename']} is not a PDF")
        if data == current:
            status = "unchanged"
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as tmp:
                tmp.write(data)
            os.replace(tmp.name, target)
            status = "updated"

    info = {
        "doi": doi,
        "title": citation_title(version),
        "apa_authors": apa_authors(version),
        "year": publication_year(server, query, version),
        "version": f"{version.get('versionNumber')}.{version.get('versionMinorNumber')}",
        "citation_version": citation_version(server, query),
        "release_date": (version.get("releaseTime") or "")[:10] or None,
        "filename": datafile["filename"],
        "file_id": datafile["id"],
        "filesize": datafile.get("filesize"),
        "checksum": checksum.get("value"),
        "path": rel_path,
    }
    return status, info


def main():
    config = yaml.safe_load(CONFIG.read_text())
    server = (os.environ.get("BOREALIS_SERVER") or config["server"]).rstrip("/")
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    configured = {g["id"] for g in config.get("guides", [])}
    new_state = {k: v for k, v in state.items() if k in configured}
    failures = 0

    for guide in config.get("guides", []):
        try:
            status, info = sync_guide(server, guide)
            new_state[guide["id"]] = info
            print(f"[{status}] {guide['id']}: {info['filename']} v{info['version']} -> {info['path']}")
        except Exception as exc:  # keep going so one bad guide doesn't block the rest
            failures += 1
            print(f"::error title=Borealis sync failed for {guide['id']}::{guide['doi']}: {exc}")

    if new_state != state:
        STATE.write_text(json.dumps(new_state, indent=2, sort_keys=True) + "\n")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
