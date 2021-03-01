# Python_scripts

A few python scripts for metabolomics.


## FBMN - Filter MGF from MZmine
The script takes a input feature quantification table and MGF file from [feature-based molecular networking (FBMN)](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking/) and output a filtered MGF with spectra for only the feature IDs present in the feature quantification table. These files can then be used to generate a FBMN that was prefiltered. 

Interative notebook here -> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/helenamrusso/Python_scripts/main?urlpath=lab/tree/FBMN_filter_mgf_MZmine.ipynb)

The script: `filter_mgf_MZmine.py`
