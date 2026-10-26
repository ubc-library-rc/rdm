---
layout: default
title: Basic Deposit
parent: Deposit in UBC Borealis
nav_order: 1
---

# Basic Deposit in UBC Borealis
{: .no_toc }

<p style="margin-bottom: 15px"></p>

<a href="https://borealisdata.ca/dataverse/ubc" target="_blank"><b>UBC Borealis</b> </a>is a cross-disciplinary research data collection. Datasets in Borealis are discoverable by Google, Google Data, Google Scholar, US National Library of Medicine, UBC Library Summon, Lunaris, DataOne, DataCite, and much more. It is an open-source application to publish, share, reference, cite, extract and analyze research data.

<p style="margin-top:25px;margin-left:30px;margin-bottom:25px"></p>

<details open markdown="block">
  <summary>
    Table of Contents
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

Looking for a cheat sheet? Check out our <a href="https://osf.io/sczv5" target="_blank">one-pager</a>! Need help? Please reach out to `research.data@ubc.ca` for assistance with any of the deposit steps below.
{: .note } 




---


# How to deposit in UBC Borealis?
{: .no_toc}

<p style="margin-bottom: 25px"></p>

The following step-by-step instructions will allow you to practice depositing data in a **Demo** UBC Borealis instance. To deposit your actual datasets, visit `https://borealisdata.ca`.
{: .warn }

## Practice Dataset
{: .no_toc}

<p style="margin-bottom: 10px"></p>

Title
{: .label .label-green}

UBC Farm Monthly Bird Surveys

Author(s)
{: .label .label-green}

Nature Vancouver

Abstract
{: .label .label-green}

Nature Vancouver, a not-for-profit charitable society based in Vancouver, BC, has conducted monthly bird surveys at UBC Farm since March 2007, in part to record the seasonal bird species over the year in nine different habitat areas of the Farm. Surveys occur on the third Sunday of the month starting at 8am (March to September) or 9am (October to February) and typically last two to three hours. Bird occurrences are recorded by genus and species, or when identification is not clear, then simply to genus. The nine stations of the farm include the market garden fields, the herb and flower gardens, the biodiversity hedgerows, and the forested portion of the farm.


Click to download the files
{: .label .label-green}

- <a download href="exercise_files\NatureVancouverBirdRecords.csv" target="_blank"> The data file</a>

- <a download href="exercise_files\NatureVancouverMonthlyBirdSurveys_Metadata.pdf" target="_blank"> The metadata/data dictionary file</a>

<p style="margin-top:25px; margin-left:30px">
<img src="figures/bird.jpg" width="300"/></p>


<br>

## *1*{: .circle .circle-blue} &nbsp;Create Account

1. Go to <a href="https://demo.borealisdata.ca/dataverse/ubc" target="_blank">the Borealis **Demo** </a> > Login (at top right)
2. Locate UBC and use your CWL to create an account. You will be redirected to <b>UBC Borealis</b>.

## *2*{: .circle .circle-red} &nbsp;Create Dataset

<p style="margin-bottom: 10px"></p>

### 1. Choose the dataverse (AKA "collection") you want to deposit data into.
{: .no_toc }

- Choose "Research Commons Workshops Dataverse" for this exercise

- You can find dataverses by going to "My Data" or "Dataverses" 
<p style="margin-bottom:25px; margin-left:30px">
<img src="figures/borealis-find-dataverse.png" width="500"/></p>

<p style="margin-bottom: 30px"></p>

### 2. Create a new dataset
{: .no_toc }

<p style="margin-bottom: 10px"></p>

- Choose `+Add Data` then `New Dataset` (not `New Dataverse`) from the dropdown menu

- Select a <b>dataset template</b> for the desired <a href="https://copyright.ubc.ca/creative-commons/" target="_blank">Creative Commons license</a> (default license is CC-BY). If you change the selected template, then all other data fields will clear, so do this first.
  - You can learn more about data licensing in the [Licenses for Research Data workshop](https://ubc-library-rc.github.io/rdm/content/09_License-Research-Data.html) and the [Advanced Deposit workshop](https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit#licenses-and-terms). 

- Fill in <b>required metadata</b> fields marked with a <a style="font-size:22px; color:red">*</a>.

If desired, fill in additional metadata fields. *Recommended: Keywords, Related Publications*. Many more metadata fields become available for editing after your dataset is saved.
{: .note }

- Click `Save Changes` button. This saves the dataset in **Draft** form; it is **not yet published** nor publicly visible. You can save the dataset without uploading files. 


<p style="margin-bottom: 30px"></p>

### 3. Upload data files
{: .no_toc }

<p style="margin-bottom: 10px"></p>

The Files section is at the bottom of the page. Here, you can upload or drag and drop files.
<p style="margin-bottom:25px; margin-left:30px">
<img src="figures/dataset_file_upload.png" width="500"/></p>

<b>Max file size: 5GB</b>. If your files are too large, try putting them into a Zip file(s), or contact `research.data@ubc.ca` for help.

By default, the software will unzip your directory upon upload. If you want to preserve the directory structure, you can <b>double-zip</b> it before uploading.
{: .note }

You can also describe the files with a description, title, and tags to help people understand the purpose of those files.


## *3*{: .circle .circle-yellow} &nbsp;Submit or Publish Dataset

Click `Submit for Review` for the data curator to review your draft and publish your edits.

Once a dataset is published, a **DOI** is assigned by Borealis to permanently identify the dataset.  

A **[Preview URL](https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit.html#2-preview-url)** can also be assigned to share with a journal and/or peer reviewers without publishing the data. 

<p style="margin-top:25px; margin-left:30px">
<img src="figures/publish.jpg" width="300"/></p>


## *4*{: .circle .circle-purple} &nbsp;Edit Dataset  

- You can edit elements of your dataset at any time using the `Files`, `Metadata`, and `Terms` (license and use permissions) tabs at the bottom of the page. 
  
- Files can be `Restricted` or `Embargoed` so they are available only on request. You can learn more about data access restrictions in the <a href="https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit" target="_blank">Advanced Deposit workshop</a>.

- Changes made to Files, Metadata, or Terms <b>after publishing</b> your dataset will be saved as a Draft version. Click `Submit for Review` to make the changes go live; the new version will supersede the old version.


Admin assistance is needed to deaccession a dataset, so triple-check before publishing your data. The DOI cannot be deleted. 
{: .warn }


## *5*{: .circle .circle-green} &nbsp;Cite Dataset

<p style="margin-bottom: 10px"></p>

- The data citation is generated by Borealis based on the required metadata you entered. It’s displayed in a blue box below the dataset title and version #. 

- Copy and paste, or use the `Cite Dataset` button to export the citation into EndNote, RIS, or Bibtex.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/borealis-cite-dataset.png" width="500"/> </p> 


<br>



# Congrats!
{: .no_toc }

Now you know how to deposit your dataset in a **Demo** UBC Borealis! You are ready to go live at <https://borealisdata.ca>! 

<p style="margin-bottom:25px;margin-left:30px">
<img src="figures/thumb-success.jpg" width="150"/>
</p>


---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.

