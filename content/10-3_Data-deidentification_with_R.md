---
layout: default
title: Programmatic Data De-identification with R
parent: De-identify Research Data
nav_order: 3
---

<img src="figures/work-in-progress.png" width="600"/>

We will be designing an R-based workshop during the summer of 2026. Please stay tuned...

# Introduction to Data De-identification with R
{: .no_toc} 

(Introduction to be placed here)

<details open markdown="block">
<summary>
  Table of contents
</summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

## Recap: Introduction to data de-identification
*What is sensitive data, what makes it sensitive, and why is it important to de-identify data?*

Sensitive data is “information that needs safeguarding against unwarranted access or disclosure” (Rod & Thompson, 2023), and this information can be related to both humans and animals.  

Data may be “sensitive” because it can have identifying information of various levels. Some pieces of information can immediately identify someone, or when combined with other information can identify someone. These different kinds of identifiers are called: 
- Direct identifiers: Pieces of information that will immediately identify a participant 
- Indirect identifiers: Pieces of information that could identify a participant when combined with another piece of information
- Non-identifiers: Pieces of information that are unlikely to identify a participant alone
- Hidden identifiers: Pieces of non-identifying information contextually combined that may identify a participant

It’s important to de-identify data because we want to minimize the risk of harm to individuals, communities, and animal species if there were to be a confidentiality breach. It’s also important because it helps prevent possible re-identification of participants. 

## Recap: Manual data de-identification
*The different possible methods and a demonstration performed on an example dataset*

Here are some common methods used, listed in no particular order:
- Anonymization: all variable information is removed/deleted
- Pseudonymization: variable information is replaced with pseudonyms, such as codes or numbers
- Aggregation: variable information is grouped to create categories or ranges
- Masking: variable information is obscured by techniques such as hashing or blurring
- Generalization: variable information is replaced with general or vague terms
- Local suppression: individual records are removed/deleted

We then showed some of these methods on an example dataset. What method you choose depends on the kind of sensitive data being de-identified and the research context.
- Step 1: pseudonymization for direct identifiers worker_id, email_id, and owner_id
- Step 2: aggregation for the age variable 
- Step 3: pseudonymization for variables city and orchard_id 
- Step 4: anonymization for variables immigration_stat, username_id, and comments

### Terminology 
{: .no_toc} 
UBC does not define the term “sensitive data”. Instead, UBC electronic information is classified using a schema outlined in UBC [Information Security Standard U1 (ISS-U1)](https://cio.ubc.ca/information-security-standards/U1). For the purposes of this workshop, however, we will use the term “sensitive data” to align with the terminology in Sensitive Data: Practical and Theoretical Considerations (Rod & Thompson, 2023). In this context, the term “sensitive data” will be treated as equivalent to information classified as “high risk” and “very-high risk” in UBC ISS-U1.
{: .note}

As a reminder, please make sure you’re working with a duplicate/copy file of your data for this experiment and not with your original data file(s). 

---

This workbook guides you through de-identifying the **Apple Grower Satisfaction Survey** (`content/exercise_files/10.3. Programmatic Data De-identification with R/WorkerSatisfaction_300rows.xlsx`: 300 rows, 16 columns).

### Learning objectives

- Identify privacy risks in survey data
- Apply de-identification steps in R using **dplyr**
- Export a shareable dataset and a separate data key file

### Workflow

1. **Setup** — load packages and set file paths
2. **Load and assess** — inspect raw data and review privacy risks
3. **Transform** — apply de-identification rules step by step
4. **Verify and deliver** — run QA checks and export output files

### Output files

- **`content/exercise_files/10.3. Programmatic Data De-identification with R/WorkerSatisfaction_300rows_deidentified.xlsx`** — for research team and analysts
- **`content/exercise_files/10.3. Programmatic Data De-identification with R/data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx`** — for authorized personnel only; store separately from the de-identified data (dummy example)

Do not edit the raw source file (`content/exercise_files/10.3. Programmatic Data De-identification with R/WorkerSatisfaction_300rows.xlsx`).

### Roadmap

| Part | Section | What happens |
|------|---------|--------------|
| **1** | Setup | Install packages, set paths |
| **2** | Load and assess | Read raw data; review direct IDs, dates, geography, free text |
| **3** | Transform | Remove, generalize, suppress, and pseudonymize — preview after each step |
| **4** | Verify and deliver | QA checks → export de-identified file → export data key |

| Risk | What to look for (Part 2) | What to do (Part 3) |
|------|---------------------------|---------------------|
| Direct identifiers | Names, emails, handles, owner names | Remove columns |
| Dates | `age` is date of birth | Replace with 5-year age bands |
| Geography | Small city counts | Suppress rare cities, then anonymize |
| External sources | Free-text `comments` | Remove column |
| Quasi-identifiers | Orchard names | Pseudonymize to `Orchard_01`, … |

---

# Part 1 — Setup

### Required packages

| Package | Purpose |
|---------|---------|
| `readxl` | Read the original Excel survey file |
| `dplyr` | Transform data (native pipe `\|>`) |
| `writexl` | Export Excel outputs |

Run **Install packages** once if a package is missing.

```r
# install.packages("readxl")
# install.packages("dplyr")
# install.packages("writexl")
# install.packages(c("readxl", "dplyr", "writexl"))
```

```r
library(readxl)
library(dplyr)
library(writexl)
```

```r
DATA_DIR    <- "content/exercise_files/10.3. Programmatic Data De-identification with R"
DATA_FILE   <- file.path(DATA_DIR, "WorkerSatisfaction_300rows.xlsx")
OUTPUT_FILE <- file.path(DATA_DIR, "WorkerSatisfaction_300rows_deidentified.xlsx")
KEY_DIR     <- file.path(DATA_DIR, "data_key_file")
KEY_FILE    <- file.path(KEY_DIR, "WorkerSatisfaction_data_key_DUMMY.xlsx")
K_THRESHOLD <- 5
```

**k-anonymity threshold:** categories with fewer than 5 records will be pooled before anonymization.

```r
cat("K_THRESHOLD =", K_THRESHOLD, "\n")
cat("Data key file:", KEY_FILE, "\n")
```

---

# Part 2 — Load and Assess

Load the unmodified survey and review what makes the data identifiable.

## 2.1 Load raw data

```r
raw <- read_excel(DATA_FILE, sheet = "Unmodified data")

cat("Raw data:", nrow(raw), "rows ×", ncol(raw), "columns\n")
head(raw, 10)
```

## 2.2 Direct identifiers

These variables point to a specific person and will be removed in Part 3:

| Variable | Why it is risky |
|----------|-----------------|
| `worker_id` | Full name (300 unique values) |
| `email_id` | Email address (300 unique values) |
| `username_id` | Social-media handle (265 unique values) |
| `owner_id` | Orchard owner name |

## 2.3 Dates

The column `age` stores **date of birth**, not a numeric age. Exact DOB is a strong quasi-identifier when combined with location and employer.

```r
data.frame(
  earliest     = as.character(min(as.Date(raw$age))),
  latest       = as.character(max(as.Date(raw$age))),
  unique_dates = length(unique(raw$age))
)
```

Exact DOB will be replaced with **5-year age bands** in Part 3.

## 2.4 Geography

`city` has 12 levels; `province` is always B.C. Small groups are easier to re-identify.

```r
raw |>
  count(city, sort = TRUE) |>
  mutate(rare = n < K_THRESHOLD)
```

```r
rare_cities <- raw |>
  count(city) |>
  filter(n < K_THRESHOLD) |>
  pull(city)

cat("Rare cities (n <", K_THRESHOLD, "):\n")
rare_cities
```

```r
raw |> count(immigration_stat, sort = TRUE)
```

> **Note:** Pool rare cities to `"Other BC community"`, then replace all city names with codes (`City_01`, …). Immigration counts are checked here; recoding is only needed if any group falls below 5.

## 2.5 External sources (free text)

The `comments` field can name people, employers, platforms, and birth years — even after other columns are cleaned.

```r
raw |>
  filter(comments != "None") |>
  slice(1:10) |>
  select(comments)
```

> **Note:** Remove `comments` entirely. Free text cannot be reliably de-identified without manual review.

## 2.6 Quasi-identifiers (orchards)

Orchard names link respondents to a specific workplace. They will be pseudonymized in Part 3.

```r
raw |> count(orchard_id, sort = TRUE)
```

> **Note:** Replace orchard names with non-descriptive codes (`Orchard_01`, …).

---

# Part 3 — Transform

Apply each rule from Part 2. Run chunks in order; each step shows **10 rows** of the updated dataframe.

## 3.1 Remove direct identifiers and comments

```r
direct_ids <- c("worker_id", "email_id", "username_id", "owner_id")

step1 <- raw |>
  select(-all_of(direct_ids), -comments)

cat("Step 3.1:", nrow(step1), "rows ×", ncol(step1), "columns\n")
head(step1, 10)
```

## 3.2 Generalize date of birth

```r
to_age_band <- function(dob) {
  yrs <- as.integer(difftime(Sys.Date(), as.Date(dob), units = "days") / 365.25)
  if (yrs < 25)      "18-24"
  else if (yrs < 35) "25-34"
  else if (yrs < 45) "35-44"
  else if (yrs < 55) "45-54"
  else               "55+"
}

step2 <- step1 |>
  mutate(age_band = sapply(age, to_age_band)) |>
  select(-age) |>
  relocate(age_band, .before = immigration_stat)

cat("Step 3.2:", nrow(step2), "rows ×", ncol(step2), "columns\n")
head(step2, 10)
```

## 3.3 Suppress rare cities

```r
step3 <- step2 |>
  mutate(city = if_else(city %in% rare_cities, "Other BC community", city))

cat("Step 3.3:", nrow(step3), "rows ×", ncol(step3), "columns\n")
head(step3, 10)
```

```r
step3 |> count(city, sort = TRUE)
```

## 3.4 Anonymize city

```r
step4 <- step3 |>
  mutate(city = paste0(
    "City_", sprintf("%02d", as.integer(factor(city)))
  ))

cat("Step 3.4:", nrow(step4), "rows ×", ncol(step4), "columns\n")
head(step4, 10)
```

```r
step4 |> count(city, sort = TRUE)
```

## 3.5 Pseudonymize orchard

```r
step5 <- step4 |>
  mutate(orchard_id = paste0(
    "Orchard_", sprintf("%02d", as.integer(factor(orchard_id)))
  ))

deid <- step5

cat("Step 3.5 — final:", nrow(deid), "rows ×", ncol(deid), "columns\n")
head(deid, 10)
```

```r
deid |> count(orchard_id, sort = TRUE)
```

### What changed

| Removed | Transformed |
|---------|-------------|
| `worker_id`, `email_id`, `username_id`, `owner_id`, `comments`, exact DOB (`age`) | `age` → `age_band`; rare cities pooled; `city` → `City_01` …; `orchard_id` → `Orchard_01` … |

---

# Part 4 — Verify and Deliver

## 4.1 QA checks

Confirm the de-identified data is safe to export. All checks should show `TRUE`.

```r
data.frame(
  check = c(
    "No direct ID columns",
    "No comments column",
    "No exact DOB column",
    "Row count unchanged",
    "Rare cities suppressed",
    "Cities anonymized",
    "Orchards pseudonymized"
  ),
  passed = c(
    !any(direct_ids %in% names(deid)),
    !"comments" %in% names(deid),
    !"age" %in% names(deid),
    nrow(deid) == nrow(raw),
    !any(rare_cities %in% deid$city),
    !any(unique(raw$city) %in% deid$city),
    !any(unique(raw$orchard_id) %in% deid$orchard_id)
  )
)
```

```r
data.frame(
  rows               = nrow(deid),
  columns            = ncol(deid),
  smallest_city      = min(table(deid$city)),
  smallest_age_band  = min(table(deid$age_band)),
  smallest_orchard   = min(table(deid$orchard_id))
)
```

> **Note:** Each group should ideally have at least 5 records, or be pooled into a broader category.

## 4.2 Export de-identified dataset

This is the file you can share for analysis. It does **not** include the data key.

```r
write_xlsx(deid, OUTPUT_FILE)

cat("Exported:", OUTPUT_FILE, "\n")
cat("Rows:", nrow(deid), "| Columns:", ncol(deid), "\n\n")
cat("Preview of exported data:\n")
head(deid, 10)
```

## 4.3 Data key file (DUMMY — illustrative only)

Keeping the data key file well protected is essential because it is the sole mechanism that can re-identify individuals in otherwise de-identified research data, and its compromise can undermine confidentiality protections and cause harm to participants. In the UBC environment, the key file must be stored separately from research data on UBC-approved secure systems, with access restricted to authorized personnel only and never stored on personal devices or unapproved cloud services.

Here is an example of a data key file for the work described above; this is a **dummy file provided for illustrative purposes only**, and in real-world research settings, such files must never be shared on public systems.

**File path:** `content/exercise_files/10.3. Programmatic Data De-identification with R/data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx`

| Sheet | Contents |
|-------|----------|
| `README` | Dummy disclaimer and UBC storage requirements |
| `orchard_key` | Original orchard name → pseudonym code |
| `city_key` | City label after suppression → pseudonym code |
| `rare_city_suppress` | Cities pooled to `"Other BC community"` |

The key holds **orchard and city code mappings only** — not worker names, emails, or other direct identifiers removed in step 3.1.

```r
orchard_key <- step1 |>
  distinct(orchard_id) |>
  arrange(orchard_id) |>
  transmute(
    original_orchard = orchard_id,
    pseudonym_code   = paste0("Orchard_", sprintf("%02d", row_number()))
  )

city_key <- step3 |>
  distinct(city) |>
  arrange(city) |>
  transmute(
    city_after_suppression = city,
    pseudonym_code         = paste0("City_", sprintf("%02d", row_number()))
  )

if (length(rare_cities) > 0) {
  rare_city_key <- data.frame(
    original_city = rare_cities,
    pooled_to     = "Other BC community"
  )
} else {
  rare_city_key <- data.frame(
    original_city = "(none — all cities at or above k threshold)",
    pooled_to     = NA_character_
  )
}

key_readme <- data.frame(
  field = c(
    "File status",
    "Purpose",
    "Contains",
    "Storage requirement (UBC)"
  ),
  description = c(
    "DUMMY — illustrative example only; not for production use",
    "Reverse pseudonym codes for orchard and city in the de-identified file",
    "Orchard map, city map, rare-city suppression list — no worker names or emails",
    "Store separately from de-identified data on UBC-approved secure systems; authorized access only"
  )
)

cat("Orchard key:\n")
head(orchard_key, 10)

cat("\nCity key:\n")
city_key
```

```r
dir.create(KEY_DIR, showWarnings = FALSE)

write_xlsx(
  list(
    README             = key_readme,
    orchard_key        = orchard_key,
    city_key           = city_key,
    rare_city_suppress = rare_city_key
  ),
  KEY_FILE
)

cat("Data key exported:", KEY_FILE, "\n")
cat("Sheets: README, orchard_key, city_key, rare_city_suppress\n")
cat("Store separately from", OUTPUT_FILE, "— never on public systems.\n")
```

---

# Closing Summary

| Stage | What changed |
|-------|--------------|
| Direct identifiers | Removed `worker_id`, `email_id`, `username_id`, `owner_id` |
| External sources | Removed `comments` |
| Dates | `age` (DOB) → `age_band` (5-year groups) |
| Geography | Rare cities pooled; all cities → `City_01` … |
| Quasi-identifiers | `orchard_id` → `Orchard_01` …; mappings in `content/exercise_files/10.3. Programmatic Data De-identification with R/data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx` (dummy, separate storage) |

The de-identified dataset keeps all satisfaction and treatment ratings for analysis while substantially lowering re-identification risk. The data key remains the only link back to original orchard and city names — protect it accordingly.
