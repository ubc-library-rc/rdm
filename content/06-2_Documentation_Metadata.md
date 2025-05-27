---
layout: default
title: Documentation and Metadata 
parent: Data Management Plans
nav_order: 3
---

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

---

# Is your data FAIR?

The **FAIR Data Principles** (Findable, Accessible, Interoperable, and Reusable), published in <a href="https://doi.org/10.1038/sdata.2016.18">Scientific Data</a> in 2016, are a set of guiding principles proposed by a consortium of scientists and organizations to support the **reusability of digital assets**. These principles have since been adopted by research institutions worldwide. The guidelines are timely as we see the unprecedented volume, complexity, and speed in the creation of data.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/fair-data-principles.png" width="600"/>
</p>

<p style="color:grey; font-size:11px; margin-left:30px">Image: <a href="https://www.openaire.eu/how-to-make-vour-data-fair" target="_blank">OpenAIRE</a>.
</p>

**F**indable
{: .label .label-purple }

        Findable data is discoverable thanks to its metadata.


**A**ccessible
{: .label .label-purple }

        Accessible data is always available and obtainable, this does not mean the files are open, 
        rather that you can access the metadata regarding the files.

**I**nteroperable
{: .label .label-purple }

        Interoperable data is able to be used by many researchers from many locations.

**R**eusable
{: .label .label-purple }

        Reusable data is described, licensed, and shared in such a way that wide reuse is possible.

**All data can be FAIR, but not all FAIR data is open**. OpenAIRE states that data should be "*as open as possible, as closed as necessary*." Not all data can be fully open, but it should still be findable at the metadata level.
{: .note}

<br>

## Want to make your data more FAIR? Metadata, the descriptive data about your project, supports your project's ability to be FAIR!
{: .no_toc}


<br>


# Metadata
Metadata is often described as "**data about data**" and helps answer the questions of who, what, when, where, why. This descriptive data is essential for creating FAIR and open data, and ensuring that the datasets you preserve will be accessible for many years to come.

<img src="figures/thumbs-up.png" align="center" width="25"/> Metadata makes it easier for researchers to:
- share their data,
- publicize their data,
- locate and retrieve data sets from others.

<p style="margin-top:25px;margin-left:30px;margin-bottom:25px">
<img src="figures/metadata1.jpg" width="300"/>
</p>



## Three of the most common categories
1. **Descriptive**: Descriptive metadata describes the content and context of your data at both the dataset and item level. 
- Examples: title, author, keywords
2. **Administrative**: Administrative metadata includes information needed to use the data.
- Examples: software requirements, copyright, licensing
3. **Structural**: Structural metadata describes how different datasets relate to one another, or any processing or formatting steps that were undertaken.
- Examples: Information about the relationship between datasets in a database, file formats

Reflection
{: .label label-blue }

        Take a moment to think about your research project. What kind of descriptive, administrative 
        and structural metadata might you want to record?


<br>


# Ensure your data is understandable

## Create a README File

<p style="margin-top:25px;margin-left:30px">
<img src="figures/readme.png" width="300"/>
</p>

To ensure that fellow researchers can understand and reuse your data, it is crucial to **describe what method you will use to facilitate comprehension**. One effective approach is to create a robust **README file**. This file should include comprehensive information about your dataset (i.e. *metadata*), such as its contents, provenance, licensing, and instructions on how to interact with it. 

You can refer to our <a href="https://ubc-library-rc.github.io/rdm/content/03_create_readme.html">Create a README File workshop</a> to learn how to create a solid README file.
{: .note }

<br>

## Data Dictionary or Codebook
In addition to the README file, you should **explain how you will define all your variables** in a data dictionary or codebook. This serves as a reference document that outlines the definitions and characteristics of each variable in your dataset. By clearly defining and documenting your variables, you enable other researchers to understand the structure and meaning of your data, promoting its effective reuse and interpretation. 

Alternatively, you can *utilize your README file* to provide this information.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/data_dictionary.png" width="600"/>
</p>


# Congrats!
{: .no_toc }

You have finished the documentation section! Please also make sure you record metadata during the research process *while the data is still active* and store it alongside your research data.

<p style="margin-bottom:25px;margin-left:30px">
<img src="figures/thumb-success.jpg" width="150"/>
</p>
  

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
