---
layout: default
title: Create a Data Dictionary
nav_order: 12
---


<img src="figures/work-in-progress.png" width="600"/>



# What is a Data Dictionary? 
{: .no_toc }
A data dictionary is a type of document that provides essential information about variables from a dataset. It includes their definitions, descriptions and structure. The primary goal of a data dictionary is to help people understand and use a dataset, especially if you’re working with multiple tables. A data dictionary may be included with the dataset or exist as an independent resource.

Overall, having a data dictionary is important for research reproducibility and revisitation. It clarifies questions like, “What does this variable mean?”

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

It’s common for long-standing research projects to have a data dictionary. Here are some examples you can explore to see the variation in how data dictionaries are represented and the kind of information they contain:
* [National Database of Deep-Sea Corals](https://www.ncei.noaa.gov/waf/dsc-data/metadata/20221213-0_NOAA_NDB_corals_sponges_data_dictionary.html)
* [Climate and Forecast Conventions](http://cfconventions.org/Data/cf-standard-names/46/build/cf-standard-name-table.html)
* [Organic Carbon Sorption and Decomposition in Selected Global Soils](https://tes-sfa.ornl.gov/sites/default/files/Soil_C_Decomp_Data_Dictionary_20140616.pdf)
* [Planetary Science Dictionary (NASA)](https://pds.nasa.gov/tools/dd-search/)

A data dictionary can be a simple table on a spreadsheet or PDF, or a detailed web application. For some projects, a data dictionary can be created and maintained by one research member, but it can also be done by the whole research team.


## Exercise 1
{: .no_toc}
{: .label .label-green }

Let’s pretend you’re a researcher and you’ve come across this dataset that may be helpful for your project. You would like to know more about it and make sense of the deposited data with it.

Here is the dataset, accessible by the hyperlinked DOI:  
>Florida, Richard, 2013, "Class-Divided Cities, Detroit Edition Published in Atlantic Cities", <a href="https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/SNXXHQ" target="_blank">https://doi.org/10.5683/SP3/SNXXHQ</a>, Borealis, V3

From the deposited files, please download **“Detroit Class Data.xlsx”** in the original file format. Then, to examine the data and to determine the appropriateness for your project, try to answer the following questions: 
1. What do the columns STATEFP10 and COUNTYFP10 mean?
2. Describe the different measures of the study
3. Describe how the data was collected?


Additionally, take a look at this dataset below. It may also be difficult to understand the data at first, but with the data dictionary included, it is much easier to make sense of it.
>Barsky, Eugene; Mitchell, Marjorie; Buhler, Jeremy, 2019, "UBC Research Data Management Survey: Science and Engineering", [https://doi.org/10.5683/SP2/9VEAT9](https://doi.org/10.5683/SP2/9VEAT9), Borealis, V3


<img src="figures/data_dictionary.png" width="200"/>

---

## Creation considerations for a data dictionary 

Document your work as you progress through your research. This means revising your data dictionary when new elements and/or variables are added or updated, which will also help reduce the risk of forgetting valuable information or losing details. Maintenance of your data dictionary is just as important as creating it!

Any text editor can be used to create a data dictionary. However, for this kind of document, we suggest using spreadsheet editing software. CSV, TSV, or XLSX are common [file formats](https://ubc-library-rc.github.io/rdm/content/02_file_formats.html) because they’re lightweight and non-proprietary. These formats are also compatible with various applications and good for preservation (future-friendly).
* If you create a data dictionary in a CSV or TSV format, please note that any formatting will be lost (no colour, bolding, font, formulas, font size, etc.). Only the data will be saved, so if formatting is important, then save it in an XLSX format. 

Once your data dictionary is created, store it where your data files are kept (here is our workshop on [directory structures](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)). Having the data dictionary nearby makes access to the guidebook more convenient, and it’s stored in a place where other important files are. 

### Data dictionaries in UBC REDCap
{: .no_toc}

REDCap is an application that helps build and manage surveys and databases for data collection. This tool may also be useful for designing and managing data dictionaries. In REDCap, there is the option to download the data dictionary file (in CSV format), make edits to fit your research variables (adding, removing, or modifying existing elements), and then re-upload the file to REDCap to apply the changes. 

UBC runs two instances of REDCap: [UBC Advanced Research Computing (ARC)](https://arc.ubc.ca/software/redcap) and [UBC Faculty of Medicine](https://restech.med.ubc.ca/our-services/electronic-data-collection/). 
* Please [contact UBC ARC](arc.support@ubc.ca) for more information about which instance to use for your research. 

## Stylistic considerations for a data dictionary

How your data dictionary is written is also important. Consider some of these best practices for data documentation:
* Be as clear and specific as possible when describing elements of your project
* Follow a style that’s consistent and agreed upon by the research team
 * You can also note these stylistic decisions in your [README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html)
* Consider your audience: will you be using jargon? If so, perhaps you may want to clarify the specialized terminology or look for an alternative word. If you refer to acronyms or abbreviations, make sure you’re defining them
* The data dictionary can simply be named ```DATA-DICTIONARY``` or ```_DATA-DICTIONARY```, but additional information can be added if necessary

A data dictionary is commonly formatted as a table with the variables placed in rows and variable information placed in columns. At the top of your data dictionary, you should include relevant descriptive metadata such as:
* A descriptive title and the name of the dataset
* The creation date of the data dictionary (using a standardized format like [ISO 8601](https://www.w3.org/TR/NOTE-datetime): YYYYMMDD or YYYY-MM-DD)
* A version number or a last updated date

## Recommended content 

Every research project is different. However, there are some elements you should consider including in your data dictionary. These elements will help users understand the details of your dataset variables, which will aid their overall understanding of your research. 

Primary elements to consider:

| **Element** | **Details** |
|-----------|-------------|
| **Variable ID** | The name used to identify a specific variable. This can be a sequence of alphanumeric characters. |
| **Variable name** | The name used to identify a specific variable in a human language, like English. Don’t include numbers, abbreviations, or acronyms. |
| **Variable definition** | The explanation of what a variable means, how it was calculated, how it should be used, and/or any known patterns. You can refer to existing discipline-specific vocabularies to increase interoperability (e.g. [Unified Medical Language System](https://www.nlm.nih.gov/research/umls/index.html)). |
| **Variable type** | The format of a variable (e.g., string, number, percentage, date). |
| **Allowable values/parameters** | Describe the permitted values that can be entered. For example: minimum/maximum values for numerical entries, a list of options for character values, or whether the field accepts nulls. |
| **Requirement** | Indicate if a variable is required with a "yes" or "no". |
| **Notes** | Add any extra notes, remarks, or instructions that help contextualize a variable. |

Secondary elements to consider:

| **Element** | **Details** |
|-----------|-------------|
| **Example usage/sample values** | Provide some examples of how a variable is implemented, or what a variable may look like. |
| **Measurement units** | The measurement unit of a variable. |
| **Question text** | Include the exact wording from the survey, interview, task, etc. |
| **Timestamp** | The time a variable’s data was collected. |
| **Missing data** | Describe the missing data for a specific variable, including the type of missing data. For example: the system missing the data, a data instrument error, or a participant skip error, etc. |

## Question
{: .no_toc}
{: .label .label-green }
In Exercise 1, we looked at a dataset without a data dictionary. It was quite difficult to understand what the dataset variables meant, so we created an unofficial data dictionary to help us make sense of the research. 

Please navigate to the sample data dictionary provided below — you can view it directly on the page, or download the file. Once you’ve viewed the content, try to answer the following questions:
- Which elements are considered primary and secondary?
- Would you change (add/remove) anything about this data dictionary?

## Sample data dictionary 

Here is a sample data dictionary you can view and/or [download as a file](https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_sample.csv). It includes some elements to provide information about the variables included in the research.

As a reminder, in the note box at the top, you can also download a data dictionary template that can be filled in and modified to fit your project. Both the sample and template data dictionary files are in a non-proprietary format that can be opened in many applications. 

*Please note that the content of the sample data dictionary was fabricated for educational purposes and does not reflect the real project’s objectives.* 

| Variable ID | Variable Name | Variable Definition | Variable Type | Allowable Values/Parameters | Requirement | Sample Values | Notes | 
| --- | --- | --- | --- | --- | --- | --- | --- |
| STATEFP10 | State code | The unique numeric code for the state. More information on state codes can be found [here](https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971). | String | Numerical values of 01-50 allowed | Yes | “01”, “02”, “06” | | 
| COUNTYFP10 | County code | The unique numeric code for the county. More information on county codes can be found [here](https://www2.census.gov/programs-surveys/decennial/2010/partners/pdf/FIPS_StateCounty_Code.pdf). | String | Numerical values of 001-110 allowed | Yes | “001”, “003”, “005” | | 
| GEOID10 | Geographical ID | Combined state, county, and tract identifier. | String | Numerical and alphabetical values allowed | Yes | “26163593300” | | 
| FFFPCT | Fast Food Percentage | Percentage of restaurants classified as fast food. | Number | Percentages from 0-100 allowed with one decimal place | Yes| 40.3, 55.8, 22.5 | | 


<br> 

<b>Here is a breakdown of what we covered:</b> A data dictionary is an informative document about the dataset's variables, content, structure, and other details needed for understanding and reproducing the research. Remember to have a consistent and clear style, and record any updates made. Aim to make your data dictionary accessible to others and for the future by saving it in a non-proprietary format.
{: .note}

# Congrats!
{: .no_toc }

*Hooray!* You can now create a data dictionary so you and other researchers can understand the dataset with no problems!
<br>

---

**Additional resources**
{: .no_toc }
The Alliance Programmatic Codebook Generator (a tool that may be helpful for you): [https://alliance-rdm-gdr.github.io/RDM_Codebook_App/](https://alliance-rdm-gdr.github.io/RDM_Codebook_App/) 

**Sources**
{: .no_toc }
* Harvard Biomedical Data Management. Data Dictionary. <https://datamanagement.hms.harvard.edu/collect-analyze/documentation-metadata/data-dictionary> 
* Penn Libraries Guides. Data Management Resources. <https://guides.library.upenn.edu/c.php?g=564157&p=9554907>
* Phegley, L. (2023). University of Pennsylvania. Data Dictionary Blank Template. <https://repository.upenn.edu/entities/publication/0430ccdd-cbd8-4404-9f54-11cb81d5b3b1>
* Stony Brook University Data Governance. Data Dictionary Standards. <https://www.stonybrook.edu/commcms/datagovernance/structureandroles/datadictionarystandards>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
