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

Please consider these when using any kind of AI tool for research:
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
As a demonstration of some of the de-identification methods, we used a dummy dataset for a mock research project looking at production efficiencies of apple growers in the Pacific Northwest. Here are the steps we did:
-	Step 1: For direct identifiers, we applied pseudonymization by replacing participant names with “person1”, “person2”, and so on.
-	Step 2: For birth dates, we used aggregation to replace individual dates with 5-year age ranges. 
-	Step 3: For geographic data, we applied pseudonymization again by replacing orchard names with “farm1”, “farm2”, and so on.
-	Step 4: For data that may be linked to external sources and result in re-identification, we used anonymization by removing this data for the variables affected. 
-	After following these steps, we received a de-identified dataset and created a separate data key file that is safely stored with the research records.

We are now going to replicate our second workshop on manual de-identification methods using Co-Pilot, to see its capabilities in assisting with the de-identification process. Here is the same dummy dataset (INSERT DUMMY DATASET) for you to download and use for this workshop.

## Using the MS Co-Pilot embedded assistant to help with data de-identification
1) Navigate to MS Excel on your web browser to access Co-Pilot as an embedded assistant, not the desktop application because Co-Pilot is not available there. You may need to log in with your UBC CWL. 
2) In your toolbar, find and select the Co-Pilot icon. A new chat should open.
3) Near the text entry box, find and select the “options” icon to activate “Edit with Co-Pilot”. This will ensure Co-Pilot will make changes directly to your duplicate file and not generate a new file each time.

## Some prompting tips to note before proceeding
-	It’s always best to be as clear as possible when prompting Co-Pilot. This can include specifying which variables will be modified, what exactly will happen to them, and what they will be replaced with (if using pseudonymization, aggregation, masking, or generalization). For example, if you use anonymization, specify exactly that the task is to remove variable data. If not specified, Co-Pilot will randomly decide and apply another de-identification method, such as aggregation or local suppression. 
-	In your prompt, you should specify to place the de-identification results in a new sheet. If not, Co-Pilot will apply changes directly on the original sheet. You can also name the new sheets by prompting for and indicating what you want the sheet name to be.
-	To create a data key file for your original raw data, we found (by a lot of trial-and-error) that it’s best to finish all de-identification methods and then prompt for a data key file. You may run into issues, such as incorrect data key updates or, as you move along the de-identification process.


