---
layout: default
title: Ethics and Legal Compliance
parent: Data Management Plans
nav_order: 7
---


# Ethics and Legal Compliance
{: .no_toc}

Managing and sharing research data involves various **legal, ethical, and intellectual property issues** that need to be addressed and respected. These issues may include:
- the protection of personal information,
- the confidentiality of **sensitive data**, 
- the consent of data subjects, 
- the ownership of data, 
- the attribution of data sources, 
- the compliance with relevant laws and regulations, and more.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/follow-rule.jpg" width="300"/>
</p>

Researchers who manage and share their data should be aware of these issues and explain how they will <u>follow the appropriate guidelines and policies for their field and region</u>. 

They should also ensure that they comply with any applicable <u>privacy legislation and laws, including those imposed by their funders or institutions</u>. These may require researchers to obtain ethical approval, inform data subjects, anonymize or encrypt data, secure data storage and transfer, respect data licenses and agreements, and report any breaches or incidents.



<details open markdown="block">
  <summary>
    Table of Content
  </summary>
  {: .text-delta }
 - TOC
{:toc}
</details>


---



## Sensitive Data 

Sensitive data is data that should not be shared in the public domain without additional consideration. Our colleagues at the UBC Advanced Research Computing have an excellent <a href="https://arc.ubc.ca/sharing-research-data" target="_blank">guide</a> to sensitive data. This might include trade secrets, medical information, commercial information, preliminary analysis, third-party data, and some geospatially linked data. Sensitive research data requires careful handling and protection, and often is not suitable for open sharing. However, there may be ways to share sensitive research data legally and ethically, such as anonymizing, aggregating, or restricting access to the data.

<p style="margin-top:25px;margin-left:30px">
<img src="figures/privacy-please.jpg" width="300"/>
</p>

In order to ensure you are handling data in an ethical manner, you should:

- evaluate the anonymity of your data
- obtain a confidential review (from a data repository admin)
- comply with <a href="https://arc.ubc.ca/sharing-research-data" target="_blank">institutional regulations</a> (e.g. those of your institution's research ethics board)
- comply with other regulations (e.g. HIPAA, BREB)
- have informed consent for data sharing
- restrict use of confidential data

<br>

## De-identification
Sensitive data contain information that could reveal the identity or harm the interests of the people or entities involved in the research. To protect the privacy and confidentiality of the research subjects, researchers can use de-identification techniques. 

<p style="margin-top:25px;margin-bottom:25px">
<img src="figures/incognito.png" width="300"/>
</p>

**De-identification** is the process of removing or modifying any information that could be used to identify someone or something in a dataset. By doing this, researchers can **share their data without disclosing sensitive information**. However, de-identification is not a simple or foolproof solution. There is always a possibility that someone could re-identify the data by using other sources of information or advanced technology. Therefore, researchers need to be aware of the <u>risks and challenges</u> of de-identification and manage them accordingly.


There are different methods of de-identification, each with its own advantages and disadvantages. 

|Method of de-identification|Description|Pros &nbsp;<img src="figures/thumbs-up.png" align="center" width="23"/> |Cons &nbsp; <img src="figures/say-no.png" align="center" width="20">|
|-|-|-|-|
|**Anonymization**|the <u>most strict</u> form where all identifying information is <u>removed</u> from the dataset and cannot be restored. |ensures a high level of privacy protection|may reduce the usefulness and quality of the data|
|**Pseudonymization**|identifying information is replaced with <u>artificial identifiers</u>, such as codes or numbers|allows the data to be linked across different sources/datasets or over time|increases the risk of re-identification if the codes are exposed or cracked|
|**Aggregation**|individual data points are grouped together into <u>categories or ranges<u>|preserves some statistical properties and patterns|reduces the level of detail and variability in the data|
|**Masking**|identifying information is <u>hidden or obscured</u> by using techniques such as encryption, hashing, blurring, or noise addition|makes the data harder to read or interpret|introduces errors or distortions in the data|
|**Generalization**|identifying information is replaced with more <u>general or vague terms</u>. For example, dates can be replaced with years, addresses can be replaced with regions, or names can be replaced with initials|preserves some semantic meaning and context|makes the data less specific and more ambiguous|

<br>

### Risk of Re-identification

No matter what de-identification methods you choose to use, there is always a chance that someone could re-identify the data by using other sources of information or advanced technology. Therefore, researchers need to be aware of these risks and manage them accordingly.

#### Example: Anonymization

<p style="margin-top:10px"></p>

Consider this dataset that contains some identifiers:

|Name|Address|Postal code|Year of birth|Gender|Occupation|Salary|
|-|-|-|-|-|-|-|
|Sally Xi|123 City Roadway, Vancouver, BC|V5V 1P2|1970|Female|Manager|90,000|
|Sam Cooper|4576 Town Way, Smalltown, BC|V8A 1A5|1982|Male|Machinist|65,000|

An anonymized version of that dataset might look like this:

|Postal code|Year of birth|Gender|Occupation|Salary|
|-|-|-|-|-|
|V5V 1P2|1970|Female|Manager|90,000|
|V8A 1A5|1982|Male|Machinist|65,000|


In some cases, this might be enough to ensure that the data is not re-identified. However, the anonymized data may be easily re-identified in this case. For example, if there are not many machinists in the V8A 1A5 postal code, there is a strong risk of re-identification for the data related to Sam Cooper.

Reflection
{: .label label-blue }
    What method(s) would you use to protect the sensitive information of the individuals? 


<p style="margin-top:25px;margin-bottom:50px; margin-left:30px">
<img src="figures/facial-recognition.png" width="250"/>
</p>


#### Example: Pseudonymization

<p style="margin-top:10px"></p>

Data pseudonymization can preserve the linkability and utility of the data. **Linkability** means that the data can be connected to the same individual or entity across different datasets or over time. This can make the data more valuable for analysis and research, but it can also increase the risk of re-identification. Therefore, researchers need to assess the risk of re-identification and balance it with the benefit of data linkage.

On the other hand, data anonymization removes any information that can directly or indirectly identify an individual or an entity in a dataset. This means that the data cannot be linked to the original source or to other datasets. 

|Name|Anonymized|Pseudonymized|
|-|-|-|
Sally Xi | ANON | P12L25
Sam Cooper |	ANON	| P38Q27
Sunil Gupta |	ANON |	P59M16
Sam Cooper |	ANON |	P38Q27
Sally Xi |	ANON |	P12L25

<br>


### De-identification Tools

<p style="margin-top:25px;margin-bottom:50px; margin-left:30px">
<img src="figures/anonymity.png" width="230"/>
</p>

Researchers are increasingly using **algorithm-based tools** to help anonymize their data and manage the risk of re-identifying their anonymized data. An example of an anonymization tool would be:

- <a href="https://arx.deidentifier.org/" target="_blank">ARX open source data anonymization software</a>


<br>

## FIPPA
The <a href="https://universitycounsel.ubc.ca/subject-areas/access-and-privacy-general/access-to-information/about-fippa/" target="_blank"> FIPPA</a>, British Columbia Freedom of Information and Protection of Privacy Act, is provincial legislation that
- make public bodies more open and accountable by providing the public with a right of access to records; 
- protect personal information from unauthorized collection, use, or disclosure by public bodies.

<p style="margin-left:30px">
<img src="figures/regulations.jpg" width="300"/>
</p>

When it comes to choosing storage resources, researchers at UBC have a range of FIPPA-compliant options:

|Eligibility|FIPPA-Compliant Storage Resources|
|-|-|
|Faculty & Staff|OneDrive, Home Drives, TeamShare, Chinook, EduCloud|
|Students|OneDrive|


<br>

## TCPS 2 (2022)

The <a href="https://ethics.gc.ca/eng/policy-politique_tcps2-eptc2_2022.html" target="_blank">Tri-Council Policy Statement: Ethical Conduct for Research Involving Humans – TCPS 2 (2022)</a> is a policy document that provides <u>ethical guidelines and principles for conducting research</u> involving human participants in Canada. 

It was developed by the three federal research funding agencies: the Canadian Institutes of Health Research (CIHR), the Natural Sciences and Engineering Research Council of Canada (NSERC), and the Social Sciences and Humanities Research Council of Canada (SSHRC). The policy applies to all research involving human participants that is funded by these agencies or conducted under the auspices of institutions that receive agency funding.

Our colleagues at the <a href="https://ethics.research.ubc.ca/" target="_blank">UBC Office of Research Ethics</a> oversee the Behavioural and Clinical Research Ethics Boards, and are associated with the Ethics Board at UBC's Okanagan campus, as well as UBC's affiliated teaching hospitals. They provide outstanding support for UBC researchers and students and would be delighted to answer your specific questions. 
 
<br>

Reflection
{: .label label-green}
    Does your data comply with FIPPA requirements? 
    Does your data contain any sensitive or confidential information? 
    Does your data include any personal identifiers? 

    Reach out to research.data@ubc.ca or arc.support@ubc.ca to discuss sensitive data sharing.


---

Need help?
{: .label .label-blue }
  Please reach out to `research.data@ubc.ca` for assistance with any of your research data questions.
