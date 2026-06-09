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


