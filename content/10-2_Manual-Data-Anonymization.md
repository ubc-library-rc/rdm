---
layout: default
title: Manual Data De-identification
parent: De-identify Research Data
nav_order: 2
---

<img src="figures/work-in-progress.png" width="600"/>

# Introduction to Manual Data De-identification
{: .no_toc} 
If you want to share a dataset containing sensitive data among your research team members or with another researcher, there should be de-identification efforts to protect participants' personal information. Manual de-identification methods can be used to help prepare a dataset with sufficient de-identification so it can be shared among the research team or for researcher collaboration.

***Disclaimer***: Please note that this workshop offers a foundational introduction to manual data de-identification. It’s recommended to consult with your institutional or departmental privacy, legal, or compliance expert for assistance with data de-identification. 

### Terminology 
{: .no_toc} 
UBC does not define the term “sensitive data”. Instead, UBC electronic information is classified using a schema outlined in UBC [Information Security Standard U1 (ISS-U1)](https://cio.ubc.ca/information-security-standards/U1). For the purposes of this workshop, however, we will use the term “sensitive data” to align with the terminology in Sensitive Data: Practical and Theoretical Considerations (Rod & Thompson, 2023). In this context, the term “sensitive data” will be treated as equivalent to information classified as “high risk” and “very-high risk” in UBC ISS-U1.
{: .note}

Looking for a cheat sheet? Check out our two-pager (IN PROGRESS)
{: .note}

<details open markdown="block">
<summary>
  Table of contents
</summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

---

# Methods for manual de-identification
Examples include, but are not listed in any particular order:

**Anonymization:** all identifying information is removed from the dataset and cannot be restored.
- Advantage: ensures a high level of privacy protection
- Disadvantage: may reduce the usefulness and quality of data
- *When to use:* this method can be used when data of a variable isn’t necessary for data analysis, or when data de-identification and privacy policies require that data values be fully removed 

**Pseudonymization:** identifying information is replaced with artificial identifiers, such as codes or numbers.
- Advantage: allows data to be linked across different sources, datasets, or over time, which can be useful 
- Disadvantage: increases the risk of re-identification if the codes are exposed or compromised
- *When to use:* this method can be used when it’s necessary to keep data values distinct, but without having the unique identifying data

**Aggregation:** individual data points are grouped together into categories or ranges.
- Advantage: preserves some statistical properties and patterns
- Disadvantage: reduces the level of detail and variability in the data, and information could still be inferred
- *When to use:* this method can be used when individual record values aren’t necessary, and clumped data values (into categories or ranges) are still useful for analysis

**Masking:** identifying information is hidden or obscured by using techniques, such as encryption, hashing, blurring, or noise addition.
- Advantage: preserves the ability for data analyses
- Disadvantage: introduces errors or distortions in the data
- *When to use:* this method can be used when only concealing those pieces of identifying information is enough to achieve de-identification

**Generalization:** identifying information is replaced with more general or vague terms. For example, dates are replaced with years, addresses replaced with regions, and names replaced with initials.
- Advantage: preserves some semantic meaning and context
- Disadvantage: makes the data less specific and more ambiguous
- *When to use:* this method can be used when data can be made more general while still being useful or functional for analysis

**Local suppression:** individual cases or responses (individual records) are deleted.
- Advantage: like anonymization, privacy is protected
- Disadvantage: the quality of data decreases, which impacts its usefulness
- *When to use:* this method can be used when there are outlier records or when data anonymity and sensitivity assessments, like k anonymity, aren’t met

# Manual de-identification steps

## Alternative steps

<b>Here's a breakdown of what we covered:</b>

# Congrats!
{: .no_toc}
*Hooray!*
---
### Sources
{: .no_toc}
--- 

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
