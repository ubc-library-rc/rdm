---
layout: default
title: File Naming
nav_order: 4
---
# Why is file naming important?
{: .no_toc }


<p style="margin-top:20px;margin-bottom:25px">
Creating a well-organized hierarchy of files with clear naming conventions is an important part of improving your research process. This is especially important if you are working with large data sets and complex output files or coordinating with multiple people at multiple institutions. There are many ways to structure your folders, and multiple naming conventions you can use. The key is <b>consistency</b>. Make your file names descriptive, and include information about dates and versioning. The best practice is to consult with your lab or with your co-workers to develop a naming schema that everyone is willing to follow consistently.
</p>


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

<b>Warm up!</b>  

What do you think about the following file names?
- 10_data 2.txt 
- figure 1.png 
- final revision.docx
- Lily's schedule&plan 2022Jul9.xlsx

<p style="margin-bottom: 40px"></p>

Are these names better? 
- better-filenames.txt
- 003_raw-data_2022-07-09.txt
- fig01_scatterplot-talk-length-vs-interest.png
- 20220709_interview-script_v01.docx

<p style="margin-bottom:40px"></p>
 
<p>This is what happens when you do not have effective naming conventions:
</p>
<img src="figures/file_names.png" width="200" style="margin-left:30px"/>

We will see very shortly why effective naming conventions are a necessity!

<p style="margin-bottom:60px"></p>







---


<p style="margin-bottom: 60px"></p>


# Follow these three principles!  &nbsp; <img src="figures/thumbs-up.png" align="center" width="45"/>
{: .no_toc }


<p style="margin-bottom: 25px"></p>


*1*{: .circle .circle-blue} &nbsp;Machine-Readable


*2*{: .circle .circle-red} &nbsp;Human-Readable 


*3*{: .circle .circle-yellow} &nbsp;Supports Default Ordering 




<br>


## *1*{: .circle .circle-blue} &nbsp; Machine-Readable 
<img src="figures/machine-reading.png" width="200" style="margin-left:30px"/>

<p style="margin-top:20px;margin-bottom:20px">

</p>

### Goals:
{: .no_toc }
- Characters in file names are handled correctly by all computer systems
- Be consistent with the chosen naming convention


<p style="margin-bottom: 25px"></p>


### For files to be machine-readable, use the following:
{: .no_toc }


<p style="margin-bottom: 20px"></p>


- Alphanumeric characters: Latin alphabetic characters and Arabic numerals 

- Snake case: use _ <b>underscores</b> to separate words and numbers
   -  `this_is_snake_case`
  
- Camel case: use <b>capitalization</b> to separate words and numbers 
   - `thisIsCamelCase`

- Hyphens: use – <b>hyphens</b> to separate words and numbers
   - `this-is-using-hyphens`

- Avoid spaces and other special characters, such as: ~ ! @ # $ % ^ & * ( ) ` ; : < > ? . , [ ] { } ' " \|
   - Certain special characters are used by operating systems to perform tasks. This makes it difficult for the machine to read the file names

- Be mindful of case sensitivity
   - Some operating systems may search for file names of a certain case
   - Example: searching for "PROJECT" may only return files containing the same name and case, and not "project"




### Be consistent:
{: .no_toc }
- The way you name your file should be consistent
- The style you choose should be based on conventions adopted in a given project, organization, language, etc.
   - Example: R and Python use snake case, so file names and folder names should follow this convention

<br> 
<br>

### Exercise 1
{: .no_toc }


<p style="margin-bottom: 20px"></p>


Let's improve these file names using what we've learned so far! Pick a file and rename it to make it more machine-readable. 

What did you change and why?

<p style="margin-top:20px">
<img src="figures/cakes-example.jpeg" width="600" style="margin-left:30px"/></p>


[//]: # (activity link: https://bit.ly/rdmactivity)


<br>


<br>




## *2*{: .circle .circle-red} &nbsp; Human-Readable

<p style="margin-top:20px">
<img src="figures/human-reading.jpg" width="200" style="margin-left:30px"/>
</p>

### Goals: 
{: .no_toc }
- Consistency
- Intelligible to humans
- Concise yet descriptive

### For files to be human-readable, consider the following:
{: .no_toc }

<p style="margin-bottom: 20px"></p>

- Have file names that follow a consistent naming method, and document this file naming method in your README file
    - Especially if acronyms, abbreviations, and/or codes are used, you should define what they mean in your README file
- The file names should be concise but detailed enough so that they're still understandable to you and anyone else who has access
    - Names shouldn't be *too* long
    - This is especially important for the future!
- Avoid including application (software) details in your file names
    - Example: you don't need to add "doc" to your file name of a text document
- Overall, the amount of detail is up to you, but we recommend having 3 to 5 elements per file name

<p style="margin-bottom:30px"></p>

Examples:
```
# not good
a.txt

# too much information
clean_data_py_script.py

# okay but can be a more detailed
application.txt

# not amazing, a bit too much detail
ubc_application_letter_for_institution_position_firstname_lastname_final_date.txt

# good, just enough detail
ubc_application_letter.txt

# good
clean_data.py
```

<br>
<br>


## *3*{: .circle .circle-yellow} &nbsp; Supports Default Ordering 
<p style="margin-top:20px">
<img src="figures/comic.gif" width="200" style="margin-left:30px"/>
</p>

### Goals:
{: .no_toc }
- Decide at the beginning how you want to sort and search for your files to ensure a good hierarchical directory structure:
     - Chronological order
     - Logical order
- Versioning and version types should be added as the last element


### Chronological order
{: .no_toc }
- Use <a href="http://www.w3.org/TR/NOTE-datetime" target="_blank">ISO 8601 standard</a>: <b>YYYYMMDD</b> or <b>YYYY-MM-DD</b> for consistent formatting and correct interpretation of dates

Sorting your files chronologically (having the date as the first name element) may look like this:
```
2024-01-01_subject_1_results.xlsx
2024-01-01_subject_2_results.xlsx
2024-02-01_subject_1_results.xlsx
2024-02-01_subject_2_results.xlsx
```


### Logical order
{: .no_toc }

- When using a sequential numbering system, use <b>leading zeros</b> to make sure files sort in sequential order
   - Examples: 001, 002, 010, 011... 100,101 ...
- We recommend ordering elements from general to specific to make searching easier

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


### Versioning and Version Types
{: .no_toc }
Adding a version to the file name should be the last element.

Use at least 2 digits with a leading zero for the version number, and/or indicate the version type.
   - Version number examples: V01, V03, etc.
   - Version type examples: _raw, _processed, _composite, etc.
 
<br>
<br>

### Exercise 2
{: .no_toc }

<p style="margin-bottom: 20px"></p>

Your lab has a spectrometer that measures thermal emissions once a day for a year for your experiment. There are three people who take that measurement in the lab.

Have a try at creating a file naming convention for these files to reflect what you learned about today's session. 

How did you structure your file names and why? 

<p style="margin-top:5px">
<img src="figures/thermometer.jpg" width="200" style="margin-left:30px"/>
</p>

[//]: # (activity link: https://bit.ly/rdmactivity)


<br>
<br>



# Congrats!
{: .no_toc }
<p style="margin-top:25px">
<img src="figures/congrats.jpg" width="200" style="margin-left:30px"/></p>

<b>Here is a breakdown of what we covered:</b>
- File names should be machine-readable: use alphanumerical characters with snake or camel case, and don't have spaces or special characters
- File names should be human-readable: clear, concise, and follow a consistent naming method
- A good file naming convention helps with sorting and searching your files


*Hooray!* Now you know how to organize files with your own file naming conventions. 


<br>


---




### Sources
{: .no_toc }
- <https://datacarpentry.org/rr-organization1/01-file-naming/index.html>
- <https://authors.library.caltech.edu/103626/1/FileNamingConventionWorksheet_Caltech.pdf>
- <http://www.exadox.com/en/articles/file-naming-convention-ten-rules-best-practice>
- <https://datamanagement.hms.harvard.edu/collect/file-naming-conventions>
- <https://pixabay.com>


---


Need help?
{: .label .label-blue }
 Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.

