---
nav_exclude: true
---

{% raw %}

# Borealis guides on the workshop site

*Eugene Barsky, UBC Library Research Commons. November 2026.*

These notes explain how the one-page guides get from Borealis onto the workshop pages, so that anyone can keep them running, fix them if something breaks, or reuse the setup on another site. I've tried to keep them short and practical. If anything is unclear or out of date, please let me know, or write to research.data@ubc.ca.

## How it works

The guides live in Borealis, each as its own dataset with its own DOI. Each workshop page shows its guide with a **Download PDF** button, a preview and a citation, and nobody has to copy files by hand.

1. **Borealis holds the master copy.** A guide is only ever updated in Borealis, by publishing a new version of its dataset. The DOI never changes and always points to the latest version.
2. **A GitHub Action copies it to the site.** Every morning (13:17 UTC: about 5 am Vancouver time in winter, 6 am in summer), the Action asks Borealis for the latest published version of each guide, using its DOI. If the PDF has changed, it saves the new one in `content/guides/` under the same file name. If nothing has changed, it does nothing.
3. **The page shows the copy.** One line on a workshop page shows the guide box, in the site's light-blue note style: "Looking for a cheat sheet? Check out our one-pager!", the Download PDF button, an Open in new tab button, a preview, and an APA citation built from the guide's details in Borealis.

The pages don't link straight to the PDF in Borealis because Borealis gives a file a new internal number with every new version, so a direct link would break. Only the DOI stays the same, and the Action takes care of the rest.

## The files

| File | What it does | Edit it? |
| --- | --- | --- |
| `_data/borealis_guides.yml` | The list of guides: one entry per guide with its DOI | Yes, to add a guide |
| `.github/workflows/sync-borealis.yml` | Runs the Action every morning, on **Run workflow**, and when the guide list changes | Only to change the schedule |
| `.github/scripts/sync_borealis.py` | Asks Borealis for each guide, downloads changed PDFs and records the citation details | Rarely |
| `_includes/borealis-pdf.html` | The guide box that appears on a page (a note box with the buttons, preview and citation) | Only to change how the box looks |
| `.github/workflows/check-site-build.yml` | Builds the site on every pull request, so a broken page is caught before it goes live | No |
| `_data/borealis_versions.json` | Each guide's version, date, authors and file details | No, the Action writes it |
| `content/guides/*.pdf` | The copies of the guides | No, the Action writes them |

## Adding a new guide

1. **Publish the guide in Borealis** as its own dataset in the collection, with the PDF as its only file. Check that the PDF isn't restricted.
2. **Add it to the guide list.** In `_data/borealis_guides.yml`, add an entry under `guides:`, keeping the spaces exactly as shown:

   ```yaml
     - id: readme
       doi: doi:10.5683/SP4/ABC123
       path: content/guides/03_readme_one-pager.pdf
   ```

   - `id` is a short name of your choice; the page uses it.
   - `doi` is the dataset's DOI, with `doi:` at the start.
   - `path` is where the PDF will live on the site. Choose it once and don't rename it later.
3. **Put the guide box on the page.** Replace the page's old "Looking for a cheat sheet?" note with this one line. The guide box is itself a note box, and it already opens with "Looking for a cheat sheet? Check out our one-pager!":

   ```liquid
   {% include borealis-pdf.html id="readme" collapsed=true %}
   ```

   - `collapsed=true` keeps the preview closed until someone clicks it.
   - `extra='...'` adds a line under the opening line, for anything else the old note said. The README page uses it for its template link:

     ```liquid
     {% include borealis-pdf.html id="readme" collapsed=true extra='Looking for a template to reuse? Check out our <a href="...">README template</a>.' %}
     ```

   - `intro='...'` replaces the opening line, if a page needs different wording.
4. **Open a pull request into `rdm-pages`.** The main branch is called `rdm-pages`, not `main`. Changing the guide list makes the Action run on the branch straight away, so the **Actions** tab shows whether it fetched the PDF before anything is merged.
5. **Merge, then check the page.** The site takes a minute or two to rebuild, and GitHub caches pages for up to about 10 minutes, so force a fresh copy with **Ctrl + F5** (Windows) or **Cmd + Shift + R** (Mac).

## Updating a guide

Update the guide in Borealis only: replace the PDF and publish a new version. The next morning the Action picks it up. To publish it straight away, go to **Actions → Sync guide PDFs from Borealis → Run workflow**.

Nothing in GitHub needs editing. The DOI, the page and the PDF's address on the site all stay the same; only the version and "Last updated" date in the citation change. Drafts are ignored, so the site only ever shows the latest *published* version.

## The citation

The guide box builds an APA citation from Borealis, for example:

> Barsky, E., Hu, B., & Choy, V. (2026). *University of British Columbia Library guide: File naming* (Version 1). Borealis. https://doi.org/10.5683/SP4/SP73CF (Last updated: 2026-11-23)

- **Authors** come from the dataset's author list in Borealis, so any change to the authors is made there.
- **Year** is the year the dataset was first published.
- **Version** is the one Borealis shows in its own citation (for example "V1"), so the two always match.
- **Last updated** is the release date of the latest version.

If Borealis doesn't return these details, the box shows a short line with the DOI instead, so the page never breaks.

## Checking that it's working

- **The Actions tab** shows every run. A green check means it worked. Opening a run shows lines like `[updated] file-naming: … v1.2` (a new PDF was saved) or `[unchanged] …` (nothing to do).
- **The morning run** happens by itself at 13:17 UTC (about 5 am Vancouver time in winter, 6 am in summer). GitHub doesn't guarantee scheduled runs: they can start late, and occasionally GitHub skips one when it is busy. A skipped day does no harm, because the next run catches up, and **Run workflow** is always there.
- **New PDFs** appear as commits by **github-actions[bot]** with the message "Sync guide PDFs from Borealis".

## When something goes wrong

| What you see | What it means | What to do |
| --- | --- | --- |
| `found 2` files matching `*.pdf` | The dataset has more than one PDF | Add `match: "name*.pdf"` to that guide's entry to pick the right one |
| `found 0` with `(restricted)` | The PDF is restricted in Borealis | Unrestrict it, or add a Borealis API token as a repository secret called `BOREALIS_API_TOKEN` |
| `HTTP Error 404` | A typo in the DOI, or the dataset isn't published | Check the DOI, including `doi:` at the start |
| `does not match its MD5 checksum` | The download was cut off | Run the workflow again |
| Push fails with a 403 | The Action isn't allowed to save | **Settings → Actions → General → Workflow permissions → Read and write** |
| Green run but the page looks old | GitHub's cache | Wait 10 minutes, then force a fresh copy |
| No **Run workflow** button | The workflow isn't on `rdm-pages` yet | Merge it first |
| The daily run stopped | GitHub pauses scheduled runs after 60 days without commits | **Actions → Sync guide PDFs from Borealis → Enable workflow** |
| The preview is blank on a phone | Android doesn't show PDFs inside a page | Nothing to fix; the Download PDF button works everywhere |

One guide failing doesn't stop the others: the Action saves every guide that worked and marks the run red, so the problem is easy to spot.

## Reusing this on another workshop site

The same setup works on any of the Research Commons Jekyll workshop sites, and with any Dataverse repository, not just Borealis.

1. Copy the five files: the two workflows, the script, the guide box and the guide list.
2. In `_data/borealis_guides.yml`, list that site's guides, and change `server:` if the guides live in a different Dataverse.
3. Check the look in `_includes/borealis-pdf.html`. The box uses the theme's `note` style, and the Download PDF button uses the note's dark blue; a site with a different theme may need different colours.
4. Make sure Actions can save to the repository (**Settings → Actions → General → Workflow permissions → Read and write**).
5. If Claude should be able to make changes there too, allow the Claude GitHub App on that repository.

{% endraw %}
