---
layout: default
title: File Naming
nav_order: 4
---

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

Although these file names may look acceptable, they have poor formatting characteristics that will be unhelpful to you in the short- and long-term. 
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
1. Machine-readable
2. Human-readable
3. Supports default ordering 

The overall goals of good file names are:
- Have the file name characters be correctly handled by all computer systems
- Have the file name be comprehensible to humans
- Have the file name be concise, yet descriptive
- Be consistent with the chosen naming convention

## *1*{: .circle .circle-blue} &nbsp; Machine-readable 
### Consider the following for your file names to be machine-readable:
{: .no_toc }
- Use alphanumeric characters: Latin alphabetic characters (abc) and Arabic numerals (123)
- Use a type of spacing case to separate file name elements:
   - Snake case: use <b>underscores</b> _ to separate words and numbers
     `this_is_snake_case`
   - Camel case: use <b>capitalization</b> to separate words and numbers
     `ThisIsCamelCase`
   - Hyphens: use <b>hyphens</b> – to separate words and numbers
     `this-is-using-hyphens`

When using capital and/or lowercase letters, **be mindful of case sensitivity**. This is because some operating systems may search for file names in a certain case, such as only uppercase or lowercase letters.

Also, it's best to **avoid empty spaces and special characters** because operating systems may use these to perform tasks. This could also make it difficult for your machine to read the file name properly.
- Special characters such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " \ 

<img src="figures/machine-reading.png" width="200" style="margin-left:30px"/>

### Exercise 1
{: .no_toc }
{: .label .label-green }

Here's a look into someone's folder containing dessert recipes. Let's improve these file names using what we've learned so far! Pick a file and rename it to make it more machine-readable. 

What did you change and why?

<img src="figures/cakes-example.jpeg" width="600" style="margin-left:30px"/>


## *2*{: .circle .circle-red} &nbsp; Human-readable
### Consider the following for files to be human-readable:
{: .no_toc }
You should aim to be consistent in the way you name your files. The style you choose could be based on conventions adopted in a given project, organization, language, etc. For example, R and Python commonly use files with snake case, so your file and folder names should follow this convention.

You should also document your naming method in your [README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html), especially if you're using acronyms, abbreviations, and/or special codes as part of your naming convention (which would need to be defined).

File names should be **concise but detailed** enough to be understandable to you and anyone else with access. The amount of detail is up to you, but names shouldn't be *too* long. Our recommendation is **3 to 5 elements per file name**, or around 32 characters, and ordering these elements from general to specific to make searching easier.  
- This is especially important for when you revisit your files in the future!
 
Lastly, avoid including application (software) details in your file names. For example, you don't need to add "doc" to the file name if that file is a text or Word document.

Here are some more examples of good versus bad file names:

| *Poor file names* | *Better file names* |
| -- | -- |
| application.txt | ubc_application_letter.txt |
| ubc_guidelines_institution_position_firstname_final.txt | FileNm_Guidelines_20180409_v01.docx |
| clean_data_py_script.py | clean_data_script.py |

<img src="figures/human-reading.jpg" width="200" style="margin-left:30px"/>


## *3*{: .circle .circle-yellow} &nbsp; Supports default ordering 
At the start of naming your files, decide how you want to sort and search for your files to have a good hierarchical directory structure. Some people want their files to sort themselves without manual organization, and the two common ways to achieve this are by using a chronological or logical system.  

### Chronological order
{: .no_toc }
Using a chronological ordering system includes having the date as the first element. This date should follow the [ISO 8601 standard](http://www.w3.org/TR/NOTE-datetime) (YYYYMMDD or YYYY-MM-DD) for consistent formatting and correct interpretation.

Sorting your files chronologically may look like this:
```
2024-01-01_subject_1_results.xlsx
2024-01-01_subject_2_results.xlsx
2024-02-01_subject_1_results.xlsx
2024-02-01_subject_2_results.xlsx
```

### Logical order
{: .no_toc }
Using a logical ordering system includes sequential numbers as the first element. However, make sure to include **leading zeros** as the first digit(s) so that files sort themselves logically. For example: 01, 02, 03, 001, 002, 003, 010, 012, 013, etc. 

Sorting your files logically may look like this:
```
00_innit.R
01_read_data.R
02_clean_data.R
03_model.R
04_visualize.R
helper01_load_variables.R
helper02_functions.R
```

### Version number and version type
{: .no_toc }
If you decide to add a version number and/or version type as a part of your file name, these should be placed as the **last** element. 
- Version numbers should include leading zeros too. For example: V01, V02, V03, etc.
- Version types should be separated with a spacing case as mentioned previously. For example: _raw, _processed, _composite, etc.

<img src="figures/comic.gif" width="200" style="margin-left:30px"/>

### Exercise 2
{: .no_toc }
{: .label .label-green }

Your lab has a spectrometer that measures thermal emissions once a day for a year as part of your experiment. There are three people in your research team who also help take those measurements in the lab.

Try creating a file naming convention for these files to reflect what you've learned. How did you structure your file names and why? 

<img src="figures/thermometer.jpg" width="200" style="margin-left:30px"/>

<br>

<b>Here is a breakdown of what we covered:</b>
File names should be machine-readable: use alphanumeric characters with snake or camel case, and don't have spaces or special characters. File names should also be human-readable: clear, concise, and follow a consistent naming method. Lastly, a good file naming convention helps with sorting and searching your files.
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

