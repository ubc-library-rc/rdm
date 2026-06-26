---
layout: default
title: Directory Structures
nav_order: 8
---

<img src="figures/work-in-progress.png" width="600"/>

# Why Are Structured Directories Important?
{: .no_toc }

Let’s pretend you store all of your digital files in one folder on your computer. Imagine how frustrating it would be, and how long it would take you to find data collected on a specific day 5 years ago! 

Instead of keeping every document in a single folder, files are often organized using a directory or folder structure. A good, consistent folder structure benefits you and others by making item access, retrieval, and storage more efficient. This will save you time, improve productivity, and overall make the research process more transparent and collaborative. 

Looking for a cheat sheet? Check out our <a href="https://osf.io/5br6a" target="_blank">one-pager</a>!
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

# Directory hierarchies

A typical directory structure is composed of a **root directory** (top-level folder), **subdirectories** (subfolders), and relevant **files**. 

A root directory contains the subdirectories, and the subdirectories contain the relevant files. However, there can be an exception for specific files that may need to exist outside of a subdirectory and be nested in a root directory (exist on their own): README files and data dictionaries.

There is no one-size-fits-all model for creating and organizing your directory. Instead, you should establish a directory that aligns with your project, so organize the folder hierarchy that works for you, your research team, and/or other users. 

However, one strong suggestion is to have your most important item(s) appear first. If you want better access to a file or folder, then have it appear first so you’re not stuck searching for it. 

Question:
{: .label .label-green}
Here’s a good example of what a common directory structure may look like. Please identify the top-level folder, the subfolders, and the files.

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

<img src="figures/folder_organizing.png" width="250" style="margin-left:30px"/>

# Directory structure organization

How files are organized in a subfolder should be relevant to the project. In other words, there should be meaning behind why the files are grouped, and not just for the sake of putting them together. 

For example, deciding to group text and spreadsheet files into a subfolder because they're all related to experiment #1, and then deciding to group all image files into another subfolder because they're all related to data visualization. 

To help improve searchability, keep these considerations in mind when organizing your files and folders:
* File and folder relationships
  * Decide how you will approach sorting your files into folders. Does a chronological, descriptive, or sequential approach work better for your research?
    * Chronological: organizing folders based on time
    * Descriptive: organizing folders based on file types or content
    * Sequential: organizing folders based on a specific order
* File and folder names
  * The file and folder names should follow [good naming practices](https://ubc-library-rc.github.io/rdm/content/01_file_naming.html): machine-readable (no special characters and no empty spaces between words), human-readable (the file or folder name reflects its content), and consistently formatted. 
* Folder structure or layout
  * Have a balance between the depth and shallowness of your folder structure: not too deep, but not too shallow.
  * If your directory is too deep or too shallow, then you would be scrolling or clicking around too much before finding the correct file. A directory that is too deep will result in a file path with too many folders, which can exceed the character limit.
    * For example: The length of a OneDrive root folder, like C:\users\meganb\OneDrive - Contoso, in addition to the relative path of the file (up to 400 characters), cannot exceed 520 characters [(Microsoft 2023)](https://support.microsoft.com/en-us/office/restrictions-and-limitations-in-onedrive-and-sharepoint-64883a5d-228e-48f5-b3d2-eb39e07630fa). In the Windows API, the maximum length for a path is 260 characters [(Microsoft 2024)](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry). If you had more files and folders, the character count can add up!

Proper or well-structured directory structures will help with data sharing. However, you should consider only sharing access to what is necessary and/or placing restrictions on sensitive files. For example, make your raw data read-only and work with its derivatives. In this way, your raw data is protected and can be referred back to if re-analysis is necessary. 


# Directory structure examples

```
Example 1: Files are sorted into subfolders representing different experiment attempts

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
Example 2: Files are sorted into subfolders representing different research elements

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


# README files and data dictionaries  

[README files](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html) and [data dictionaries](https://ubc-library-rc.github.io/rdm/content/07_data_dictionary.html) are two files critical for research transparency and reproducibility, and storing all metadata about your research: file and folder content, naming conventions, data structure, and much more. They both help you and anyone else understand the contents of your directory and data without needing to ask the author(s) directly. 

The two types of files needed to store all project metadata
| *File type* | *Description* | *Where it should be stored* |
| --- | --- | --- |
| README file | Elaborates on the contents and decision-making of the folder structure, discusses how, where, and who conducted the data collection, and more. Depending on the size of your research project and discipline, a README file can also contain variable definitions. | Stored in the root directory |
| Data dictionary | Elaborates on variable definitions and how they're used. | Stored where the data files are kept |


Because these two files are important for your research, they should be the first to appear when accessing a directory or folder. To help prioritize the access of these files, we recommend naming them all in capital letters and placing an underscore (_) at the start of the name. This will help push the files to the top of the directory when your machine organizes by default. 
- For example: ```_README``` and ```_DATA-DICTIONARY```

As a result, the directory structure may look like this:

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

Lastly, create your README file and data dictionary in a plain text format, such as Markdown (.md) or TXT (.txt). These formats aren’t reliant on special proprietary software, meaning they can be opened in many kinds of applications. You may often see README files called ```README.txt``` or ```README.md``` because they're commonly written in those plain text formats.

# Helpful design tools

Here are some helpful tools to help you plan out and design your directory structure without having to use your real files and folders. 

[Project Tree Generator](https://woochanleee.github.io/project-tree-generator/) and [Tree Generator](https://t.co/AQzht2i703) are easy online tools to use that allow you to create a directory structure. You can copy and paste your design into a document (plain text formatted) so you can save it and share it with researchers.

You can also use the ```tree``` function in the Terminal application. This will create tree-like structures for your files and folders without having to manually make a design. Windows and Linux should already have this function, but Macs would need to install it (helpful instructions can be found [here](https://instr.iastate.libguides.com/file-mgmt/foldertree#quick). 

<img src="figures/folders2.png" width="100" style="margin-left:30px"/>

## Exercise 1
{: .label .label-green}
{: .no_toc}

You’re a student in the UBC course BIOL 116 and working on your final research project. Here is what your files look like before submitting the final assignment:

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
Let’s practice planning out a directory structure! Please use one of the design tools mentioned above to organize these files. You can refer to this template (see below) for this exercise, or refer above to the previous examples for inspiration.

Use the provided tools below to put the files into an organized folder structure. You can copy this template and use it for this exercise:
```
├── example/
|   ├── example/           
|   |   ├── example

```

<br>

<b>Here is a breakdown of what we covered:</b>
Directory structures are crucial for file access, retrieval, storage, and research transparency. Follow a consistent organizational structure that makes sense for your project and research team. Use clear naming, logical structuring, and consistent relationships between files and folders. Limit the number of nested folders (neither too deep nor too shallow) and strive to make folder hierarchies as simple as possible. Lastly, README files should be placed in the root directory, and data dictionaries should be placed where the data is found because they contain important guiding information. 
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
