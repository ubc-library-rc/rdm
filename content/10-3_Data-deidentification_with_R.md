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

# Introduction

This workbook guides you through de-identifying the **Apple Grower
Satisfaction Survey** (`WorkerSatisfaction_300rows.xlsx`: 300 rows, 16
columns).

### Learning objectives

-   Identify privacy risks in survey data
-   Apply de-identification steps in R using **dplyr**
-   Export a shareable dataset and a separate data key file

### Workflow

1.  **Setup** — load packages and set file paths
2.  **Load and assess** — inspect raw data and review privacy risks
3.  **Transform** — apply de-identification rules step by step
4.  **Verify and deliver** — run QA checks and export output files

### Output files

-   **`WorkerSatisfaction_300rows_deidentified.xlsx`** — for research
    (e.g. public access…)
-   **`data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx`** — for
    authorized personnel only; store separately from the de-identified
    data (dummy example)

Do not edit the raw source file (`WorkerSatisfaction_300rows.xlsx`).

### Roadmap

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr>
<th>Part</th>
<th>Section</th>
<th>What happens</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>1</strong></td>
<td>Setup</td>
<td>Install packages, set paths</td>
</tr>
<tr>
<td><strong>2</strong></td>
<td>Load and assess</td>
<td>Read raw data; review direct IDs, dates, geography, free text</td>
</tr>
<tr>
<td><strong>3</strong></td>
<td>Transform</td>
<td>Remove comments and de-identify identifiers</td>
</tr>
<tr>
<td><strong>4</strong></td>
<td>Verify and deliver</td>
<td>QA checks → export de-identified file → export data key</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 40%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Risk</th>
<th>What to look for (Part 2)</th>
<th>What to do (Part 3)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Direct identifiers</td>
<td>Names, emails, handles, owner names</td>
<td>De-identify to <code>Worker_01</code>, <code>Email_01</code>, …</td>
</tr>
<tr>
<td>Dates</td>
<td><code>age</code> is date of birth</td>
<td>Group into 5-year age bands</td>
</tr>
<tr>
<td>Geography</td>
<td>Small city counts</td>
<td>Suppress rare cities, then de-identify to <code>City_01</code>,
…</td>
</tr>
<tr>
<td>External sources</td>
<td>Free-text <code>comments</code></td>
<td>Remove column</td>
</tr>
<tr>
<td>Quasi-identifiers</td>
<td>Orchard names</td>
<td>De-identify to <code>Orchard_01</code>, …</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

# Part 1 — Setup

> **R and RStudio (workshop prerequisite)**  
> This workbook assumes you have **R** and **RStudio** installed and can
> open and run `.Rmd` files. If you have not set these up yet, follow
> the UBC Library Research Commons guide:  
> [Installing R and
> RStudio](https://ubc-library-rc.github.io/IntroR/content/installation.html)

### Required packages

<table>
<thead>
<tr>
<th>Package</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>readxl</code></td>
<td>Read the original Excel survey file</td>
</tr>
<tr>
<td><code>dplyr</code></td>
<td>Transform data (native pipe <code>\|&gt;</code>)</td>
</tr>
<tr>
<td><code>writexl</code></td>
<td>Export Excel outputs</td>
</tr>
</tbody>
</table>

Run **Install packages** once if a package is missing.

    # install.packages("readxl")
    # install.packages("dplyr")
    # install.packages("writexl")
    # install.packages(c("readxl", "dplyr", "writexl"))

    library(readxl)
    library(dplyr)
    library(writexl)

    DATA_FILE   <- "WorkerSatisfaction_300rows.xlsx"
    OUTPUT_FILE <- "WorkerSatisfaction_300rows_deidentified.xlsx"
    KEY_DIR     <- "data_key_file"
    KEY_FILE    <- file.path(KEY_DIR, "WorkerSatisfaction_data_key_DUMMY.xlsx")
    K_THRESHOLD <- 5

**k-anonymity threshold:** categories with fewer than 5 records will be
pooled before anonymization.

    cat("K_THRESHOLD =", K_THRESHOLD, "\n")

    ## K_THRESHOLD = 5

    cat("Data key file:", KEY_FILE, "\n")

    ## Data key file: data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx

------------------------------------------------------------------------

# Part 2 — Load and Assess

Load the unmodified survey and review what makes the data identifiable.

## 2.1 Load raw data

    raw <- read_excel(DATA_FILE, sheet = "Unmodified data")

    cat("Raw data:", nrow(raw), "rows ×", ncol(raw), "columns\n")

    ## Raw data: 300 rows <U+00D7> 16 columns

    head(raw, 10)

    ## # A tibble: 10 x 16
    ##    worker_id        email_id age                 immigration_stat city  province
    ##    <chr>            <chr>    <dttm>              <chr>            <chr> <chr>   
    ##  1 James Strange    james.s~ 1998-09-10 00:00:00 Non-immigrant    Kelo~ B.C.    
    ##  2 Maya Liya        maya.li~ 1994-08-04 00:00:00 Immigrant        Kelo~ B.C.    
    ##  3 Amelio Beal      amelio.~ 1995-01-02 00:00:00 Non-permanent r~ West~ B.C.    
    ##  4 Cara Sahara      cara.sa~ 1991-03-22 00:00:00 Non-permanent r~ West~ B.C.    
    ##  5 Neiv Rieg        neivr@g~ 1990-07-15 00:00:00 Non-permanent r~ Vict~ B.C.    
    ##  6 Troy Ahoy        tahoy@y~ 1988-06-06 00:00:00 Immigrant        Vict~ B.C.    
    ##  7 Dave Mahew       dmahew@~ 2000-11-11 00:00:00 Non-immigrant    Vern~ B.C.    
    ##  8 Jamie Thomas     jamiet@~ 1992-12-18 00:00:00 Immigrant        Vern~ B.C.    
    ##  9 Betty Stills     bettys5~ 1997-09-06 00:00:00 Non-permanent r~ Cobb~ B.C.    
    ## 10 Enrique Iglasias ei123@h~ 1985-10-16 00:00:00 Non-permanent r~ Cobb~ B.C.    
    ## # i 10 more variables: orchard_id <chr>, owner_id <chr>, username_id <chr>,
    ## #   sns_worked <dbl>, sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>,
    ## #   cmf_manager <dbl>, sat_work_overall <dbl>, comments <chr>

## 2.2 Direct identifiers

These variables point to a specific person. They will be
**de-identified** (not dropped) so rows stay linkable within the dataset
without exposing real names or contact details:

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr>
<th>Variable</th>
<th>Why it is risky</th>
<th>Code prefix</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>worker_id</code></td>
<td>Full name (300 unique values)</td>
<td><code>Worker_001</code>, …</td>
</tr>
<tr>
<td><code>email_id</code></td>
<td>Email address (300 unique values)</td>
<td><code>Email_001</code>, …</td>
</tr>
<tr>
<td><code>username_id</code></td>
<td>Social-media handle (265 unique values)</td>
<td><code>Username_001</code>, …</td>
</tr>
<tr>
<td><code>owner_id</code></td>
<td>Orchard owner name (12 unique values)</td>
<td><code>Owner_01</code>, …</td>
</tr>
</tbody>
</table>

## 2.3 Dates

The column `age` stores **date of birth**, not a numeric age. Exact DOB
is a strong quasi-identifier when combined with location and employer.

    data.frame(
      earliest     = as.character(min(as.Date(raw$age))),
      latest       = as.character(max(as.Date(raw$age))),
      unique_dates = length(unique(raw$age))
    )

    ##     earliest     latest unique_dates
    ## 1 1970-02-20 2000-11-11          295

Exact DOB will be replaced with **5-year age bands** in Part 3.

## 2.4 Geography

`city` has 12 levels; `province` is always B.C. Small groups are easier
to re-identify.

    raw |>
      count(city, sort = TRUE) |>
      mutate(rare = n < K_THRESHOLD)

    ## # A tibble: 12 x 3
    ##    city             n rare 
    ##    <chr>        <int> <lgl>
    ##  1 Victoria        33 FALSE
    ##  2 Summerland      32 FALSE
    ##  3 Keremeos        31 FALSE
    ##  4 Kelowna         29 FALSE
    ##  5 West Kelowna    29 FALSE
    ##  6 Peachland       27 FALSE
    ##  7 Cobble Hill     26 FALSE
    ##  8 Vernon          24 FALSE
    ##  9 Naramata        18 FALSE
    ## 10 Oliver          18 FALSE
    ## 11 Osoyoos         17 FALSE
    ## 12 Penticton       16 FALSE

    rare_cities <- raw |>
      count(city) |>
      filter(n < K_THRESHOLD) |>
      pull(city)

    cat("Rare cities (n <", K_THRESHOLD, "):\n")

    ## Rare cities (n < 5 ):

    rare_cities

    ## character(0)

    raw |> count(immigration_stat, sort = TRUE)

    ## # A tibble: 3 x 2
    ##   immigration_stat           n
    ##   <chr>                  <int>
    ## 1 Non-permanent resident   107
    ## 2 Non-immigrant            103
    ## 3 Immigrant                 90

> **Note:** Recoding is only needed if any group falls below 5. For
> example, we would pool rare cities to `"Other BC community"` if count
> is below 5.

## 2.5 External sources (free text)

The `comments` field can name people, employers, platforms, and birth
years — even after other columns are cleaned.

    raw |>
      filter(comments != "None") |>
      slice(1:10) |>
      select(comments)

    ## # A tibble: 10 x 1
    ##    comments                                                                     
    ##    <chr>                                                                        
    ##  1 I get that I'm a farm worker and grinding is part of the job, but it'd be ni~
    ##  2 I don't mind the actual work, but the people I work with and the owners like~
    ##  3 I only like this job because I can make good money, everything else sucks. I~
    ##  4 The hours and work are hard, but it's good money and I love the team we have~
    ##  5 Hard but great work                                                          
    ##  6 I'm an apple picker, it is what it is                                        
    ##  7 It's a good summer job to help me pay for school, definitely not something I~
    ##  8 The owner's wife is such a sweetheart, but I don't like the owner himself.  ~
    ##  9 I hate this job and everybody who works here.  the guys I work with are awfu~
    ## 10 I don't love the job but I stay for the money and the routine.

> **Note:** Remove `comments` entirely. Free text cannot be reliably
> de-identified without manual review.

## 2.6 Quasi-identifiers (orchards)

Orchard names link respondents to a specific workplace. They will be
de-identified in Part 3.

    raw |> count(orchard_id, sort = TRUE)

    ## # A tibble: 12 x 2
    ##    orchard_id              n
    ##    <chr>               <int>
    ##  1 Billie's Apples        33
    ##  2 Okanagan Fresh         32
    ##  3 Valley View Apples     31
    ##  4 Applejacks             29
    ##  5 West Kelowna Apples    29
    ##  6 Lakeside Groves        27
    ##  7 Country Apples         26
    ##  8 Bon Appletit           24
    ##  9 Golden Valley Farms    18
    ## 10 Ridgeline Orchard      18
    ## 11 Peak Harvest Co        17
    ## 12 Sunrise Orchards       16

> **Note:** Replace orchard names with non-descriptive codes
> (`Orchard_01`, …).

------------------------------------------------------------------------

# Part 3 — Transform

Apply each rule from Part 2. Run chunks in order; each step shows **10
rows** of the updated dataframe.

    direct_ids <- c("worker_id", "email_id", "username_id", "owner_id")

## 3.1 Remove comments

Free text cannot be reliably de-identified; drop this column only.

    step1 <- raw |>
      select(-comments)

    cat("Step 3.1:", nrow(step1), "rows ×", ncol(step1), "columns\n")

    ## Step 3.1: 300 rows <U+00D7> 15 columns

    head(step1, 10)

    ## # A tibble: 10 x 15
    ##    worker_id        email_id age                 immigration_stat city  province
    ##    <chr>            <chr>    <dttm>              <chr>            <chr> <chr>   
    ##  1 James Strange    james.s~ 1998-09-10 00:00:00 Non-immigrant    Kelo~ B.C.    
    ##  2 Maya Liya        maya.li~ 1994-08-04 00:00:00 Immigrant        Kelo~ B.C.    
    ##  3 Amelio Beal      amelio.~ 1995-01-02 00:00:00 Non-permanent r~ West~ B.C.    
    ##  4 Cara Sahara      cara.sa~ 1991-03-22 00:00:00 Non-permanent r~ West~ B.C.    
    ##  5 Neiv Rieg        neivr@g~ 1990-07-15 00:00:00 Non-permanent r~ Vict~ B.C.    
    ##  6 Troy Ahoy        tahoy@y~ 1988-06-06 00:00:00 Immigrant        Vict~ B.C.    
    ##  7 Dave Mahew       dmahew@~ 2000-11-11 00:00:00 Non-immigrant    Vern~ B.C.    
    ##  8 Jamie Thomas     jamiet@~ 1992-12-18 00:00:00 Immigrant        Vern~ B.C.    
    ##  9 Betty Stills     bettys5~ 1997-09-06 00:00:00 Non-permanent r~ Cobb~ B.C.    
    ## 10 Enrique Iglasias ei123@h~ 1985-10-16 00:00:00 Non-permanent r~ Cobb~ B.C.    
    ## # i 9 more variables: orchard_id <chr>, owner_id <chr>, username_id <chr>,
    ## #   sns_worked <dbl>, sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>,
    ## #   cmf_manager <dbl>, sat_work_overall <dbl>

## 3.2 De-identify direct identifiers

Replace names, emails, handles, and owner names with non-descriptive
codes (same approach as city and orchard).

    step2 <- step1 |>
      mutate(
        worker_id   = paste0("Worker_",   sprintf("%03d", as.integer(factor(worker_id)))),
        email_id    = paste0("Email_",    sprintf("%03d", as.integer(factor(email_id)))),
        username_id = paste0("Username_", sprintf("%03d", as.integer(factor(username_id)))),
        owner_id    = paste0("Owner_",    sprintf("%02d", as.integer(factor(owner_id))))
      )

    cat("Step 3.2:", nrow(step2), "rows ×", ncol(step2), "columns\n")

    ## Step 3.2: 300 rows <U+00D7> 15 columns

    head(step2, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age                 immigration_stat      city  province
    ##    <chr>      <chr>     <dttm>              <chr>                 <chr> <chr>   
    ##  1 Worker_114 Email_110 1998-09-10 00:00:00 Non-immigrant         Kelo~ B.C.    
    ##  2 Worker_170 Email_163 1994-08-04 00:00:00 Immigrant             Kelo~ B.C.    
    ##  3 Worker_010 Email_011 1995-01-02 00:00:00 Non-permanent reside~ West~ B.C.    
    ##  4 Worker_035 Email_033 1991-03-22 00:00:00 Non-permanent reside~ West~ B.C.    
    ##  5 Worker_194 Email_193 1990-07-15 00:00:00 Non-permanent reside~ Vict~ B.C.    
    ##  6 Worker_276 Email_261 1988-06-06 00:00:00 Immigrant             Vict~ B.C.    
    ##  7 Worker_054 Email_057 2000-11-11 00:00:00 Non-immigrant         Vern~ B.C.    
    ##  8 Worker_117 Email_114 1992-12-18 00:00:00 Immigrant             Vern~ B.C.    
    ##  9 Worker_022 Email_021 1997-09-06 00:00:00 Non-permanent reside~ Cobb~ B.C.    
    ## 10 Worker_064 Email_061 1985-10-16 00:00:00 Non-permanent reside~ Cobb~ B.C.    
    ## # i 9 more variables: orchard_id <chr>, owner_id <chr>, username_id <chr>,
    ## #   sns_worked <dbl>, sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>,
    ## #   cmf_manager <dbl>, sat_work_overall <dbl>

    step2 |>
      select(all_of(direct_ids)) |>
      slice(1:5)

    ## # A tibble: 5 x 4
    ##   worker_id  email_id  username_id  owner_id
    ##   <chr>      <chr>     <chr>        <chr>   
    ## 1 Worker_114 Email_110 Username_154 Owner_03
    ## 2 Worker_170 Email_163 Username_040 Owner_03
    ## 3 Worker_010 Email_011 Username_088 Owner_08
    ## 4 Worker_035 Email_033 Username_104 Owner_08
    ## 5 Worker_194 Email_193 Username_046 Owner_02

## 3.3 Generalize date of birth

    to_age_band <- function(dob) {
      yrs <- as.integer(difftime(Sys.Date(), as.Date(dob), units = "days") / 365.25)
      if (yrs < 25)      "18-24"
      else if (yrs < 35) "25-34"
      else if (yrs < 45) "35-44"
      else if (yrs < 55) "45-54"
      else               "55+"
    }

    step3 <- step2 |>
      mutate(age_band = sapply(age, to_age_band)) |>
      select(-age) |>
      relocate(age_band, .before = immigration_stat)

    cat("Step 3.3:", nrow(step3), "rows ×", ncol(step3), "columns\n")

    ## Step 3.3: 300 rows <U+00D7> 15 columns

    head(step3, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age_band immigration_stat      city  province orchard_id
    ##    <chr>      <chr>     <chr>    <chr>                 <chr> <chr>    <chr>     
    ##  1 Worker_114 Email_110 25-34    Non-immigrant         Kelo~ B.C.     Applejacks
    ##  2 Worker_170 Email_163 25-34    Immigrant             Kelo~ B.C.     Applejacks
    ##  3 Worker_010 Email_011 25-34    Non-permanent reside~ West~ B.C.     West Kelo~
    ##  4 Worker_035 Email_033 35-44    Non-permanent reside~ West~ B.C.     West Kelo~
    ##  5 Worker_194 Email_193 35-44    Non-permanent reside~ Vict~ B.C.     Billie's ~
    ##  6 Worker_276 Email_261 35-44    Immigrant             Vict~ B.C.     Billie's ~
    ##  7 Worker_054 Email_057 25-34    Non-immigrant         Vern~ B.C.     Bon Apple~
    ##  8 Worker_117 Email_114 25-34    Immigrant             Vern~ B.C.     Bon Apple~
    ##  9 Worker_022 Email_021 25-34    Non-permanent reside~ Cobb~ B.C.     Country A~
    ## 10 Worker_064 Email_061 35-44    Non-permanent reside~ Cobb~ B.C.     Country A~
    ## # i 8 more variables: owner_id <chr>, username_id <chr>, sns_worked <dbl>,
    ## #   sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>, cmf_manager <dbl>,
    ## #   sat_work_overall <dbl>

## 3.4 Suppress rare cities

    step4 <- step3 |>
      mutate(city = if_else(city %in% rare_cities, "Other BC community", city))

    cat("Step 3.4:", nrow(step4), "rows ×", ncol(step4), "columns\n")

    ## Step 3.4: 300 rows <U+00D7> 15 columns

    head(step4, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age_band immigration_stat      city  province orchard_id
    ##    <chr>      <chr>     <chr>    <chr>                 <chr> <chr>    <chr>     
    ##  1 Worker_114 Email_110 25-34    Non-immigrant         Kelo~ B.C.     Applejacks
    ##  2 Worker_170 Email_163 25-34    Immigrant             Kelo~ B.C.     Applejacks
    ##  3 Worker_010 Email_011 25-34    Non-permanent reside~ West~ B.C.     West Kelo~
    ##  4 Worker_035 Email_033 35-44    Non-permanent reside~ West~ B.C.     West Kelo~
    ##  5 Worker_194 Email_193 35-44    Non-permanent reside~ Vict~ B.C.     Billie's ~
    ##  6 Worker_276 Email_261 35-44    Immigrant             Vict~ B.C.     Billie's ~
    ##  7 Worker_054 Email_057 25-34    Non-immigrant         Vern~ B.C.     Bon Apple~
    ##  8 Worker_117 Email_114 25-34    Immigrant             Vern~ B.C.     Bon Apple~
    ##  9 Worker_022 Email_021 25-34    Non-permanent reside~ Cobb~ B.C.     Country A~
    ## 10 Worker_064 Email_061 35-44    Non-permanent reside~ Cobb~ B.C.     Country A~
    ## # i 8 more variables: owner_id <chr>, username_id <chr>, sns_worked <dbl>,
    ## #   sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>, cmf_manager <dbl>,
    ## #   sat_work_overall <dbl>

    step4 |> count(city, sort = TRUE)

    ## # A tibble: 12 x 2
    ##    city             n
    ##    <chr>        <int>
    ##  1 Victoria        33
    ##  2 Summerland      32
    ##  3 Keremeos        31
    ##  4 Kelowna         29
    ##  5 West Kelowna    29
    ##  6 Peachland       27
    ##  7 Cobble Hill     26
    ##  8 Vernon          24
    ##  9 Naramata        18
    ## 10 Oliver          18
    ## 11 Osoyoos         17
    ## 12 Penticton       16

## 3.5 De-identify city

    step5 <- step4 |>
      mutate(city = paste0(
        "City_", sprintf("%02d", as.integer(factor(city)))
      ))

    cat("Step 3.5:", nrow(step5), "rows ×", ncol(step5), "columns\n")

    ## Step 3.5: 300 rows <U+00D7> 15 columns

    head(step5, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age_band immigration_stat      city  province orchard_id
    ##    <chr>      <chr>     <chr>    <chr>                 <chr> <chr>    <chr>     
    ##  1 Worker_114 Email_110 25-34    Non-immigrant         City~ B.C.     Applejacks
    ##  2 Worker_170 Email_163 25-34    Immigrant             City~ B.C.     Applejacks
    ##  3 Worker_010 Email_011 25-34    Non-permanent reside~ City~ B.C.     West Kelo~
    ##  4 Worker_035 Email_033 35-44    Non-permanent reside~ City~ B.C.     West Kelo~
    ##  5 Worker_194 Email_193 35-44    Non-permanent reside~ City~ B.C.     Billie's ~
    ##  6 Worker_276 Email_261 35-44    Immigrant             City~ B.C.     Billie's ~
    ##  7 Worker_054 Email_057 25-34    Non-immigrant         City~ B.C.     Bon Apple~
    ##  8 Worker_117 Email_114 25-34    Immigrant             City~ B.C.     Bon Apple~
    ##  9 Worker_022 Email_021 25-34    Non-permanent reside~ City~ B.C.     Country A~
    ## 10 Worker_064 Email_061 35-44    Non-permanent reside~ City~ B.C.     Country A~
    ## # i 8 more variables: owner_id <chr>, username_id <chr>, sns_worked <dbl>,
    ## #   sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>, cmf_manager <dbl>,
    ## #   sat_work_overall <dbl>

    step5 |> count(city, sort = TRUE)

    ## # A tibble: 12 x 2
    ##    city        n
    ##    <chr>   <int>
    ##  1 City_11    33
    ##  2 City_09    32
    ##  3 City_03    31
    ##  4 City_02    29
    ##  5 City_12    29
    ##  6 City_07    27
    ##  7 City_01    26
    ##  8 City_10    24
    ##  9 City_04    18
    ## 10 City_05    18
    ## 11 City_06    17
    ## 12 City_08    16

## 3.6 De-identify orchard

    step6 <- step5 |>
      mutate(orchard_id = paste0(
        "Orchard_", sprintf("%02d", as.integer(factor(orchard_id)))
      ))

    deid <- step6

    cat("Step 3.6 — final:", nrow(deid), "rows ×", ncol(deid), "columns\n")

    ## Step 3.6 <U+2014> final: 300 rows <U+00D7> 15 columns

    head(deid, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age_band immigration_stat      city  province orchard_id
    ##    <chr>      <chr>     <chr>    <chr>                 <chr> <chr>    <chr>     
    ##  1 Worker_114 Email_110 25-34    Non-immigrant         City~ B.C.     Orchard_01
    ##  2 Worker_170 Email_163 25-34    Immigrant             City~ B.C.     Orchard_01
    ##  3 Worker_010 Email_011 25-34    Non-permanent reside~ City~ B.C.     Orchard_12
    ##  4 Worker_035 Email_033 35-44    Non-permanent reside~ City~ B.C.     Orchard_12
    ##  5 Worker_194 Email_193 35-44    Non-permanent reside~ City~ B.C.     Orchard_02
    ##  6 Worker_276 Email_261 35-44    Immigrant             City~ B.C.     Orchard_02
    ##  7 Worker_054 Email_057 25-34    Non-immigrant         City~ B.C.     Orchard_03
    ##  8 Worker_117 Email_114 25-34    Immigrant             City~ B.C.     Orchard_03
    ##  9 Worker_022 Email_021 25-34    Non-permanent reside~ City~ B.C.     Orchard_04
    ## 10 Worker_064 Email_061 35-44    Non-permanent reside~ City~ B.C.     Orchard_04
    ## # i 8 more variables: owner_id <chr>, username_id <chr>, sns_worked <dbl>,
    ## #   sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>, cmf_manager <dbl>,
    ## #   sat_work_overall <dbl>

    deid |> count(orchard_id, sort = TRUE)

    ## # A tibble: 12 x 2
    ##    orchard_id     n
    ##    <chr>      <int>
    ##  1 Orchard_02    33
    ##  2 Orchard_07    32
    ##  3 Orchard_11    31
    ##  4 Orchard_01    29
    ##  5 Orchard_12    29
    ##  6 Orchard_06    27
    ##  7 Orchard_04    26
    ##  8 Orchard_03    24
    ##  9 Orchard_05    18
    ## 10 Orchard_09    18
    ## 11 Orchard_08    17
    ## 12 Orchard_10    16

### What changed

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th>Removed</th>
<th>De-identified / transformed</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>comments</code></td>
<td><code>worker_id</code> → <code>Worker_001</code> …;
<code>email_id</code> → <code>Email_001</code> …;
<code>username_id</code> → <code>Username_001</code> …;
<code>owner_id</code> → <code>Owner_01</code> …</td>
</tr>
<tr>
<td>exact DOB (<code>age</code>)</td>
<td><code>age</code> → <code>age_band</code>; rare cities pooled;
<code>city</code> → <code>City_01</code> …; <code>orchard_id</code> →
<code>Orchard_01</code> …</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

# Part 4 — Verify and Deliver

## 4.1 QA checks

Confirm the de-identified data is safe to export. All checks should show
`TRUE`.

    data.frame(
      check = c(
        "Direct IDs de-identified",
        "No comments column",
        "No exact DOB column",
        "Row count unchanged",
        "Rare cities suppressed",
        "Cities de-identified",
        "Orchards de-identified"
      ),
      passed = c(
        !any(unique(raw$worker_id) %in% deid$worker_id),
        !"comments" %in% names(deid),
        !"age" %in% names(deid),
        nrow(deid) == nrow(raw),
        !any(rare_cities %in% deid$city),
        !any(unique(raw$city) %in% deid$city),
        !any(unique(raw$orchard_id) %in% deid$orchard_id)
      )
    )

    ##                      check passed
    ## 1 Direct IDs de-identified   TRUE
    ## 2       No comments column   TRUE
    ## 3      No exact DOB column   TRUE
    ## 4      Row count unchanged   TRUE
    ## 5   Rare cities suppressed   TRUE
    ## 6     Cities de-identified   TRUE
    ## 7   Orchards de-identified   TRUE

Add checks for email, username, and owner de-identification:

    data.frame(
      check = c(
        "Emails de-identified",
        "Usernames de-identified",
        "Owners de-identified"
      ),
      passed = c(
        !any(unique(raw$email_id) %in% deid$email_id),
        !any(unique(na.omit(raw$username_id)) %in% deid$username_id),
        !any(unique(raw$owner_id) %in% deid$owner_id)
      )
    )

    ##                     check passed
    ## 1    Emails de-identified   TRUE
    ## 2 Usernames de-identified   TRUE
    ## 3    Owners de-identified   TRUE

    data.frame(
      rows               = nrow(deid),
      columns            = ncol(deid),
      smallest_city      = min(table(deid$city)),
      smallest_age_band  = min(table(deid$age_band)),
      smallest_orchard   = min(table(deid$orchard_id))
    )

    ##   rows columns smallest_city smallest_age_band smallest_orchard
    ## 1  300      15            16                14               16

> **Note:** Each group should ideally have at least 5 records, or be
> pooled into a broader category.

## 4.2 Export de-identified dataset

This is the file you can share for analysis. It does **not** include the
data key.

    write_xlsx(deid, OUTPUT_FILE)

    cat("Exported:", OUTPUT_FILE, "\n")

    ## Exported: WorkerSatisfaction_300rows_deidentified.xlsx

    cat("Rows:", nrow(deid), "| Columns:", ncol(deid), "\n\n")

    ## Rows: 300 | Columns: 15

    cat("Preview of exported data:\n")

    ## Preview of exported data:

    head(deid, 10)

    ## # A tibble: 10 x 15
    ##    worker_id  email_id  age_band immigration_stat      city  province orchard_id
    ##    <chr>      <chr>     <chr>    <chr>                 <chr> <chr>    <chr>     
    ##  1 Worker_114 Email_110 25-34    Non-immigrant         City~ B.C.     Orchard_01
    ##  2 Worker_170 Email_163 25-34    Immigrant             City~ B.C.     Orchard_01
    ##  3 Worker_010 Email_011 25-34    Non-permanent reside~ City~ B.C.     Orchard_12
    ##  4 Worker_035 Email_033 35-44    Non-permanent reside~ City~ B.C.     Orchard_12
    ##  5 Worker_194 Email_193 35-44    Non-permanent reside~ City~ B.C.     Orchard_02
    ##  6 Worker_276 Email_261 35-44    Immigrant             City~ B.C.     Orchard_02
    ##  7 Worker_054 Email_057 25-34    Non-immigrant         City~ B.C.     Orchard_03
    ##  8 Worker_117 Email_114 25-34    Immigrant             City~ B.C.     Orchard_03
    ##  9 Worker_022 Email_021 25-34    Non-permanent reside~ City~ B.C.     Orchard_04
    ## 10 Worker_064 Email_061 35-44    Non-permanent reside~ City~ B.C.     Orchard_04
    ## # i 8 more variables: owner_id <chr>, username_id <chr>, sns_worked <dbl>,
    ## #   sat_hrs <dbl>, trt_workers <dbl>, trt_manager <dbl>, cmf_manager <dbl>,
    ## #   sat_work_overall <dbl>

## 4.3 Data key file (DUMMY — illustrative only)

Keeping the data key file well protected is essential because it is the
sole mechanism that can re-identify individuals in otherwise
de-identified research data, and its compromise can undermine
confidentiality protections and cause harm to participants. In the UBC
environment, the key file must be stored separately from research data
on UBC-approved secure systems, with access restricted to authorized
personnel only and never stored on personal devices or unapproved cloud
services.

Here is an example of a data key file for the work described above; this
is a **dummy file provided for illustrative purposes only**, and in
real-world research settings, such files must never be shared on public
systems.

**File path:** data\_key\_file/WorkerSatisfaction\_data\_key\_DUMMY.xlsx
— **one sheet** (`data_key`) with all mappings in a single table:

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr>
<th>Column</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>variable</code></td>
<td>Which field was de-identified (<code>worker_id</code>,
<code>email_id</code>, <code>city</code>, …)</td>
</tr>
<tr>
<td><code>original_value</code></td>
<td>Value in the raw file (or pooled city label before final code)</td>
</tr>
<tr>
<td><code>deid_code</code></td>
<td>Code used in the de-identified file</td>
</tr>
<tr>
<td><code>notes</code></td>
<td>Optional step label (e.g. rare-city pooling)</td>
</tr>
</tbody>
</table>

To **restore** a de-identified file: for each `variable`, join
`deid_code` in the de-identified data back to `original_value` using
this table (never merge the key into the shareable dataset).

The key holds **mappings for all de-identified identifiers**. It must
never be stored or shared alongside the de-identified dataset.

    worker_key <- raw |>
      distinct(worker_id) |>
      arrange(worker_id) |>
      transmute(
        original_value = worker_id,
        deid_code = paste0("Worker_", sprintf("%03d", row_number()))
      )

    email_key <- raw |>
      distinct(email_id) |>
      arrange(email_id) |>
      transmute(
        original_value = email_id,
        deid_code = paste0("Email_", sprintf("%03d", row_number()))
      )

    username_key <- raw |>
      distinct(username_id) |>
      arrange(username_id) |>
      transmute(
        original_value = username_id,
        deid_code = paste0("Username_", sprintf("%03d", row_number()))
      )

    owner_key <- raw |>
      distinct(owner_id) |>
      arrange(owner_id) |>
      transmute(
        original_value = owner_id,
        deid_code = paste0("Owner_", sprintf("%02d", row_number()))
      )

    orchard_key <- raw |>
      distinct(orchard_id) |>
      arrange(orchard_id) |>
      transmute(
        original_value = orchard_id,
        deid_code = paste0("Orchard_", sprintf("%02d", row_number()))
      )

    city_key <- step4 |>
      distinct(city) |>
      arrange(city) |>
      transmute(
        original_value = city,
        deid_code = paste0("City_", sprintf("%02d", row_number()))
      )

    if (length(rare_cities) > 0) {
      rare_city_key <- data.frame(
        original_value = rare_cities,
        deid_code = "Other BC community",
        notes          = "city pooled (k-anonymity) before City_XX codes"
      )
    } else {
      rare_city_key <- data.frame(
        original_value = character(0),
        deid_code = character(0),
        notes          = character(0)
      )
    }

    # One table: stack every mapping for simple lookup and restore
    data_key <- bind_rows(
      worker_key   |> mutate(variable = "worker_id",   notes = NA_character_),
      email_key    |> mutate(variable = "email_id",    notes = NA_character_),
      username_key |> mutate(variable = "username_id", notes = NA_character_),
      owner_key    |> mutate(variable = "owner_id",    notes = NA_character_),
      orchard_key  |> mutate(variable = "orchard_id",  notes = NA_character_),
      rare_city_key |> mutate(variable = "city"),
      city_key     |> mutate(variable = "city", notes = "final city code after pooling")
    ) |>
      select(variable, original_value, deid_code, notes) |>
      arrange(variable, original_value)

    cat("Data key preview (first 10 rows):\n")

    ## Data key preview (first 10 rows):

    head(data_key, 10)

    ## # A tibble: 10 x 4
    ##    variable original_value deid_code notes                        
    ##    <chr>    <chr>          <chr>     <chr>                        
    ##  1 city     Cobble Hill    City_01   final city code after pooling
    ##  2 city     Kelowna        City_02   final city code after pooling
    ##  3 city     Keremeos       City_03   final city code after pooling
    ##  4 city     Naramata       City_04   final city code after pooling
    ##  5 city     Oliver         City_05   final city code after pooling
    ##  6 city     Osoyoos        City_06   final city code after pooling
    ##  7 city     Peachland      City_07   final city code after pooling
    ##  8 city     Penticton      City_08   final city code after pooling
    ##  9 city     Summerland     City_09   final city code after pooling
    ## 10 city     Vernon         City_10   final city code after pooling

    cat("\nRows by variable:\n")

    ## 
    ## Rows by variable:

    data_key |> count(variable)

    ## # A tibble: 6 x 2
    ##   variable        n
    ##   <chr>       <int>
    ## 1 city           12
    ## 2 email_id      300
    ## 3 orchard_id     12
    ## 4 owner_id       12
    ## 5 username_id   265
    ## 6 worker_id     300

    dir.create(KEY_DIR, showWarnings = FALSE)

    write_xlsx(list(data_key = data_key), KEY_FILE)

    cat("Data key exported:", KEY_FILE, "\n")

    ## Data key exported: data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx

    cat("Single sheet: data_key (", nrow(data_key), " mapping rows )\n", sep = "")

    ## Single sheet: data_key (901 mapping rows )

    cat("Store separately from", OUTPUT_FILE, "— never on public systems.\n")

    ## Store separately from WorkerSatisfaction_300rows_deidentified.xlsx <U+2014> never on public systems.

------------------------------------------------------------------------

# Closing Summary

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr>
<th>Stage</th>
<th>What changed</th>
</tr>
</thead>
<tbody>
<tr>
<td>Direct identifiers</td>
<td><code>worker_id</code>, <code>email_id</code>,
<code>username_id</code>, <code>owner_id</code> → de-identification
codes</td>
</tr>
<tr>
<td>External sources</td>
<td>Removed <code>comments</code></td>
</tr>
<tr>
<td>Dates</td>
<td><code>age</code> (DOB) → <code>age_band</code> (5-year groups)</td>
</tr>
<tr>
<td>Geography</td>
<td>Rare cities pooled; all cities → <code>City_01</code> …</td>
</tr>
<tr>
<td>Quasi-identifiers</td>
<td><code>orchard_id</code> → <code>Orchard_01</code> …; all mappings in
data_key_file/WorkerSatisfaction_data_key_DUMMY.xlsx (dummy, separate
storage)</td>
</tr>
</tbody>
</table>

The de-identified dataset keeps all satisfaction and treatment ratings
for analysis while substantially lowering re-identification risk. **The
data key is highly sensitive** — it links de-identification codes back
to real names, emails, and locations. Protect and store it separately.



