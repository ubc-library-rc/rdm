---
layout: default
title: File Naming
nav_order: 4
---
<img src="figures/work-in-progress.png" width="500" style="margin-left:30px"/>

# Why is File Naming Important?
{: .no_toc }

Creating a well-organized hierarchy of files with clear naming conventions is an important part of improving your research process. This is especially important if you are working with large datasets and complex output files, or coordinating with multiple people across multiple institutions.

There are many ways to structure your folders, and multiple naming conventions you can use. The key is <b>consistency</b>. Make your file names descriptive, and include information about dates and versioning. The best practice is to consult with your lab or with your co-workers to develop a naming schema that everyone is willing to follow consistently.

Looking for a cheat sheet? Check out our <a href="https://osf.io/pfweq" target="_blank">one-pager</a>!
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

Although these file names may look acceptable, they have poor formatting characteristics that will help you in the short- and long-term. 
- 10_data 2.txt 
- Lily's schedule&plan 2022Jul9.xlsx

When using ineffective file naming conventions, this is what you may encounter:
<img src="figures/file_names.png" width="200" style="margin-left:30px"/>

These example file names are better and more effective. We'll see why in the following sections
- 003_raw-data_2022-07-09.txt
- 20220709_interview-script_v01.docx

---

# Three principles for optimal file names  &nbsp; <img src="figures/thumbs-up.png" align="center" width="45"/>
{: .no_toc }
1. Machine-Readable
2. Human-Readable
3. Supports Default Ordering 

The overall goals of good file names are:
- Have the file name characters be correctly handled by all computer systems
- Have the file name be comprehensible to humans
- Have the file name be concise, yet descriptive
- Be consistent with the chosen naming convention

## *1*{: .circle .circle-blue} &nbsp; Machine-Readable 
### Consider the following for your files to be machine-readable:
{: .no_toc }
- Use alphanumeric characters: Latin alphabetic characters (abc) and Arabic numerals (123)
- Use a type of spacing case to separate file name elements:
   - Snake case: use <b>underscores</b> _ to separate words and numbers
   - Camel case: use <b>capitalization</b> to separate words and numbers
   - Hyphens: use <b>hyphens</b> – to separate words and numbers

Spacing case examples:
- `this_is_snake_case`
- ThisIsCamelCase`
- `this-is-using-hyphens` 
 
When using capital and/or lowercase letters, be mindful of case sensitivity. This is because some operating systems may search for file names of a certain case, such as only capital letters or lowercase letters.

Also, it's best to avoid empty spaces and special characters because these may be used by operating systems to perform tasks. This also could make it difficult for your machine to read the file name properly.
- Special characters such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " \ | 

<img src="figures/machine-reading.png" width="200" style="margin-left:30px"/>

### Exercise 1
{: .no_toc }
{: .label .label-green }

Here's a look into someone's folder containing dessert recipes. Let's improve these file names using what we've learned so far! Pick a file and rename it to make it more machine-readable. 

What did you change and why?

<img src="figures/cakes-example.jpeg" width="600" style="margin-left:30px"/>


## *2*{: .circle .circle-red} &nbsp; Human-Readable
### Consider the following for files to be human-readable:
{: .no_toc }
- Have file names that follow a consistent naming method, and document this file naming method in your [README](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html) file
    - Especially if acronyms, abbreviations, and/or codes are used, you should define what they mean in your README file

 ### Be consistent:
{: .no_toc }
Make sure you're consistent in the way you name your files. The style you choose should be based on conventions adopted in a given project, organization, language, etc.
- Example: R and Python use snake case, so file names and folder names should follow this convention
 
- The file names should be concise but detailed enough so that they're still understandable to you and anyone else who has access
    - The amount of detail is up to you, but the names shouldn't be *too* long - we recommend having 3 to 5 elements per file name, or under 32 characters
    - This is especially important for the future!
    - We recommend ordering elements from general to specific to make searching easier
- Avoid including application (software) details in your file names
    - Example: you don't need to add "doc" to the file name of a text document

More examples:
```
# not good
a.txt

# too much information
ubc_application_letter_for_institution_position_firstname_lastname_final_date.txt

# okay but can be a bit more detailed
application.txt

# not amazing, a bit too much detail
clean_data_py_script.py

# good, just enough detail
ubc_application_letter.txt

# good
clean_data.py

# also great
FileNm_Guidelines_20180409_v01.docx
```

<img src="figures/human-reading.jpg" width="200" style="margin-left:30px"/>


## *3*{: .circle .circle-yellow} &nbsp; Supports Default Ordering 
<img src="figures/comic.gif" width="200" style="margin-left:30px"/>

### Goals:
{: .no_toc }
- Decide at the beginning how you want to sort and search for your files to ensure a good hierarchical directory structure:
     - Chronological order
     - Logical order
- Versioning and version types should be added as the last element

### Chronological order
{: .no_toc }
Use <a href="http://www.w3.org/TR/NOTE-datetime" target="_blank">ISO 8601 standard</a>: <b>YYYYMMDD</b> or <b>YYYY-MM-DD</b> for consistent formatting and correct interpretation of dates.

Sorting your files chronologically (having the date as the first name element) may look like this:
```
2024-01-01_subject_1_results.xlsx
2024-01-01_subject_2_results.xlsx
2024-02-01_subject_1_results.xlsx
2024-02-01_subject_2_results.xlsx
```

### Logical order
{: .no_toc }
When using a sequential numbering system, use <b>leading zeros</b> to make sure files sort in sequential order
- Examples: 001, 002, 010, 011...

Sorting your files logically (using leading zeros) may look like this:
```
00_innit.R
01_read_data.R
02_clean_data.R
03_model.R
04_visualize.R
helper01_load_variables.R
helper02_functions.R
```

### Version Number and Version Types
{: .no_toc }
Adding a version to the file name should be the last element.

Use at least 2 digits with a leading zero for the version number, and/or indicate the version type.
   - Version number examples: V01, V03, etc.
   - Version type examples: _raw, _processed, _composite, etc.

### Exercise 2
{: .no_toc }
{: .label .label-green }

Your lab has a spectrometer that measures thermal emissions once a day for a year for your experiment. There are three people who take that measurement in the lab.

Have a try at creating a file naming convention for these files to reflect what you learned about today's session. 

How did you structure your file names and why? 

<img src="figures/thermometer.jpg" width="200" style="margin-left:30px"/>

[//]: # (activity link: https://bit.ly/rdmactivity)

<br>

<b>Here is a breakdown of what we covered:</b>
File names should be machine-readable: use alphanumerical characters with snake or camel case, and don't have spaces or special characters. File names should also be human-readable: clear, concise, and follow a consistent naming method. Lastly, a good file naming convention helps with sorting and searching your files.
{: .note}

# Congrats!
{: .no_toc }
*Hooray!* Now you know how to organize files with your own file naming conventions. 

---


### Sources
{: .no_toc }
- Caltech Library. File Naming Convention Worksheet. <https://authors.library.caltech.edu/103626/1/FileNamingConventionWorksheet_Caltech.pdf>
- Data Carpentry. File Organization: Naming. <https://datacarpentry.org/rr-organization1/01-file-naming/index.html>
- Exadox. Folder and File Naming Convention - 10 Rules for Best Practice. <http://www.exadox.com/en/articles/file-naming-convention-ten-rules-best-practice>
- Harvard Biomedical Data Management. File Naming Conventions. <https://datamanagement.hms.harvard.edu/collect/file-naming-conventions>
- Harvard Library Guides. File Naming Best Practices. <https://guides.library.harvard.edu/c.php?g=1033502&p=7491825>
- Stanford University Libraries. Data Best Practices and Case Studies. <https://guides.library.stanford.edu/data-best-practices>


---


Need help?
{: .label .label-blue }
 Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.

