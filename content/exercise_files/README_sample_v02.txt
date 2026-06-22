<Please note the content of this sample README file was fabricated for educational purposes and does not reflect the real project's objectives. This sample demonstrates a README example containing the minimum requirements, along with additional metadata to enhance the README file.>




This README file was generated on 2024-10-10 by Matthew Davis and updated on 2026-06-17 by Matthew Davis. 

TITLE OF DATASET: Soil Adsorption Curves and Environmental Soil Data

DESCRIPTION/SUMMARY
Ammonium in soil pore water is thought to participate in bidirectional exchange with the atmosphere; however, common soil nutrient analysis methods determine the bulk quantity of ammonium associated with the soil particles rather than determining the aqueous ammonium concentration. Previous works have applied the Langmuir and Freundlich isotherm equations to ammonium-enriched soils to estimate partitioning, but this may not be representative of conditions in natural, unmanaged soils. 

This dataset contains the data and code to reproduce the results from chapters 4 to 5 of Matthew Davis's thesis (2024): Evaluating adsorption isotherm models for determining the partitioning of ammonium between soil and soil pore water in environmental soil samples.


RESEARCH METHODOLOGY 
Environmental soil samples were collected from green spaces in Toronto and used to evaluate several commonly used adsorption isotherm equations, including the Langmuir, Freundlich, Temkin and Toth equations, to determine their applicability in lightly managed and non-fertilized soils. We then compare ammonia emission potentials (a quantity predicting the propensity of ammonia to volatilize from a liquid reservoir) determined using a conventional high-salt extraction procedure to determine the soil ammonium content to that modelled using the Temkin and Langmuir equations and demonstrate that conventional approaches may overestimate emission potentials from soils by a factor of 5–20.


SOFTWARE/TOOLS USED
- R version 4.4.2
- R packages used: tidyverse, openair, leaflet, openxlsx


DOI/PERSISTENT IDENTIFIERS
Hyperlinked DOI for this dataset: https://doi.org/10.5683/SP3/JGRIN0


LICENSE INFORMATION 
The terms under which this dataset may be used follows the CC BY-SA 4.0 license. 


AUTHOR/CREATOR INFORMATION 
Position: Author
Name: Matthew Davis
ORCID: 0000-0002-0699-7038
Institution: University of Toronto
Address: https://sites.chem.utoronto.ca/murphygroup/content/matthew-davis
Email: m.davis@utoronto.ca

Position: Principal investigator, corresponding author
Name: Jennifer Murphy
ORCID:
Institution: University of Toronto
Address: https://sites.chem.utoronto.ca/murphygroup/pi
Email: jen.murphy@utoronto.ca

Position: Author
Name: Kevin Yan
ORCID:
Institution: University of Toronto
Address: https://sites.chem.utoronto.ca/murphygroup/content/kevin-yan
Email: k.yan@utoronto.ca

All experimental results can be reproduced using the code and data in this repository. Feel free to contact Jennifer Murphy (corresponding author) by email at jen.murphy@utoronto.ca if you have any questions about our work. 


RELATED PUBLICATIONS
Journal article citation for this dataset: Davis, M. G., Yan, K., and Murphy, J. G. Evaluating adsorption isotherm models for determining the partitioning of ammonium between soil and soil pore water in environmental soil samples, Biogeosciences, 21, 5381–5392, https://doi.org/10.5194/bg-21-5381-2024, 2024.

Citation for Matthew Davis's thesis:  Davis, M. G. (2024). An investigation of local and regionally significant non-agricultural sources of ammonia in Toronto and the Great Lakes Region. [Doctoral dissertation, University of Toronto]. University of Toronto TSpace. http://hdl.handle.net/1807/140872 



FILE LIST/DIRECTORY
- `src/` contains source code for the adsorption curves and environmental soils analysis. This contains Rmd files to generate the models and plots in the paper.
- `data/` contains all the data used in this project. This subdirectory contains a data dictionary. 



ACKNOWLEDGEMENTS 
We thank our colleagues Myrna Simpson and Jenny Oh (University of Toronto) for their helpful discussions. We also thank the University of Toronto ANALEST facility staff for their technical assistance.

This research has been supported by the Natural Science and Engineering Research Council (NSERC) Discovery grant (grant no. RGPIN-2022-05241) and a grants and contributions agreement GCXE19S016 with Environment and Climate Change Canada held by Jennifer Murphy. Matthew Davis held a Walter C. Sumner Memorial Fellowship while conducting this research. An undergraduate summer research award from NSERC supported Kevin Yan during this work.

