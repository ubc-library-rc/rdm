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

<img src="figures/document.png" width="200"/>

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

<img src="figures/documentation.png" width="250"/>

# Manual de-identification steps
You're a researcher looking into the production efficiencies of apple growers in the Pacific Northwest. Here is the [example dummy dataset](https://ubc-library-rc.github.io/rdm/content/exercise_files/WorkerSatisfaction_deIDsteps_KEY_workshop_v01.xlsx) for this workshop. 

This dataset was created for this workshop and doesn’t reflect a real study with real participants. We will be using this example dataset to illustrate the following manual de-identification procedures. 

Please note that most of the records of the example dataset have already been de-identified. However, the first record is not de-identified, so you can practice the manual de-identification methods by following the steps outlined below. 

**Step 1: Direct identifiers** 

Here, let’s first find the direct identifiers and select a method to remove them. We will use <u>pseudonymization</u>. For example, names will be replaced with “person1”, “person2”, and so on.  

Examples of direct identifiers:
  - Names, addresses, phone numbers, emails
  - Government ID number, IP addresses
  - Photos, biometric ID
 
| *Identifiable name* | *worker_id* |
|---------------------|-------------|
| James Strange | person1 |
| Maya Liya | person2 |
| Amelio Beal | person3 |

**Step 2: Dates**

Next, we’re going to identify and re-code specific dates in a way that will still allow data analysis. You should consider removing any dates that aren’t important for analysis. We will use <u>aggregation</u> for the “date of birth” variable. For example, 5-year age ranges will replace each birth date.

Examples of dates that could be linked to public records:
  - Specific days
  - Date of birth
  - Date of interview or treatment
 
| *Date of birth* | *age* |
|---|---|
| 1998-09-10 | 25-29 |
| 1994-08-04 | 30-34 |
| 1995-01-02 | 30-34 |

**Step 3: Geographic data**

Keep in mind that if geographical specificity is needed for analysis, then take extra precautions to protect other variables that may contribute to re-identification. For this step, we’re going to use <u>pseudonymization</u> again for the geographical variables. For example, orchard names will be replaced with “farm1”, “farm2”, “farm3”, and so on. 

Examples of geographical data:
  - Street address
  - Census tract
  - Postal code or zip code
  - Country
  - Area population of less than 100,000
 
| *Orchard name* | *orchard_id* |
|---|---|
| Applejacks | farm1 |
| Applejacks | farm1 |
| West Kelowna Apples | farm2 |

**Step 4: Data potentially linked to external sources**

Keep an eye out for (indirect) variables that could link to publicly accessible sources of data, like government registries or social media profiles. These kinds of data matched with geographical data could lead to re-identification. Here, we will use <u>anonymization</u> for the social media profiles included in the dataset. For example, for each record, we will remove the participant’s username from their social media profile.

Examples of indirect variables:
  - Social media profiles
  - A medical clinic matched with a business revenue database

| *LinkedIn username* | *Full anonymization* |
|---|---|
| james.strg |  |
| ML_9504 |  |
| beal_a |  |

**The finalized de-identified dataset**

Here is the final product after manually de-identifying the dataset. The dataset is sufficiently de-identified enough that it can be shared with research team members or external partners, for example. 

To assess the anonymity of this dataset, we can look at the overall k anonymity value, which is k=1. In real life, this k anonymity value would be <u>unacceptable</u>. This tells us that the dataset was not sufficiently de-identified and that participants are easily identifiable. Ideally in real life, a k anonymity value of 3 or 5 would be good. 

For this workshop, however, we will keep the k anonymity value of 1 because it’s only a dummy dataset and no real participants are involved. 

| *worker_id* | *orchard_id* | *age* |
|---|---|---|
| person1 | farm1 | 25-29 | 
| person2 | farm1 | 30-34 |
| person3 | farm2 | 30-34 |


## Alternative steps
Previously, we demonstrated one manual de-identification method for each step. However, other kinds of methods (mentioned at the beginning of this workshop) could be applied as well. 

For example:
- In step 1, anonymization can be applied to some direct identifiers, like emails. This means removing all data for the “email_id”.
- In step 2, generalization can be applied to the birth dates to only use the birth years. However, be aware of outliers.
- In step 3, anonymization can also be applied to the “city” variable, as the province could be enough for data analysis. This would look like removing all data for the “city” variable, leaving only data related to the province variable.
- In step 4, masking could be applied to the social media profiles, blurring out the participants’ social media usernames. This could be using asterisks in place of the usernames for each record. 

<img src="igures/risk_assessment.jpg" width="250"/>

<b>Here's a breakdown of what we covered:</b>
Participants’ private and identifiable information needs to be protected when sharing a dataset containing sensitive data. A sensitive dataset can be sufficiently de-identified using the manual de-identification methods outlined in this workshop, so it can be safely shared with your research team or other researchers. These methods include anonymization, pseudonymization, aggregation, masking, generalization, and local suppression. For each step of the de-identification process, select the method that is the most appropriate to address the sensitivity of the variable being de-identified. Also, remember to assess the anonymity of your finalized dataset to make sure it’s properly de-identified. 
{: .note}

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
