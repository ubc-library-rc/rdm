---
layout: default
title: Create a Data Dictionary
nav_order: 12
---

# What is a Data Dictionary? 
{: .no_toc }

A data dictionary is a type of documentation that provides essential information about variables in a dataset, including their definitions, descriptions, and structure. The primary goal of a data dictionary is to help people understand and use a dataset, especially if you are working with multiple tables or with a database. A data dictionary may be included with the dataset or exist as an independent resource. 

Having a data dictionary is important for research reproducibility and revisitation. It clarifies questions like, "What does this variable mean?"

- Looking for a cheat sheet? Check out our <a href="https://osf.io/akzpq" target="_blank">one-pager</a>
- Looking for a template to reuse? Check out our <a href="https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_template_blank.csv" target="_blank">data dictionary template</a> 
{: .note}

<details open markdown="block">
 <summary>
   Table of Contents
 </summary>
 {: .text-delta }
- TOC
{:toc}
</details>

---

## Warm-Up
{: .no_toc}
{: .label .label-green }

It's common for long-standing research projects to have a data dictionary. Here are some open-source examples to explore:

* [National Database of Deep-Sea Corals](https://www.ncei.noaa.gov/waf/dsc-data/metadata/20221213-0_NOAA_NDB_corals_sponges_data_dictionary.html)
* [Climate and Forecast Conventions](http://cfconventions.org/Data/cf-standard-names/46/build/cf-standard-name-table.html)
* [Organic Carbon Sorption and Decomposition in Selected Global Soils](https://tes-sfa.ornl.gov/sites/default/files/Soil_C_Decomp_Data_Dictionary_20140616.pdf)
* [Planetary Science Dictionary (NASA)](https://pds.nasa.gov/tools/dd-search/)

A data dictionary can be a simple table (spreadsheet or PDF) or a detailed web application. For some projects, a data dictionary is created and maintained by one research member, but this can also be done by the entire research team. 

<p style="margin-bottom: 30px"></p> 

## Exercise 1
{: .no_toc}
{: .label .label-green }

Please help us make sense of the dataset below.

Access this dataset:  

>Florida, Richard, 2013, "Class-Divided Cities, Detroit Edition Published in Atlantic Cities", <a href="https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/SNXXHQ" target="_blank">https://doi.org/10.5683/SP3/SNXXHQ</a>, Borealis, V3

Download the data file <b>"Detroit Class Data.xlsx"</b> in the <b>Original File Format</b>. While examining the data, try to answer the following questions:
1. What do you think the columns `STATEFP10` and `COUNTYFP10` mean?
2. Describe the different measures in this study.
3. How was the data collected?

Alternatively, here is another dataset example with a better data dictionary:
>Barsky, Eugene; Mitchell, Marjorie; Buhler, Jeremy, 2019, "UBC Research Data Management Survey: Science and Engineering", [https://doi.org/10.5683/SP2/9VEAT9](https://doi.org/10.5683/SP2/9VEAT9), Borealis, V3

You can see how a data dictionary allows users to make sense of the data very fast.

<img src="figures/data_dictionary.png" width="200"/>

---

# The Process of Creating a Data Dictionary 

Document your work as you go, such as making updates when new elements and variables are added or updated. This reduces the risk of forgetting valuable information or losing details. 

Place the data dictionary where your data files are stored. Having the data dictionary nearby makes it easier to understand the data, as it serves as a guide to its contents. Check out our [directory structures](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html#stylistic-considerations-of-a-readme) workshop for more information. 

A data dictionary can be created with any text editor or word processor, but we suggest using spreadsheet software. The spreadsheet should be saved as a CSV or TSV file because it's a lightweight, non-proprietary file format that's accessible to everyone and future-friendly. 

<p style="margin-bottom: 30px"></p> 

# Stylistic Considerations of a Data Dictionary

How you write your data dictionary is as important as the information you include. To ensure consistency, follow the style that's agreed upon by the research team. Also, make sure to note any stylistic decisions in your [README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html#stylistic-considerations-of-a-readme) if necessary. 

The following are some general best practices related to data documentation:
* Be as clear as possible
* Don't use jargon 
* Define terms, abbreviations, and acronyms 
* Follow [good naming conventions](https://ubc-library-rc.github.io/rdm/content/01_file_naming.html#1--machine-readable) and a consistent formatting style

A data dictionary is usually formatted as a table with the variables in rows and variable information in columns. At the top, you should mention relevant metadata such as the dataset's name, the creation date of the data dictionary, and the version number or last updated date. 

<p style="margin-bottom: 30px"></p> 

# Recommended Content 

Every project is different, so consider which of the following applies to your project.

Primary fields to consider:

| **Field** | **Details** |
|-----------|-------------|
| **Variable ID** | The name used to identify a specific variable. This can be a sequence of alphanumeric characters. |
| **Variable Name** | The name of a specific variable in a human language, like English. Don’t include abbreviations or acronyms. |
| **Variable Definition** | The explanation of what a variable means, how it was calculated, how it should be used, or any known patterns. You can refer to existing discipline-specific vocabularies to increase interoperability (e.g. [Unified Medical Language System](https://www.nlm.nih.gov/research/umls/index.html)). |
| **Variable Type** | The format of a variable (e.g., string, number, percentage, date). |
| **Allowable Values / Parameters** | Describe the values that can be entered. For example: min/max values for numerical entries, a list of options for character values, or whether the field accepts nulls. |
| **Requirement** | Indicate if a variable is required with a "yes" or "no". |
| **Notes** | Add any extra notes, remarks, or instructions that help contextualize a variable. |

Secondary fields to consider:

| **Field** | **Details** |
|-----------|-------------|
| **Example Usage/Sample Values** | Provide some examples of how a variable is implemented, or what a variable may look like. |
| **Measurement Units** | The measurement unit of a variable. |
| **Question Text** | Include the exact wording from the survey, interview, task, etc. |
| **Timestamp** | The indicated time a variable’s data was collected. |
| **Missing Data** | Describe the missing data for a specific variable. Indicate the type of missing data, such as the system missing the data, a data instrument error, or a participant skip error, etc. |

<p style="margin-bottom: 30px"></p> 

# Sample Data Dictionary 

Below is a shortened data dictionary for the dataset we looked at in exercise 1. 

You can download a sample data dictionary based on exercise 1 [here](https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_sample.csv). The fields and existing values can be deleted and modified to fit your project.  

**NOTE: The values here are <u>made-up examples</u> for educational purposes. They do not reflect the real study.**

| Variable ID | Variable Name | Variable Definition | Variable Type | Allowable Values/Parameters | Requirement | Sample Values | Notes | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| STATEFP10 | State code | The unique numeric code for the state. More information on state codes can be found [here](https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971). | String | Numerical values of 01-50 allowed | Yes | “01”, “02”, “06” | | 
| COUNTYFP10 | County code | The unique numeric code for the county. More information on county codes can be found [here](https://www2.census.gov/programs-surveys/decennial/2010/partners/pdf/FIPS_StateCounty_Code.pdf). | String | Numerical values of 001-110 allowed | Yes | “001”, “003”, “005” | | 
| GEOID10 | Geographical ID | Combined state, county, and tract identifier. | String | Numerical and alphabetical values allowed | Yes | “26163593300” | | 
| FFFPCT | Fast Food Percentage | Percentage of restaurants classified as fast food. | Number | Percentages from 0-100 allowed with one decimal place | Yes| 40.3, 55.8, 22.5 | | 

<p style="margin-bottom: 20px"></p> 

## Data Dictionary Template

You can download a blank data dictionary template [here](https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_template_blank.csv). The header and fields can be modified to fit your project. 

<br> 

<b>Here is a breakdown of what we covered:</b> A data dictionary is an informative document about the dataset's variables, content, structure, and other details needed for understanding and reproducing the research. Remember to have a consistent and clear style, and record any updates made. Aim to make your data dictionary accessible to others and for the future by saving it in a non-proprietary format.
{: .note}

# Congrats!
{: .no_toc }

*Hooray!* You can now create a data dictionary so you and other researchers can understand the dataset with no problems!
<br>

---

<b>Sources</b>
{: .no_toc }
* Harvard Biomedical Data Management. Data Dictionary. <https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/data-dictionary> 
* Penn Libraries Guides. Data Management Resources. <https://guides.library.upenn.edu/c.php?g=564157&p=9554907>
* Phegley, L. (2023). University of Pennsylvania. Data Dictionary Blank Template. <https://repository.upenn.edu/entities/publication/0430ccdd-cbd8-4404-9f54-11cb81d5b3b1>
* Stony Brook University Data Governance. Data Dictionary Standards. <https://www.stonybrook.edu/commcms/datagovernance/structureandroles/datadictionarystandards>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
