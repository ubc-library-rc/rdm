---
layout: default
title: Directory Structures
nav_order: 8
---

# Why Are Structured Directories Important?
{: .no_toc }

<p style="margin-top:15px"></p>

Let's pretend you store everything on your computer in one folder. Imagine how long it would take to find data you collected on a specific day a few years ago. Instead of keeping every document in a single place, files are often organized using directories or folder structures. 

A good, consistent folder structure benefits you and others by making item access, retrieval, and storage more efficient. This ultimately saves time and improves productivity. Folder structures make the research process more transparent and collaborative by ensuring everyone can find the files they need. 

<p style="margin-bottom: 20px"></p>

Looking for a cheat sheet? Check out our <a href="https://osf.io/5br6a" target="_blank">one-pager</a>!
{: .note}

<br>

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

<img src="figures/folder_organizing.png" width="400" style="margin-left:30px"/>

<p style="margin-bottom: 30px"></p>

---

# Organizing Your Directory Structure

There are several things to consider when deciding on the organization (structure) of your project directory. This includes the names, structure, and relationships of the files and folders. We recommend starting simple and making modifications along the way. 

Your directory should delineate segments of your projects to improve searchability. Some possible categories are project, time, location, and file type. 

You should have a good balance between the depth and shallowness of your folder structure. 
  * <b>Too deep:</b> too many clicks before you get to the file you need. A file path with too many folders to get through can max out the character limit
    * For example:
      * The length of a OneDrive root folder, like C:\users\meganb\OneDrive - Contoso, in addition to the relative path of the file (up to 400 characters), cannot exceed 520 characters [(Microsoft 2023)](https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa)
      * In the Windows API, the maximum length for a path is 260 characters [(Microsoft 2024)](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry)
    * Would you like to click through all these folders for a CSV file? `Z:\1232\New_Projects_shared\2000\2000_0889\site_a_name of the site payment\payment\year_4\payment_year4.csv` (by the way, is this good file-folder naming?)
  * <b>Too shallow:</b> too many different subdirectories under your root directory. This can also result in many clicks (and subsequent back clicks) before finding the correct file

File and folder names should reflect what they contain and follow good naming practices:
* Machine-readable
* Human-readable
* See our workshop on [file naming](https://ubc-library-rc.github.io/rdm/content/01_file_naming.html) for more information 

Lastly, when working with a team, consider implementing restrictions on sensitive files. For example, make your raw data read-only and work only with its derivatives. In this way, your raw data is protected and can be referred back to if re-analysis is necessary. 

<br>

# Directory Hierarchies
  
You should establish a folder hierarchy that aligns with your project. There is no one-size-fits-all model, so make an organizational system and hierarchy that works for you and anyone else who may be accessing the project, like your research team members or other collaborators. Deciding how to hierarchically organize depends on the nature of the project, but in general, you should put the most important item(s) first. 

A typical directory structure is composed of a **root directory** (i.e. top-level folder), **subdirectories** (i.e. subfolders), and relevant **files**.

Usually, we separate data, analysis, and reports into stand-alone subdirectories under the project's root directory. For example, the structure typically looks like this:   

```
├── Project-Folder/
|   ├── Experiment-Data/
|   |   ├── File-1
|   |   ├── File-2
|   ├── Experiment-Analysis/
|   |   ├── File-1
|   ├── Experiment-Report/
|   |   ├── File-1
|   |   ├── File-2
```

Question:
{: .label .label-green}
<p style="margin-bottom: 10px"></p>
Which ones in this example are root directories? What about subdirectories?

<br>

# Directory Structure Examples

```
Example 1: This example folder is organized such that the different experiments are in the subfolders

example_project
├── Project-Example_Folder/
|   ├── Experiment_1/
│   |   ├─ data.csv
│   |   ├─ data_cleaning.R
│   |   └─ model.R
|   ├── Experiment_2/
|   |   └─ . . . 
|   ├── Experiment_3/
|   |   ├── File-1
|   |   └─ . . .
```

```
Example 2: This example folder is organized such that the different components are in the subfolders 

another_example
├── Another-Example_Folder/
|   ├── data/
│   |   ├─ data_exp_1.csv
│   |   └─ data_exp_2.csv
|   ├── cleaning/
│   |   ├─ clean_exp1.R
│   |   └─ clean_exp2.R
|   ├── visualization/
|   |   └─ . . .
```

<br>

# README Files and Data Dictionaries 

README files and data dictionaries are critical for transparency and reproducibility because they contain a brief description of the major folder contents, naming conventions, and data structure. They allow for an easier understanding of the contents of your directory and data without needing to ask the author(s). This is especially helpful when working with a group or sharing directories with others. See our workshops on [README files](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html) and [data dictionaries](https://ubc-library-rc.github.io/rdm/content/07_data_dictionary.html). 

## Two types of files needed to store all metadata

1. ```README``` file: resides in the **root directory** and elaborates on the contents and decision-making of the folder structure. It also discusses how, where, and who conducted the data collection.
2. ```DATA-DICTIONARY``` file: resides **where the data files are placed** and elaborates on how the data variables are defined and described.

For example, the directory structure may look like this:

```
├── Project-Folder/
|   ├── _README.md                  <----
|   ├── Experiment-Data/
|   |   ├── _DATA-DICTIONARY.md     <----
|   |   ├── File-1
|   |   ├── File-2
|   ├── Experiment-Analysis/
|   |   ├── File-1
|   ├── Experiment-Report/
|   |   ├── File-1
|   |   ├── File-2
```

```README``` files and ```DATA-DICTIONARIES``` should be the first things to appear when looking at any directory or folder, as these are your guides to its contents. We recommend naming them in all capital letters and including an underscore (_) at the start of the file name to make them stand out and appear at the top. 

```README``` files and ```DATA-DICTIONARIES``` should be written in a plain text format. This will ensure that these files won't rely on special proprietary software and can be opened on any computer. You will often see readme files called ```README.txt``` or ```README.md``` because they're commonly written in TXT or Markdown plain text formats.

<p style="margin-bottom: 30px"></p>

## Exercise 1
{: .label .label-green}
{: .no_toc}

<p style="margin-bottom: 10px"></p>

You’re in the UBC course BIOL 116, and you’re working on your research project. You have files that looked like the following before submitting the final assignment:

```
Pither_20210921_BIOL116RProject_ph-data.csv
Pither_20210922_BIOL116RProject_ph-data.csv
Pither_20210923_BIOL116RProject_ph-data.csv
Pither_20210924_BIOL116RProject_ph-data.csv
Pither_BIOL116RProject_Analysis_V0.xlsx
Pither_BIOL116RProject_Figure-freq-plot_V0.png
Pither_BIOL116RProject_Figure-linear-reg_V0.png
Pither_BIOL116RProject_Figure-linear-reg_V1.png
Pither_BIOL116RProject_Lab-report_V0.docx
Pither_BIOL116RProject_Lab-report_V1.docx
Pither_BIOL116RProject_Lab-report_V2.docx
Pither_BIOL116RProject_Lab-report_V3.docx
```

Use the provided tools below to put the files into an organized folder structure. You can copy this template and use it for this exercise:
```
├── example/
|   ├── example/           
|   |   ├── example

```

You can also refer to the example that we saw earlier:
```
├── Project-Folder/
|   ├── _README.md                  
|   ├── Experiment-Data/
|   |   ├── _DATA-DICTIONARY.md            
|   |   ├── File-1
|   |   ├── File-2
|   ├── Experiment-Analysis/
|   |   ├── File-1
|   ├── Experiment-Report/
|   |   ├── File-1
|   |   ├── File-2
```

<p style="margin-bottom: 30px"></p>

[//]: # (activity link: https://bit.ly/rdmactivity)

# Suggested Design Tools 

Here are some useful tools to help you plan and design your folder structures:
* [Project Tree Generator](https://woochanleee.github.io/project-tree-generator/): You can paste your GitHub repository URL to generate a project tree or create it from scratch
* [Tree Generator by Nathan](https://t.co/AQzht2i703): Design a diagram for potential file tree with more options
* In your terminal, you can use `tree` to generate a tree-like structure. Windows and Linux have this function, but you will need to install it for Mac

<img src="figures/folders2.png" width="100" style="margin-left:30px"/>

<br>

<b>Here is a breakdown of what we covered:</b>
Directory structures are crucial for file access, retrieval, storage, and research transparency. Follow a consistent organizational structure that makes sense for your project and research team. Use clear naming, logical structuring, and consistent relationships between files and folders. Aim for a balanced folder structure — not too deep or too shallow. Lastly, README files should be placed in the root directory, and data dictionaries should be placed where the data is found because they contain important guiding information. 
{: .note}

# Congrats!
{: .no_toc }

*Hooray!* Now you know how to create structured directories for files. Go ahead and organize your important personal or team files! 

<br>

---

### Sources
{: .no_toc }
- Copeland, C., Pither, J., Vis-Dunbar, M. (2021). Procedures and Guidelines. <https://ubco-biology.github.io/Procedures-and-Guidelines/>
- Harvard Biomedical Data Management. Directory Structure. <https://datamanagement.hms.harvard.edu/plan-design/directory-structure> 
- MIT Broad Research Communication Lab. File Structure. <https://mitcommlab.mit.edu/broad/commkit/file-structure/>
- MIT Libraries. File Naming and Folder Hierarchy. <https://libraries.mit.edu/data-management/store/organize/>
- New York University Libraries. File Organization. <https://guides.nyu.edu/data_management/file-org>
- UC Davis Library. Directory Structures. <https://guides.library.ucdavis.edu/data-management/directories>


---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
