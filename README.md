# Python_scripts

A few python scripts for metabolomics.


## FBMN - Filter MGF from MZmine
The script takes as input a list of features to be deleted and the MGF file from [feature-based molecular networking (FBMN)](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking/). As output, a filtered MGF with spectra for only the feature IDs of interest is generated. This file can then be used to generate a FBMN that was prefiltered. 

NOTE: It is important to also filter the Feature Table (.csv file) exported from MZmine, so that the features in both files match.


Interative notebook here -> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/helenamrusso/Python_scripts/main?urlpath=lab/tree/FBMN_filter_mgf_MZmine.ipynb)

The script: `filter_mgf_MZmine.py`
