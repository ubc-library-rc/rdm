---
layout: default
title: AI-Assisted Data De-identification with Copilot for Microsoft 365
parent: De-identify Research Data
nav_order: 4
---

<img src="figures/work-in-progress.png" width="600"/>

We will be designing this workshop in Spring 2026. Please stay tuned...

# Introduction to AI-Assisted Data De-identification
{: .no_toc} 
With an increase of artificial intelligence (AI) tools, we’re curious to see and understand how well they perform as an assistant in the de-identification process of sensitive data. There is potential for ethically using an AI tool to help with this process (not to replace), especially for large amounts of data, but it has not been guaranteed yet. Please be aware that we aren’t recommending any specific AI tool or using AI as a robust and reliable process for data de-identification. In fact, our experiments showcased that AI is not ready yet to perform equally for the data de-identification tasks. The purpose of this workshop is to only experiment with an AI tool for this kind of task.

There is no promise that the Co-Pilot agent will work properly, such as encountering errors, inconsistencies, or Co-Pilot may suddenly cease activity. You may encounter the message, “Editing with Copilot is temporarily unavailable due to high demand. Try again later or turn off edits to keep chatting with Copilot.”

**Please consider these when using any kind of AI tool for research:**
- UBC Risk Management has a summary of what AI tools could be used for different purposes as approved by the PIA process. For this workshop, we will be using the Copilot M365 Embedded assistant in Microsoft 365 approved for up to high-risk data (not the Copilot M365 Chat which has been approved only to up to medium risk data).
- Additionally, note that:
  - There is a risk that Co-Pilot M365 Embedded assistant will make errors and not de-identify all identifiers
  - There is a risk that Co-Pilot M365 Embedded assistant will alter other data that shouldn’t be changed
  - Please ensure some quality assurance process after you use Co-Pilot M365 Embedded assistant for data de-identification
{: .warn}

As a reminder, please make sure you’re working with a duplicate/copy file of your data for this experiment and not with your original data file(s).

### Terminology 
{: .no_toc} 
UBC does not define the term “sensitive data”. Instead, UBC electronic information is classified using a schema outlined in UBC [Information Security Standard U1 (ISS-U1)](https://cio.ubc.ca/information-security-standards/U1). For the purposes of this workshop, however, we will use the term “sensitive data” to align with the terminology in Sensitive Data: Practical and Theoretical Considerations (Rod & Thompson, 2023). In this context, the term “sensitive data” will be treated as equivalent to information classified as “high risk” and “very-high risk” in UBC ISS-U1.
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

## Recap: Manual de-identification methods
In our second workshop, we introduced you to some common examples of manual de-identification methods for sensitive data. Have a look at the list below for a refresher on the types we discussed: 
- Anonymization: all identifying information is removed from the dataset and cannot be restored.
- Pseudonymization: identifying information is replaced with artificial identifiers, such as codes or numbers.
-	Aggregation: individual data points are grouped together into categories or ranges.
-	Masking: identifying information is hidden or obscured by using techniques, such as encryption, hashing, blurring, or noise addition.
-	Generalization: identifying information is replaced with more general or vague terms.
-	Local suppression: individual cases or responses (individual records) are deleted. 

## Recap: Manual de-identification steps 
