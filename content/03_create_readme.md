---
layout: default
title: Create a README File
nav_order: 6
---

<img src="figures/work-in-progress.png" width="600"/>

**Please note this workshop is under revision. The README sample and template may be incorrect or unavailable.** 
{: .note}

# What is a README?
{: .no_toc}

A README file is an important document that accompanies your dataset. It provides key information about your project to make sure the dataset(s) can be correctly understood, reanalyzed, and reused by you and others. Without a README file, you could spend hours combing through related manuscripts or searching online to decipher file contents, analysis procedures, and acronyms.

It's good practice to have this document when conducting your research because it helps maximize the usability of your data in the long-term. You may also notice that many data repositories, including UBC’s, will ask you to include a README file as part of your data deposit. 

However, keep in mind that a README file complements your dataset. It does not replace the metadata that data repositories (e.g. Borealis or FRDR) ask you to provide when you deposit your data. The repository’s metadata will support findability within and between data repositories, while the README is portable and continues to describe the dataset, even after it has been separated from its original context. 

- Looking for a cheat sheet? Check out our <a href="https://osf.io/aqxw3" target="_blank">one-pager</a>
- Looking for a template to reuse? Check out our <a href="https://ubc-library-rc.github.io/rdm/content/exercise_files/README_template_v02.txt" target="_blank">README template</a> 
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
<p style="margin-bottom: 20px"></p>

## Warm-Up: Exercise 1
{: .no_toc}
{: .label .label-green }

Let's start by looking at a dataset deposited in Borealis. Please navigate to this dataset by clicking on the hyperlinked DOI and then scroll to view the deposited content under the "Files" tab.

Here is the dataset:
>Davis, Matthew, 2024, "Soil Adsorption Curves and Environmental Soil Data", <a href="https://doi.org/10.5683/SP3/JGRIN0" target="_blank">https://doi.org/10.5683/SP3/JGRIN0</a>, Borealis, V1

Once you’ve looked through the files included in the dataset, try to answer these questions:
1. If you received new soil data from Corktown, how would you create a new model and plot?
2. If you wanted to replicate this project, what software package(s) would be required to run the exact data analyses?
3. If you had questions about this project, who could we contact and how?


**The main takeaway here is that data without information about it (contained in a README file) is not useful to us!**

<img src="figures/person_thinking.png" width="150" style="margin-left:30px"/>

---

## Creation considerations for a README file
Create your README file at the start of your project, or at least before your project is shared and becomes publicly accessible. Typically, making one README file is enough for a dataset or a set of files with similar content. However, if multiple READMEs are needed, then you should format them the same way to maintain consistency. 
- As soon as possible, update your README file to reflect any changes made to your research project so you don't lose any important information

Any text editor can be used to create a README file. Commonly used formats are Markdown and TXT because of their lightweight formatting. These plain text formats also don’t rely on proprietary software, which means that they are more durable in the long-run, help with preserving your information better, and can be opened by various applications. R Markdown (common in R projects) and reStructuredText (common in Python projects) are also other common formats of README files.

Once your README file is created, store it in the root directory of your project folder (here is our workshop on [directory structures](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)), so that it will be the first file seen and easily accessible. 


## Stylistic considerations for a README file
How your README is written is also important. Consider some of these best practices for data documentation: 
- Be as clear and specific as possible when describing elements of your project
- Use descriptive titles, including your README file itself along with other subsections within your README file
- Add in relevant dates, such as when the README file, dataset(s), and other files were created and updated. These dates should follow a standardized format, like [ISO 8601](https://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DD or YYYYMMDD) to maintain consistency
- Consider your audience: will you be using jargon? If so, perhaps you may want to clarify the specialized terminology or look for an alternative word. If you refer to acronyms or abbreviations, make sure you’re defining them
- You could also enhance research transparency by addressing any research limitations (such as missing data), file quantities, and file versions
- The README file can simply be named ```README``` or ```_README```, but additional information can be added if necessary


## Minimum README file requirements  
Although every research project is different, a README file should at least include the 9 elements outlined in the table below, which will help users understand the basic details of your dataset(s) and evaluate the level of relevance to them.

These minimum requirements mirror the report by the Digital Research Alliance of Canada's Borealis Expert Group: [README Elements for Research Data Deposits in Borealis](https://doi.org/10.5683/SP3/CJ5X5O), along with additional elements to consider for possible README file enhancement. These elements also align with the Tri-Agency's language from an FAQ on [data retention, deposit, and availability (see question #17)](https://science.gc.ca/site/science/en/interagency-research-funding/policies-and-guidelines/research-data-management/faq-data-retention-deposit-and-availability). 

| **README metadata element** | **Definition** |
|---|---|
| **Author/creator** | The person(s), corporate body(ies), or agency(ies) responsible for creating the dataset. List authors in the order they should appear in citations. Where possible, include [ORCIDs](https://info.orcid.org/researchers/) to uniquely identify researchers and support proper attribution. |
| **Title** | The full, descriptive title by which the dataset is known. The title should clearly convey the subject matter and scope of the data so a reader can assess its relevance without opening any files. |
| **Description/summary** | A narrative summary of the dataset's purpose, content, and scope. Describe why the data were collected, what is captured, how the data are structured, and what they might be used for. Write for a broad academic audience so that researchers unfamiliar with the project can determine whether the data suit their needs. |
| **Contact information** | The name, institutional affiliation, and email address of the person(s) responsible for answering questions about the dataset. If the primary contact may change over time, consider also providing an institutional or project-level address so users can always reach someone knowledgeable about the data. |
| **License information** | The legal terms under which the dataset may be used, shared, and redistributed. Provide the full license name and version (e.g., [Creative Commons Attribution 4.0 International, CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)). If a standard open license does not apply, describe any restrictions on use, sharing, or derivative works. | 
| **DOI/persistent identifier** | A [Digital Object Identifier (DOI)](https://www.doi.org/the-identifier/what-is-a-doi/) or other persistent identifier assigned to the dataset, ensuring it can be reliably located and cited over time. If a DOI is not yet assigned at deposit, note it as pending and update the README once available. |
| **Research methodology** | A summary of the research methods used to generate the dataset, covering study design (e.g., experimental, observational, survey-based, or computational), data collection instruments or procedures, and key processing steps applied to the raw data. The goal is to provide users with sufficient context to assess the data's reliability and understand what would be required to replicate the data. |
| **Related publications** | Journal articles, reports, or other scholarly works that are directly based on or make use of this dataset. Provide full citations with DOIs where available. This helps users understand how the data have been analyzed, identifies methodological context, and ensures the researchers who generated the data receive appropriate credit and citations. |
| **Software/tools used** | The names and versions of any software, programming languages, or specialized tools needed to open, read, or reproduce the dataset or its analyses (e.g., R 4.3.1, Python 3.11, MATLAB R2023b). Include the operating system where relevant. This information is essential to reproducibility and helps users determine whether they can work with the data using the tools available to them. |

## Exercise 2
{: .no_toc}
{: .label .label-green }

Let's revisit the dataset cited in the warm-up exercise. Recall how difficult it was to understand the dataset, so we created an unofficial README for it to help understand the dataset better. 

Let's open the [example here](https://ubc-library-rc.github.io/rdm/content/exercise_files/README_sample_exercise_v01.txt), view the content, and answer the following questions:
1. What existing elements are useful to us?
2. What elements are underdeveloped or missing?
3. If you wanted to enhance this README file, what would you add?

## Sample README file
Here is a more thorough sample README file for the dataset cited in the warm-up exercise. It includes the 9 minimum elements to capture academic research projects. 

You can view and download the [sample README file here](https://ubc-library-rc.github.io/rdm/content/exercise_files/README_sample_v02.txt). In the note box at the top, you can also download a README template that can be filled in and modified to fit your project. Both of these files are in plain text format and can be opened in many applications. 

*Please note that the content of the example README file was fabricated for educational purposes and does not reflect the real project’s objectives.*

<img src="figures/readme.png" width="200" style="margin-left:30px"/>

<br>

<b>Here is a breakdown of what we covered:</b> 
READMEs are important documents containing information about your project's data. They help ensure your data is correctly interpreted and navigated for you and others in the future when revisited. READMEs should be created at the start of your project and maintained throughout, and include content that is appropriate to your project. Lastly, it's best to write your README in a non-proprietary format, like TXT or Markdown. 
{: .note}

# Congrats!
{: .no_toc }
*Hooray!* You are now ready to write up a good README file so you and other researchers can understand your project with no problems.
<br>

---


### Sources
{: .no_toc }
- Barsky, E., Cevik, Z., Cooper, A., Eber, A., Hu, B., Lui, L. H., & Pratt, I. (2026). README for research data deposits in Borealis: minimum and enhanced metadata elements (Version V1) [dataset]. Borealis. [https://doi.org/10.5683/SP3/CJ5X5O](https://doi.org/10.5683/SP3/CJ5X5O) 
- Cornell Data Services. Writing READMEs for Research Data. <https://data.research.cornell.edu/data-management/sharing/readme/>
- Government of Canada - Research Data Management. FAQ: Data retention, deposit, and availability. [https://science.gc.ca/site/science/en/interagency-research-funding/policies-and-guidelines/research-data-management/faq-data-retention-deposit-and-availability](https://science.gc.ca/site/science/en/interagency-research-funding/policies-and-guidelines/research-data-management/faq-data-retention-deposit-and-availability)
- Harvard Biomedical Data Management. README Files. <https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/readme-files>
- Princeton Research Data Service. READMEs for Research Data. <https://bit.ly/4lv23t3>
- The Geneva Graduate Institute. README.txt. <https://libguides.graduateinstitute.ch/rdm/readme>
- UBC Library. Research Data Management Data Guide. <https://bit.ly/3HtrzM8>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
