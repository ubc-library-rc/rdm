---
layout: default
title: Basic Deposit
parent: Deposit in UBC Dataverse Collection
nav_order: 1
---

# Basic Deposit in UBC Dataverse Collection
{: .no_toc }

<p style="margin-bottom: 15px"></p>

<a href="https://borealisdata.ca/dataverse/ubc" target="_blank"><b>UBC Dataverse Collection</b> </a>is a cross-disciplinary research data collection on Borealis. Datasets in Borealis are discoverable by Google, Google Data, Google Scholar, US National Library of Medicine, UBC Library Summon, Lunaris, DataOne, DataCite, and much more. It is an open-source application to publish, share, reference, cite, extract and analyze research data.

<p style="margin-top:25px;margin-left:30px;margin-bottom:25px"></p>

<details open markdown="block">
  <summary>
    How to deposit in UBC Dataverse Collection?
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>

Looking for a cheat sheet? Check out our <a href="https://osf.io/sczv5" target="_blank">one-pager</a>! Need help? Please reach out to `research.data@ubc.ca` for assistance with any of the deposit steps below.
{: .note } 




---


# How to deposit in UBC Dataverse Collection?
{: .no_toc}

<p style="margin-bottom: 25px"></p>

The following step-by-step instructions will allow you to practice depositing data in a **Demo** UBC Dataverse instance. To deposit your actual datasets, visit `https://borealisdata.ca`.
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


Click to Download the Files
{: .label .label-green}

- <a download href="exercise_files\NatureVancouverBirdRecords.csv" target="_blank"> The Data file</a>

- <a download href="exercise_files\NatureVancouverMonthlyBirdSurveys_Metadata.pdf" target="_blank"> The metadata/data dictionary file</a>

<p style="margin-top:25px; margin-left:30px">
<img src="figures/bird.jpg" width="300"/></p>


<br>

## *1*{: .circle .circle-blue} &nbsp;Create Account

1. Go to <a href="https://demo.borealisdata.ca/dataverse/ubc" target="_blank">the Borealis **Demo** </a> > Login (at top right)
2. Locate UBC and use your CWL to create an account. You will be redirected to the <b>UBC Dataverse Collection</b>.

<br>

## *2*{: .circle .circle-red} &nbsp;Create Dataset

<p style="margin-bottom: 10px"></p>

### 1. Choose the dataverse you want to deposit data into.
{: .no_toc }


- <p style="font-size:17px; color:purple">Choose "Research Commons Workshops Dataverse" for this exercise </p> 
  
  
- You can find dataverses via: 
<p style="margin-bottom:25px; margin-left:30px">
<img src="figures/borealis-find-dataverse.png" width="500"/></p>


<p style="margin-bottom: 30px"></p>







### 2. Create a new dataset
{: .no_toc }

<p style="margin-bottom: 10px"></p>

- Choose `+Add Data` > `New Dataset` (not New Dataverse) from the dropdown menu

- Select a <b>dataset template</b> for the desired <a href="https://copyright.ubc.ca/creative-commons/" target="_blank">Creative Commons license</a> (default license is CC0). You can learn more about data licensing in the <a href="https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit" target="_blank">Advanced Deposit workshop</a>. Selecting a template will clear all other data fields, so do this first.


- Fill in <b>required metadata</b> fields marked with a <a style="font-size:22px; color:red">*</a>.

If desired, fill in additional metadata fields. *Recommended: Keywords, Related Publications*. Many more metadata fields become available for editing after your dataset is saved.
{: .note }

- Click `Save Changes` button. This saves the dataset in **Draft** form; it is **not yet published** nor publicly visible. You can save the dataset without uploading files. 


<p style="margin-bottom: 30px"></p>





### 3. Upload data files
{: .no_toc }

<p style="margin-bottom: 10px"></p>

The Files section is at the bottom of the page. 

You can upload files now:
<p style="margin-bottom:25px; margin-left:30px">
<img src="figures/dataset_file_upload.png" width="500"/></p>

<b>Max file size: 5Gb</b>. If your files are too large, try putting them into a Zip file(s), or contact `research.data@ubc.ca` for help.

By default, the software will unzip your directory upon upload. If you want to preserve the directory structure, you can <b>double-zip</b> that directory before uploading.
{: .note }

<b>Describe the files</b>: Title, Description, Tags. Remember that people can’t use your data if they don’t know what it is!



<br>



## *3*{: .circle .circle-yellow} &nbsp;Submit or Publish Dataset


Depending on your user permissions, you will have a button for either:
- `Submit for Review` (the draft dataset is reviewed by a research data administrator)
- `Publish` (makes the dataset publicly available)

Once a dataset is published, Dataverse assigns a **DOI** to permanently identify the dataset.  

We can also assign a **[Preview URL](https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit.html#2-preview-url)** to share with a journal and/or peer reviewers without publishing the data. 

<p style="margin-top:25px; margin-left:30px">
<img src="figures/publish.jpg" width="300"/></p>



<br>



## *4*{: .circle .circle-purple} &nbsp;Edit Dataset  

- You can edit elements of your dataset at any time using the `Files`, `Metadata`, and `Terms` (license and use permissions) tabs at the bottom of the page. 
  
- Files can be `Restricted` or `Embargoed` so they are available only on request. You can learn more about data access restrictions in the <a href="https://ubc-library-rc.github.io/rdm/content/05-2_Advanced_Deposit" target="_blank">Advanced Deposit workshop</a>.

- Changes made to Files, Metadata, or Terms <b>after publishing</b> your dataset will be saved as a Draft version. Click `Submit for Review` or `Publish` again to make the changes go live; the new version will supersede the old.


Admin assistance is needed to deaccession a dataset, so triple-check before Publishing your data. The DOI cannot be deleted. 
{: .warn }


<br>


## *5*{: .circle .circle-green} &nbsp;Cite Dataset

<p style="margin-bottom: 10px"></p>

- The data citation is generated by Borealis based on the required metadata you entered. It’s displayed in a blue box below the dataset title and version #. 

- Copy and paste, or use the `Cite Dataset` button to export the citation into EndNote, RIS, or Bibtex.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/borealis-cite-dataset.png" width="500"/> </p> 


<br>



# Congrats!
{: .no_toc }

Now you know how to deposit your dataset in a **Demo** UBC Dataverse Collection! You are ready to go live at <https://borealisdata.ca>! 

<p style="margin-bottom:25px;margin-left:30px">
<img src="figures/thumb-success.jpg" width="150"/>
</p>
  

Want to learn more details about data deposits in the UBC Dataverse collection? You are qualified for the [Advanced Deposit workshop](05-2_Advanced_Deposit.md) now!

---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.

