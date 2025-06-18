---
layout: default
title: Create a README File
nav_order: 6
---
# What is a README?
{: .no_toc}

A README file provides information about a project and helps ensure that data can be correctly interpreted by you and others when sharing or publishing data. It contains information commonly required to understand the dataset, its contents, provenance, licensing and how to interact with it. A README file is generally named ```README``` and is typically a text or markdown file.

In short, a README is a portable, durable way to inform other researchers about how to navigate, collaborate, or extend your project. Having them alongside your project(s) is good practice, especially when depositing data in a repository. 

<p style="margin-bottom: 20px"></p>

- Looking for a cheat sheet? Check out our <a href="https://osf.io/aqxw3" target="_blank">one-pager</a>
- Looking for a template to reuse? Check out our <a href="https://ubc-library-rc.github.io/rdm/content/assets/templates/UBC_README.txt" target="_blank">README template</a> 
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
<p style="margin-bottom: 20px"></p>

## Warm-Up: Exercise 1
{: .no_toc}
{: .label .label-green }

Let's access this dataset:
>Davis, Matthew, 2024, "Soil Adsorption Curves and Environmental Soil Data", <a href="https://doi.org/10.5683/SP3/JGRIN0" target="_blank">https://doi.org/10.5683/SP3/JGRIN0</a>, Borealis, V1

Take a look at the project and try to answer the following:

1. You got new data for ammonia absorption into soil from Corktown, how would you go about generating the new model and plot? 
2. You want to recreate the whole project, what package(s) do you need to have installed to rerun everything?
3. You have a question about this project, who and how can we reach the corresponding author?

<p style="margin-bottom: 20px"></p>

<img src="figures/confused.jpg" width="200" style="margin-left:30px"/>

[//]: # (activity link: https://bit.ly/rdmactivity)

---

## The Process of Creating a README

Consider creating a README file at the start of your project, or at least preparing a README before your project goes public, and continually updating it. One README file can be made for a dataset or a set of files that are of the same or similar formatting. If multiple READMEs are necessary, format them the same to maintain consistency. 

Place the README at the root directory of the project (check out our workshop on [directory structures](https://ubc-library-rc.github.io/rdm/content/04_directory_structures.html)) so it can be one of the first files people will look at. 

You can use any text editor to create a README. [Markdown](https://ubc-library-rc.github.io/Introduction-to-Markdown/) or TXT formats are commonly used because you can add lightweight formatting, and it is non-proprietary. Using a plain text format helps preserve your information because it relies on durable, open standards rather than proprietary formats.  

Some other common formats you might see are R Markdown (common in R projects) and reStructuredText (common in Python projects).

<p style="margin-bottom: 20px"></p>

## Recommended Content
  
Every project is different, so consider which of the following applies to your project. For example, a software project will have different sections than an academic research project.

* **Information** - Name and contact information, ORCIDs, how can people get in contact with you?
* **Description** - Let users know what your project does. Provide context - this can be similar to an abstract for a research paper, and information on what the data contains.
* **Dates** - Use a standardized format, like ISO 8601 (YYYY-MM-DD or YYYYMMDD)
* **Language**
* **Title of dataset or project**
* **Methodology** - Describe data collection, processing, and analysis, software and tools used, sample collection, etc.
* **Installation** - The project may work on your project, but not everyone has all the installations and dependencies installed. Let people know what they need to install to make sure they can run the data smoothly.
* **Data-specific information** - define any variables, codes, or acronyms
* **Usage** - Showing people an example of how your project/tool works can be very beneficial for users. 
* **Contributing** -  Let other users/collaborators know how they can contribute to the project. 
* **Acknowledgement** - Use this area to acknowledge people/resources that contributed to the project.
* **License** - If your project is open-source, mention the appropriate license, add any citation recommendations, and add any restrictions. 

<p style="margin-bottom: 20px"></p>

## Sample README 

<a href="https://ubc-library-rc.github.io/rdm/content/exercise_files/README_template.txt" target="_blank"> Download this sample README </a>. 

We created an example of a README for the project we looked at earlier in the warm-up exercise. This sample file was designed to capture academic research projects. There are other samples available for other types of projects (software, data science, etc.). 

**NOTE: The contents in the example template are <u>made up</u> for educational purposes, and do not reflect what the real study had in mind.**

## Exercise 2
{: .no_toc}
{: .label .label-green }

Now, let's practice what we just learned. 

From the sample template, what are some things that you noticed that may be specific to academic research? What are some things you would include if this were a software project? 

<img src="figures/readme.png" width="300" style="margin-left:30px"/>

<br>

<b>Here is a breakdown of what we covered:</b> 
READMEs are important documents containing information about your project's data. They help ensure your data is correctly interpreted and navigated for you and others in the future when revisited. READMEs should be created at the start of your project and maintained throughout, and include content that is appropriate to your project. Lastly, it's best to write your README in a non-proprietary format, like TXT or Markdown. 
{: .note}

# Congrats!
{: .no_toc }
*Hooray!* You are now ready to write up a good README file so you and other researchers can understand your project with no problems.
<br>

---


### Sources
{: .no_toc }
- UBC Library DataGuide. <https://bit.ly/3HtrzM8>
- Cornell University. Guide to writing "readme" style metadata. <https://bit.ly/2W4t9xa>
- The Graduate Institute Geneva. Readme.txt. <https://bit.ly/3aH6AUx>
- GitHub Basic Writing and Formatting Syntax. <https://bit.ly/2y7c4dZ>
- <https://pixabay.com>
- <https://www.pexels.com>

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
