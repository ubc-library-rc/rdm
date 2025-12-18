---
layout: default
title: Introduction to Data Anonymization
parent: Data Anonymization
nav_order: 1
---

<img src="figures/work-in-progress.png" width="600"/>

# Introduction to Data Anonymization
{: .no_toc}
Although it is good practice to share our research data and findings, we need to consider precautions when conducting ethical, reliable, and responsible research. 
Sensitive data requires careful handling and security to protect participant privacy and confidentiality and to comply with ethical and legal requirements. Leaked sensitive data poses major harm and risks, such as revealing identities, which negatively affect the interests of people, communities, and/or animals involved in the research.

### Terminology
{: .no_toc}
In UBC terminology [(Information Technology Standard U1)](https://cio.ubc.ca/information-security-standards/U1), sensitive data is classified as medium risk, high risk, or very high risk. For the purposes of this workshop, however, we will use the term “sensitive data” to align with the terminology in Sensitive Data: Practical and Theoretical Considerations (Rod & Thompson, 2023). In this context, these terms will be treated as equivalent. 
{: .note}

Looking for a cheat sheet? Check out our one-pager (TBD)
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

# What is sensitive data?
Sensitive data is “information that must be safeguarded against unwarranted access or disclosure” (Rod & Thompson, 2023) and may relate to both humans and animals.

Examples of data that are considered “sensitive”:
* Personal health information
* Some kinds of geographical information, like the locations of endangered species
* Data protected by institutional policy

## Why do we anonymize data?
Data is anonymized to minimize the risk of harm to individuals, communities, and animal species in the event of a confidentiality breach. Data anonymization is also done to prevent possible re-identification, where participants could be isolated in a dataset and then matched to other information that could identify them with reasonable effort.  The level of harm that may impact participants depends on the population, topic, and context of the data.

Examples of who may be harmed:
* Vulnerable populations
  - Racialized communities
  - Indigenous communities
  - Politically oppressed communities
  - Lower-income groups
  - Children and teens
* Participants with experiences of socially sensitive topics (of a Western lens)
  - Drugs (including cigarettes) and alcohol use
  - Details of sexual activity and/or STD status
  - Private family issues
  - Relationship/domestic violence
  - Loss or death in the family
  - Victimization status
  - Criminal/delinquent behaviour
  - Health-related questions, medical conditions, and mental health questions
 
## What makes data "sensitive"?
Within a dataset, there are different kinds of identifying pieces of information that may be included in a dataset: direct identifiers, indirect identifiers, non-identifiers, and hidden identifiers. These kinds of identifiers can immediately identify a participant or can identify them when combined with other identifiers.

### Direct identifiers
{: .no_toc}
Direct identifiers are pieces of information that will immediately re-identify a participant. This type of information <b>must</b> be removed from any published dataset. You also want to consider removing direct identifiers when sharing data within the research group. 

Here are 15 direct identifiers compiled by Rod & Thompson (2023) in their textbook chapter:
* Full or partial names or initials
* Dates linked to individuals, such as birth, graduation, or hospitalization (year alone or month alone may be acceptable)
* Full or partial addresses (large units of geography, such as city, fall under indirect identifiers and need to be reviewed)
* Full or partial postal codes (the first three digits may be acceptable)
* Telephone or fax numbers
* Email addresses
* Web or social media identifiers or usernames
* Web or internet protocol numbers, precise browser and operating system information (these may be collected by some types of survey software or web forms)
* Vehicle identifiers, such as license plates
* Identifiers linked to medical or other devices
* Any other identifying numbers directly or indirectly linked to individuals, such as social insurance numbers, student numbers or pet ID numbers
* Photographs or individuals or their houses or locations, or video recordings containing these; medical images or scans
* Audio recordings of individuals
* Biometric data
* Any unique and recognizable characteristics of individuals (for example, a Canada research chair in Physics)

### Indirect identifiers ("quasi-identifiers")
{: .no_toc}
Indirect identifiers, or “quasi-identifiers”, are pieces of information that, when combined, could identify a participant. The removal of this kind of information should be evaluated in the context of what is known or may be reasonably inferred. For example:
* Likely to pose a high risk:
  - Variables containing groups with small numbers of respondents
  - Extreme values or unusual combinations of variables

Consider the size of the potentially-identifiable group(s) in the general population, and the contextual information that accompanies the data.

Here are some more examples of indirect identifiers:
* Participant surveys or interviews (who consented to have their information be used for research purposes)
* Medical records
* Disability
* Tax-filer records
* Social media
* Age (can be a direct identifier for the very elderly)
* Gender identity
* Income
* Occupation or industry
* Geographic variables
* Ethnic and immigration variables
* Membership in organizations or use of specific services 

### Non-identifiers
{: .no_toc}
Non-identifiers are pieces of information that likely won’t identify a participant. For example:
* Ratings on a Likert scale, rankings, and opinions
* Temporary measures, like a resting heart rate or the number of times you ate a meal in the last week

However, still consider the level of sensitivity of the data. A dataset with medical information about health behaviours should be handled more carefully than a dataset with potato chip flavour ratings. Similar to free text responses, comments, and transcribed interviews, which also need to be considered on a case-by-case basis.

### Hidden identifiers
{: .no_toc} 
Like indirect identifiers, hidden identifiers are when non-identifiers are contextually combined in some way that may re-identify participants. 

The size of the dataset also matters because machine learning can be applied to reveal patterns and potentially re-identify participants. For example, comparing public restaurant reviews to a dataset containing ratings of barbeque buffets can re-identify a participant with sufficient effort. 

## Exercise 1
{: .no_toc}
{: .label .label-green }
  
# Consent language

# Future use of data

# Assessing risk and anonymization: "k-anonymity" 

## Exercise 2
{: .no_toc}
{: .label .label-green }

# How to protect and preserve sensitive data?


<b>Here's a breakdown of what we covered:</b>








