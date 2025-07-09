---
layout: default
title: Create a Data Dictionary
nav_order: 12
---

# What is a Data Dictionary? 
{: .no_toc }

A data dictionary is a type of documentation that provides important information about the variables in the dataset, such as their definitions, descriptions, and structure. This is especially important if you are working with multiple tables or with a database. 

It's useful to have a data dictionary because it's a critical tool for research reproducibility and revisitation. The main goal of a data dictionary is to help people understand and use the dataset(s). It will help answer questions like, "What does this variable mean?" 


Looking for a cheat sheet? Check out our <a href="https://osf.io/akzpq" target="_blank">one-pager</a>
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

A data dictionary can be a simple table (spreadsheet or PDF) or a detailed web application. Some projects only need one data dictionary that can be created and maintained by a single person while others will require a whole team to create and maintain it. 


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

Alternatively, here is an example of another dataset with a better data dictionary:
>Barsky, Eugene; Mitchell, Marjorie; Buhler, Jeremy, 2019, "UBC Research Data Management Survey: Science and Engineering", [https://doi.org/10.5683/SP2/9VEAT9](https://doi.org/10.5683/SP2/9VEAT9), Borealis, V3

* You can see how a data dictionary allows users to make sense of the data very fast.
* Data dictionary can travel with the dataset or even serve as a stand-alone data item.

---

# The Process of Creating a Data Dictionary 

Document your work as you go, such as making updates when new elements and variables are added or updated. This reduces the risk of forgetting valuable information or losing details. 

Place the data dictionary where your data files are stored. Having the data dictionary nearby makes it easier to understand the data, as it serves as a guide to its contents. Check out our [directory structures](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html#stylistic-considerations-of-a-readme) workshop for more information. 

A data dictionary can be created with any text editor or word processor, but we suggest using spreadsheet software. The spreadsheet should be saved as a CSV or TSV file because it's a lightweight, non-proprietary file format that's accessible to everyone and future-friendly. 

# Stylistic Considerations of a Data Dictionary

How you write your data dictionary is as important as the information you include. To ensure consistency, follow the style that's agreed upon by the research team. Also make sure to note any stylistic decisions in your [README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html#stylistic-considerations-of-a-readme) if necessary. 

The following are some general best practices related to data documentation:
* Be as clear as possible
* Don't use jargon 
* Define terms, abbreviations, and acronyms 
* Keep the data dictionary where you [store your data](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)
* Follow [good naming conventions](https://ubc-library-rc.github.io/rdm/content/01_file_naming.html#1--machine-readable) and a consistent formatting style

# Recommended Content 

A data dictionary is usually formatted as a table with the variables in rows and variable information in columns. Every project is different, so consider which of the following applies to your project.

Key fields to consider:
* Name of the dataset(s)
* Variable: the name used to identify the field, can be alphanumeric
* Variable name: the human-intelligible name of the variable (such as English). Don't include abbreviations or acronyms
* Variable definition: an explanation of what the variable means
* Variable type: the format of the variable (e.g. string, number, percentage, etc.)
* Allowable values/parameters for the variable: a description of what data may be entered into a field. For numerical fields: minimum and maximum values. For character fields: allowable values
* Date created: the date the dictionary entry was created
* Date updated: the date the dictionary entry was modified
* Notes: any additional notes, remarks, or comments that contextualize the information conveyed in the variable or relay special instructions

Secondary fields to consider:
* Measurement units of the variable
* Example usage
* Question text: include the exact wording from the survey questions
* Missing data: describe all missing codes and indicate the types of missing data, like system missing, data instrument error, and participant skip error

# Sample Data Dictionary 

Below is a shortened data dictionary for the dataset we looked at in exercise 1. You can download the sample data dictionary [here](https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_template.csv) (CSV file) 

**NOTE: These values here are <u>made up</u> for educational purposes, they do not reflect what the real study had in mind.**

| Column Name | Meaningful Name             | Description                                                                                                                                                                                   | Data Type | Data Usage Type       | Sample Values                               |
|-------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------|---------------------------------------------|
| STATEFP10   | State code                | The unique numeric code for the state. More information on state codes can be found [here](https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971).                                | String    | Dimension Attribute   | “01”, “02”, “06”                            |
| COUNTYFP10  | County code               | The unique numeric code for the county. More information on county codes can be found [here](https://www2.census.gov/programs-surveys/decennial/2010/partners/pdf/FIPS_StateCounty_Code.pdf). | String    | Dimension Foreign Key | “001”, “003”, “005”                         |
| GEOID10     | Geographical ID           | Combined state, county, and tract identifier.                                                                                                                                                 | String    | Dimension Foreign Key | “26163593300”                               |
| FFFPCT      | Fast Food Percentage      | Percentage of restaurants classified as fast food.                                                                                                                                            | Number    | Fact                  | 40.3, 55.8, 22.5                            |

## Data Dictionary Template

You can download a data dictionary template [here](https://repository.upenn.edu/entities/publication/0430ccdd-cbd8-4404-9f54-11cb81d5b3b1). Modify the elements included so they fit your project. 

<br> 

<b>Here is a breakdown of what we covered:</b> A data dictionary is an informative document about the dataset's variables, content, structure, and other details needed for understanding and reproducing the research. Remember to have a consistent and clear style, and record any updates made. Aim to make your data dictionary accessible to others and for the future by saving it in a non-proprietary format.
{: .note}

# Congrats!
{: .no_toc }

*Hooray!* You can now create a data dictionary so you and other researchers can understand the dataset with no problems!

<br>
---

<b>Sources</b>
* Harvard Biomedical Data Management. Data Dictionary. (https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/data-dictionary)
* Penn Libraries Guides. Data Management Resources. (https://guides.library.upenn.edu/c.php?g=564157&p=9554907)
* Phegley, L. (2023). University of Pennsylvania. Data Dictionary Blank Template. (https://repository.upenn.edu/entities/publication/0430ccdd-cbd8-4404-9f54-11cb81d5b3b1)
* Stony Brook University Data Governance. Data Dictionary Standards. (https://www.stonybrook.edu/commcms/datagovernance/structureandroles/datadictionarystandards)

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
