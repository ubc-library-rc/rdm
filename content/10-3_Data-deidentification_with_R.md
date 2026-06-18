---
layout: default
title: Programmatic Data De-identification with R
parent: De-identify Research Data
nav_order: 3
---

# Introduction to Data De-identification with R
{: .no_toc} 

In the previous workshop, we discussed manual de-identification methods for sensitive data. These efforts help ensure that a dataset can be shared safely with other researchers and protect participants’ identifying information. However, manually de-identifying a dataset may be laborious for large datasets, compared to smaller-scale datasets. In this case, using a tool or program can help speed up the de-identification process to save you some time and energy.

We will replicate workshop 2 by using R as an appropriate tool to help with the manual de-identification process. Please note that you will need to have R and RStudio available on your machine (jump ahead to [Part 1 - Setup before starting](https://ubc-library-rc.github.io/rdm/content/10-3_Data-deidentification_with_R.html#part-1--setup)).  
<details open markdown="block">
<summary>
  Table of contents
</summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

---

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
*Learning about different de-identification methods and demonstrating some of them on an example dataset.*

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

**As a reminder, please make sure you’re working with a duplicate/copy file of your data for this experiment and not with your original data file(s).** 

---

<div style="border: 1.5px solid #ddd; border-radius: 10px; padding: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
  <iframe src="exercise_files/data-deidentification-r-workshop/Workbook_WorkerSatisfaction_Deidentification.pdf" 
          width="100%" 
          height="600px" 
          style="border: none; border-radius: 6px;">
  </iframe>
  <p style="text-align:center; margin-top:8px;">
    <a href="exercise_files/data-deidentification-r-workshop/Workbook_WorkerSatisfaction_Deidentification.pdf">Open full workbook in new tab ↗</a>
  </p>
</div>

<div style="border: 1.5px solid #ddd; border-radius: 10px; padding: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
  <iframe src="exercise_files/data-deidentification-r-workshop/Workbook_WorkerSatisfaction_Deidentification.html" 
          width="100%" 
          height="600px" 
          style="border: none; border-radius: 6px;">
  </iframe>
  <p style="text-align:center; margin-top:8px;">
    <a href="exercise_files/data-deidentification-r-workshop/Workbook_WorkerSatisfaction_Deidentification.html" target="_blank" rel="noopener">
      Open full workbook in new tab ↗
    </a>
  </p>
</div>
