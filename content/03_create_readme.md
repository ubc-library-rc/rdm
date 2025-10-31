---
layout: default
title: Create a README File
nav_order: 6
---
# What is a README?
{: .no_toc}

A README file provides information about a project and helps ensure that data can be correctly interpreted by you and others when sharing or publishing datasets. It contains information commonly required to understand the dataset, its contents, provenance, licensing and how to interact with it. This helps maximize your dataset's usability and long-term preservation potential. A README file is generally named ```README``` and is typically a text or markdown file.

In short, a README file is a simple text document that accompanies your dataset, serving as a quick start guide that summarizes the essential information another researcher might need to understand, reanalyze, or repurpose your data. Without this context, readers could spend hours combing through related manuscripts or searching online to decipher file contents and acronyms.
<p style="margin-bottom: 20px"></p>

- Looking for a cheat sheet? Check out our <a href="https://osf.io/aqxw3" target="_blank">one-pager</a>
- Looking for a template to reuse? Check out our <a href="https://ubc-library-rc.github.io/rdm/content/assets/templates/UBC_README.txt" target="_blank">README template</a> 
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

Let's access this dataset:
>Davis, Matthew, 2024, "Soil Adsorption Curves and Environmental Soil Data", <a href="https://doi.org/10.5683/SP3/JGRIN0" target="_blank">https://doi.org/10.5683/SP3/JGRIN0</a>, Borealis, V1

Take a look at the project and try to answer the following:

1. You got new data for ammonia absorption into soil from Corktown, how would you go about generating the new model and plot? 
2. You want to recreate the whole project, what package(s) do you need to have installed to rerun everything?
3. You have a question about this project, who and how can we reach the corresponding author?

<p style="margin-bottom: 20px"></p>

<img src="figures/person_thinking.png" width="200" style="margin-left:30px"/>

[//]: # (activity link: https://bit.ly/rdmactivity)

---

## The Process of Creating a README

Consider creating a README file at the start of your project, or at least preparing a README before your project goes public, and continually updating it so you don't lose any details. One README file can be made for a dataset or a set of files that are of the same or similar formatting. If multiple READMEs are necessary, format them the same to maintain consistency. 

Place the README at the root directory of the project (check out our workshop on [directory structures](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)) so it can be one of the first files people will look at. 

You can use any text editor to create a README. [Markdown](https://ubc-library-rc.github.io/Introduction-to-Markdown/) or TXT formats are commonly used because you can add lightweight formatting, and it is non-proprietary. Using a plain text format helps preserve your information because it relies on durable, open standards rather than proprietary formats.  

Some other common formats you might see are R Markdown (common in R projects) and reStructuredText (common in Python projects).

<p style="margin-bottom: 20px"></p>

## Stylistic Considerations of a README

How you write your README is as important as the information you include. You should be as clear as possible. 

Here are some best practices for data documentation you may consider:
* Be as clear and specific as possible, including descriptive titles
* Don't use jargon
* Define terms, acronyms, and/or abbreviations
* Address any limitations
* Address any quantities, multiples, versions, and/or updates

## Recommended Content
  
Every project is different, so consider which of the following applies to your project. <b>For example</b>, a software project will have different sections than an academic research project.

| **Element** | **Details** |
|-------------|-------------|
| **Information** | Include at least two contacts. This could be the principal investigator and a co-investigator or another author. Include names, associated institutions, institution emails, and ORCIDs if available. |
| **Description** | Provide detailed context as much as possible – indicate what your project does and what your dataset contains. Give your README a descriptive title and include any dates that may be helpful, such as creation (both README and dataset), updates, data collection, etc. Using a standard date format, like [ISO 8601](http://www.w3.org/TR/NOTE-datetime) (YYYY-MM-DD or YYYYMMDD), is a good practice. |
| **Methodology** | Provide information about your research protocols such as data collection, data processing and analysis, sampling, instruments, tools, and software (include version and any special requirements for installation and operation), other sources used, geographic information of data collection, any standards followed, etc. |
| **Data and File Overview** | Describe the file structure of the dataset, such as the files or folders applicable for dataset organization and the relationship between the files. You should also indicate any other file relationships, such as if there are multiples, different versions, or modifications, and explain why if necessary. |
| **Data-Specific Information** | Define and describe any labels, codes, variables, abbreviations, and/or acronyms. Also, mention if any special formats are applicable. This can be repeated and modified for each dataset when appropriate. |
| **Sharing and Access Information** | Indicate the appropriate licences for your project. Also mention any restrictions, permissions, and/or data confidentiality conditions. You may also wish to include relevant links to other supporting datasets, locations where to access the dataset, or publications that cite or use the dataset. |
| **Acknowledgements** | Acknowledge your research team members, assistants, staff, and students who also had a contributive role in your project. Also include information on the funding support for your project, such as the name of the organization, grant name and number, fellowship name, awards, etc. |


<p style="margin-bottom: 20px"></p>

## Sample README 

<a href="https://ubc-library-rc.github.io/rdm/content/exercise_files/README_template.txt" target="_blank"> Download this sample README </a>. 

We created an example of a README for the project we looked at earlier in the warm-up exercise. This sample file was designed to capture academic research projects. There are other samples available for other types of projects (software, data science, etc.). 

**NOTE: The contents in the example template are <u>made up</u> for educational purposes, and do not reflect what the real study had in mind.**

## Exercise 2
{: .no_toc}
{: .label .label-green }

Now, let's practice what we just learned. 

From the sample template, what are some things that you noticed that may be specific to academic research? What are some things you would include if this were a software project? 

<img src="figures/readme.png" width="300" style="margin-left:30px"/>

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
- Cornell Data Services. Writing READMEs for Research Data. <https://data.research.cornell.edu/data-management/sharing/readme/>
- Harvard Biomedical Data Management. README Files. <https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/readme-files>
- Princeton Research Data Service. READMEs for Research Data. <https://bit.ly/4lv23t3>
- The Geneva Graduate Institute. README.txt. <https://libguides.graduateinstitute.ch/rdm/readme>
- UBC Library. Research Data Management Data Guide. <https://bit.ly/3HtrzM8>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
