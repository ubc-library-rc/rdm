---
layout: default
title: File Formats
nav_order: 5
---


# File Formats for Data Curation
{: .no_toc }

<p style="margin-bottom: 20px"></p>

A file format encodes information within a computer file so that it can be recognized by an application and accessed. The file name extension helps indicate the kind of format being used. Each file type (such as text, images, or sound) has many file formats available. 

Software and data storage technology change quickly, and files can become obsolete or difficult to access. In general, data files should be copied to new media every 2-5 years, especially if technology changes or if files begin to degrade. We strongly recommend using non-proprietary (open) file formats because it's important for preserving readability and long-term access for you and anyone else.

<p style="margin-bottom: 25px"></p>

Looking for a cheat sheet? Check out our <a href="https://osf.io/ena5p" target="_blank">one-pager</a>!
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
### Warm-up: Exercise 1
{: .no_toc}
{: .label .label-green }

A dancing club in Saskatoon has kept its documents since the early 2000s. Recently, a club member wanted to refer back to an older agenda from July 5th, 2003, but was unsuccessful in opening and viewing its contents properly. Below is the agenda file the club member wanted to open. 

Have a try at downloading the file in the WordPerfect format <a href="exercise_files/Agenda July 5th.wpd" target="_blank"> here</a>. Could you successfully open and view its contents on your machine? What do you notice? 
      
---
<b>What are some file formats you use often?</b> 
- .xls (Microsoft Excel) 
- .m4a (for digital audio)
- .doc (Microsoft Word) 
- .gdoc (Google Document)

These may be commonly used file formats, but they’re not recommended for data curation because they’re proprietary. These kinds of formats aren't sustainable and may cause access issues in the future.

<img src="figures/shock.png" width="150" style="margin-left:30px"/>

---

## What are proprietary file formats?

A file format is considered *proprietary* when it's limited by software patents, has a lack of format specification details, or has built-in encryption to prevent open usage by the public. As a result, specific software from a vendor (that may be inaccessible, like high costs) is required to use that proprietary format. 

However, in some cases, an industry may treat specific file formats as the de facto standard, even if they are proprietary and rely on expensive software.  

In your research, if you're using a specific proprietary format but want to ensure that your files are accessible in the future, here are some potential solutions:
- Save your raw data in its original, possibly proprietary, format and convert its derivatives/copies into a non-proprietary format to work with. Working with derivatives/copies will help protect the raw data from accidental data deletion or modification
- Include a section in your [README file](https://ubc-library-rc.github.io/rdm/content/03_create_readme.html) to document and inform others about your file format decisions, along with any available file derivatives in a non-proprietary format

You may have noticed that the WordPerfect file in the warm-up exercise couldn't be opened easily because it's a proprietary format. You may have been able to open it, but its contents may have been incomprehensible. This same kind of situation can also apply to other well-known file formats like Word or Google Docs. Once you no longer have proper access to use these kinds of software, how will you access your files?

<img src="figures/encryption.jpg" width="150" style="margin-left:30px"/>

<p style="margin-bottom: 50px"></p>

## What are non-proprietary (open) file formats?

A file format is considered *non-proprietary* when its specifications are available. This allows open-source developers to write software that can use the file format(s), in case a particular vendor no longer supports the format. 

Open file formats typically have similar qualities, such as:
- Freely available to use by everyone: unencrypted and uncompressed
- Has a decreased risk of technical obsolescence because it's not reliant on specific software
- Standard representation (such as ASCII or Unicode) and standard documentation
- Commonly used by the research community

Using open formats means you don't have to worry about relying on a single special software to read and use those files -- they can be opened in various software. You can expect that these files in an open format are better preserved and accessible in the future. 

<img src="figures/open-source.jpg" width="150" style="margin-left:30px"/>

## Additional considerations: File quality and file size 

File quality refers to the representation of an item's characteristics, such as its level of compression (for image files, for example). 

The file *quality* and *size* will depend on the kind of file format used. File formats encoded with a high quality will typically result in larger file sizes, compared to file formats encoded with a lower quality, which typically result in smaller file sizes. 

The trade-off is the cost of storage space, machine capability (if your machine can handle large files), and the convenience of sharing the file(s) with others. Therefore, you should consider your options carefully. 

## Common file format examples

This table has recommended file formats for good preservation and accessibility, as well as file formats to avoid. For more specific information, please refer to the sources listed at the end of this workshop. 

| File type | Recommended formats (shown as the file extension)                      | Avoided formats                |
|-----------|------------------------------------------|--------------------------------|
| Digital text      | .docx, .html, .pdf, .rtf, .txt, .xml           | .doc, .wpd                     |
| Digital images    | JPEGs (such as .jpg2, .jpeg, .jfif), .pdf, .png, .tiff    | Adobe Photoshop, camera raw formats (such as .arw and .cr2)            |
| Digital videos     | .mkv, .mov, MPEG-4s (such as .mp4 and .m4a)                          | .wmv                           |
| Digital audio     | .aiff, .flac, .mp3, .wav                | CD, DVD, .m4p, .mod, .xmi       |
| Datasets   | .csv, .db, .shp, .tsv, .xlsx | .xls                           |
| Web data  | .html, .json, .xml                       |                                |

<br>

### Exercise 2
{: .no_toc}
{: .label .label-green }

Let's convert a proprietary file into an open format for the future! 

Below is a dataset containing an .xls file, the proprietary Excel format. Please download the Excel file from the dataset and try converting it to a .csv format. 
  
Access the dataset here:  
>Yarmand, Shahram, 2019, "Replication data for: Stochastic and Deterministic Modeling of the Future Price of Crude oil and Bottled Water", <a href="https://doi.org/10.5683/SP2/VPF8J8" target="_blank"> https://doi.org/10.5683/SP2/VPF8J8</a>, Borealis, V1

How did you convert the Excel file into a CSV file? 

<img src="figures/bottles.jpg" width="150"/>

<br>

<b>Here is a breakdown of what we covered:</b>
Proprietary file formats have limitations, like requiring specific software, that may make accessing the file content difficult in the future.
Open file formats are highly recommended because they're sustainable and preserve well for the future.
{: .note}

# Congrats!
{: .no_toc }

*Hooray!* Now you know which file formats are appropriate for data curation, so your research data can be preserved for the long term.

<br>

---


### Sources
{: .no_toc }
- Duke University Libraries. File Formats for Preservation and Reuse. <https://guides.library.duke.edu/c.php?g=633433&p=4429351>
- Library of Congress. Recommended Formats Statement. <https://www.loc.gov/preservation/resources/rfs>
- MIT Libraries. File Formats for Long-Term Access. <https://libraries.mit.edu/data-management/store/formats/>
- New York University Libraries. File Format Selection. <https://guides.nyu.edu/data_management/file-formats>
- Northwestern Libraries. File Format Recommendations. <https://www.library.northwestern.edu/about/administration/policies/file-format-recommendations.html>
- Stanford University Libraries. Data Best Practices and Case Studies. <https://guides.library.stanford.edu/data-best-practices/format-files> 
- UMBC. Non-Proprietary File Formats. <https://lib.guides.umbc.edu/c.php?g=728911&p=5872066>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
