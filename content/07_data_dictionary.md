---
layout: default
title: Create a Data Dictionary
nav_order: 12
---

# Data dictionary
{: .no_toc }


A data dictionary is a variable-level documentation that tells us important information about the variables in the dataset. This is especially important if you are working with multiple tables or with a database. A data dictionary is typically formatted as a table with a row corresponding to a variable in your dataset and columns representing a field of information about that variable. The data dictionary should include variable names, data types, descriptions, and sample values.

The main goal of the data dictionary is to help people understand datasets. It will help your peers answer questions such as: "What does this variable mean?"
<p style="margin-bottom: 25px"></p>

Looking for a cheat sheet? Check out our <a href="https://osf.io/akzpq" target="_blank">one-pager</a>!
{: .note}

Most long-standing research projects will have a data dictionary, below are some open-source examples:

* [National Database of Deep-Sea Corals](https://www.ncei.noaa.gov/waf/dsc-data/metadata/20221213-0_NOAA_NDB_corals_sponges_data_dictionary.html)
* [Climate and Forecast Conventions](http://cfconventions.org/Data/cf-standard-names/46/build/cf-standard-name-table.html)
* [Organic Carbon Sorption and Decomposition in Selected Global Soils](https://tes-sfa.ornl.gov/sites/default/files/Soil_C_Decomp_Data_Dictionary_20140616.pdf)
* [Human Health Risk Assessment](https://rais.ornl.gov/documents/tm232.pdf)
* [Drug Product Database - Health Canada](https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/drug-product-database/terminology.html)
* [NCI Proteomic Data Commons](https://proteomic.datacommons.cancer.gov/data-dictionary/dictionary.html)
* [EarthExploer USGS Landsat](https://www.usgs.gov/centers/eros/science/landsat-data-dictionary#data_category)
* [Planetary Science Dictionary (NASA)](https://pds.nasa.gov/tools/dd-search/)

As you can see, a data dictionary can be a simple table (spreadsheet or PDF) or a full-fledged web application. Some projects only need one data dictionary that can be created and maintained by a single person while others will require a whole team to create and maintain it. 


## Exercise 1
{: .no_toc}
{: .label .label-green }

Please help us to make sense of a dataset.

Access a dataset:  

>Florida, Richard, 2013, "Class-Divided Cities, Detroit Edition Published in Atlantic Cities", <a href="https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/SNXXHQ" target="_blank">https://doi.org/10.5683/SP3/SNXXHQ</a>, Borealis, V3

Download the data file <b>"Detroit Class Data.xlsx"</b> in the <b>Original File Format</b>. Examining the data, try to answer the following questions:
1. What do you think the columns `STATEFP10` and `COUNTYFP10` mean?
2. Describe the different measures in this study.
3. How was the data collected?

Alternatively, here is an example of a dataset with a decent data dictionary:
>Barsky, Eugene; Mitchell, Marjorie; Buhler, Jeremy, 2019, "UBC Research Data Management Survey: Science and Engineering", [https://doi.org/10.5683/SP2/9VEAT9](https://doi.org/10.5683/SP2/9VEAT9), Borealis, V3

* You can see how a data dictionary allows users to make sense of the data very fast.
* Data dictionary can travel with the dataset or even serve as a stand-alone data item.

# How to create a Data Dictionary

* A data dictionary will typically be structured so each row corresponds to a column in your dataset and each column represents a field of information about the column. 
* Include the following fields: 
  
    * Column name 
    * Column name in plain English
    * Description of the Column
    * Data type 
    * Data usage type
    * Sample values

* Optional fields to include

    * Transformations (Was the column the result of a transformation?)
    * Example usage (SQL queries)
    * Missing values 
    * Values (this is useful if a column uses a scale/test)
    * Other notes 

## Template 

Below is an example data dictionary for the dataset we looked at earlier. This template was designed to capture most general datasets. There are other data dictionary templates available for more specific needs. 
**NOTE: These values here are <u>made up</u> for educational purposes, they do not reflect what the real study had in mind.**

<p style="margin-bottom: 25px"></p>

You can download this template in CSV [here](https://ubc-library-rc.github.io/rdm/content/assets/templates/data_dictionary_template.csv)
{: .note}


| Column Name | Meaningful Name             | Description                                                                                                                                                                                   | Data Type | Data Usage Type       | Sample Values                               |
|-------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------|---------------------------------------------|
| STATEFP10   | State code                | The unique numeric code for the state. More information on state codes can be found [here](https://www23.statcan.gc.ca/imdb/p3VD.pl?Function=getVD&TVD=53971).                                | String    | Dimension Attribute   | “01”, “02”, “06”                            |
| COUNTYFP10  | County code               | The unique numeric code for the county. More information on county codes can be found [here](https://www2.census.gov/programs-surveys/decennial/2010/partners/pdf/FIPS_StateCounty_Code.pdf). | String    | Dimension Foreign Key | “001”, “003”, “005”                         |
| TRACTCE10   | Census Tract Code         | Code identifying a specific census tract. More information on tract codes can be found [here](https://transition.fcc.gov/form477/Geo/more_about_census_tracts.pdf).                           | String    | Dimension Attribute   | “593300”                                    |
| GEOID10     | Geographical ID           | Combined state, county, and tract identifier.                                                                                                                                                 | String    | Dimension Foreign Key | “26163593300”                               |
| NAMELSAD10  | Area Name                 | The full name of the census area.                                                                                                                                                             | String    | Attribute             | “Los Angeles County, CA”, “Cook County, IL” |
| class       | Land Classification       | Indicates land use or classification.                                                                                                                                                         | String    | Dimension Attribute   | “Residential”, “Commercial”, “Agricultural” |
| CCPCT       | Child Care Percentage     | Percentage of households using child care services.                                                                                                                                           | Number    | Fact                  | 15.2, 25.4, 32.7                            |
| FFFPCT      | Fast Food Percentage      | Percentage of restaurants classified as fast food.                                                                                                                                            | Number    | Fact                  | 40.3, 55.8, 22.5                            |
| SCPCT       | Senior Citizen Percentage | Percentage of population over 65 years old.                                                                                                                                                   | Number    | Fact                  | 10.4, 15.8, 20.1                            |
| WCPCT       | Working Class Percentage  | Percentage of households in the working class.                                                                                                                                                | Number    | Fact                  | 45.2, 62.1, 51.3                            |

## The Style 

How you write your data dictionary is as important as the information you include. Always remember to be as clear as possible. Follow the style guide provided by your team to be consistent. The following are some general best practices related to data documentation:

* Don't use jargon 
* Define terms and acronyms 
* House the data dictionary where you [store data](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)
* Make it [machine-readable](https://ubc-library-rc.github.io/rdm/content/01_file_naming.html#1--machine-readable)

## The process 

Document your work as you go, so you don’t lose track of any details. If you wait until the end of your project, you might already have lost or forgotten valuable information.

You can create a data dictionary with any text editor but we suggest using some kind of spreadsheet (Excel, Numbers, etc.). Although you should edit the data dictionary with spreadsheet software, we suggest saving it as a CSV or TSV file as it is a non-proprietary format and freely available for everyone to use in the future. 


# Congrats!
{: .no_toc }

<p style="margin-top:25px;margin-left:30px">
<img src="figures/angel-congrats.jpg" width="300"/>
</p>

You are now ready to create your data dictionary so other researchers can understand your dataset with no problems!

<br>

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
