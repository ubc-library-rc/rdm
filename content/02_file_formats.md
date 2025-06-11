---
layout: default
title: File Formats
nav_order: 5
---

# File Formats for Data Curation
{: .no_toc }

<p style="margin-bottom: 20px"></p>

A file format encodes information within a computer file so that it can be recognized by an application and accessed. It is indicated by the file name extension. Each file type (such as text, images, or sound) has many file formats available. We strongly recommend using non-proprietary (open) file formats because it's important for preserving readability and long-term access for you and anyone else.

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
### Warm-up - Exercise 1
{: .no_toc}
{: .label .label-green }

<p style="margin-bottom: 10px"></p>

A dancing club in Saskatoon has kept its documents since the early 2000s. Recently, a club member wanted to refer back to an agenda from July 5, 2003, but was unable to open it. Please see the WordPerfect file below.  
    
Could you <a href="exercise_files/Agenda July 5th.wpd" target="_blank"> download that document </a>  and try to recover it on your machine? 

What do you notice? 
    
[//]: # (activity link: https://bit.ly/rdmactivity)

<p style="margin-bottom: 25px"></p>

---
<b>What are some file formats you use often?</b> 
- .xls (Microsoft Excel) 
- .mp3 (for digital audio)
- .docx (Microsoft Word) 
- .gdoc (Google Document)

<p style="margin-bottom: 25px"></p>

These are all commonly used file formats. However, these are not recommended for data curation because they are proprietary! In other words, these common formats are unsustainable. <img src="figures/say-no.png" width="20">

<p style="margin-bottom: 30px"></p>

<img src="figures/shock.png" width="150" style="margin-left:30px"/>

---

## What are proprietary formats?

A file format is considered *proprietary* when it's limited by software patents, lack of format specification details, or built-in encryption to prevent open usage by the public. 

This results in requiring specific software from a vendor to use the proprietary format. In some cases, an industry may treat specific file formats as the de facto standard even if the formats are proprietary and rely on expensive software.

You have noticed that the file in the warm-up exercise was an older proprietary file that can no longer be opened. This inaccessibility can happen to other proprietary formats like Microsoft Word or Google Docs.

<img src="figures/encryption.jpg" width="100" style="margin-left:30px"/>

<p style="margin-bottom: 50px"></p>

## What are non-proprietary (open) formats?

A file format is considered *non-proprietary* when its specifications are released, so open-source developers can write software to utilize the file format in case a particular vendor no longer supports the format. 

Qualities of open-format files:
- Freely available to use by everyone: unencrypted and uncompressed
- Has a decreased risk of technical obsolescence because it's not reliant on specific software
- Standard representation (such as ASCII or Unicode) and standard documentation
- Commonly used by the research community

<img src="figures/open-source.jpg" width="100" style="margin-left:30px"/>

<p style="margin-bottom: 50px"></p>

## Other considerations 

File quality and file size:
- File quality refers to the representation of an item's characteristics
- The file quality affects the kind of file format to use. The encoding that handles high resolution will have larger file sizes than lower-quality file formats. The trade-off is the cost of storage space and the convenience of sharing the file with others

## We recommend these common file formats

<p style="margin-bottom: 20px"></p>


| File Type | Recommended Formats                      | Avoided Formats                |
|-----------|------------------------------------------|--------------------------------|
| Text      | XML, ASCII, TXT, PDF, LaTeX, .docx       | .doc, .wpd                     |
| Images    | TIFF, JPEG2000, PNG, JPEG/JFIF           | RAW, Adobe Photoshop, PDF      |
| Video     | MOV, MPEG-2                              | .wmv                           |
| Audio     | PCM, WAVE, DSD                           | CD, DVD, .m4p, .mp3, xmi, .mod |
| Dataset   | CSV, TSV, .db, .sqlite, Shapefile, .xlsx | .xls                           |
| Web Data  | JSON, XML, HTML                          |                                |

<br>

### Exercise 2
{: .no_toc}
{: .label .label-green }

<p style="margin-bottom: 10px"></p>

Help us to preserve datasets for the long term! Download an Excel file ( .xls) from the dataset below and convert it to CSV.
  
Access this dataset:  
>Yarmand, Shahram, 2019, "Replication data for: Stochastic and Deterministic Modeling of the Future Price of Crude oil and Bottled Water", <a href="https://doi.org/10.5683/SP2/VPF8J8" target="_blank"> https://doi.org/10.5683/SP2/VPF8J8</a>, Borealis, V1

How did you convert the Excel file into a CSV file? What did you notice?

<img src="figures/bottles.jpg" width="200"/>
<p style="margin-bottom: 20px"></p>

[//]: # (activity link: https://bit.ly/rdmactivity)

<br>

# Congrats!
{: .no_toc }

- Proprietary file formats have limitations, like requiring specific software, that may make accessing the file content difficult in the future
- Open file formats are highly recommended because they're sustainable and preserve well for the future
{: .<b>Here is a breakdown of what we covered:</b>}

*Hooray!* Now you know which file formats are appropriate for data curation, so your research data can be preserved for the long term.

<br>

---


### Sources
{: .no_toc }
- <https://lib.guides.umbc.edu/c.php?g=728911&p=5872066>
- <https://guides.nyu.edu/data_management/file-formats>
- <https://www.library.northwestern.edu/about/administration/policies/file-format-recommendations.html>
- <https://www.loc.gov/preservation/resources/rfs>
- <https://pixabay.com>
- <https://www.pexels.com>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
