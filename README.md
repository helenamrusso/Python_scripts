# Python_scripts

A few python scripts for metabolomics.


## FBMN - Filter MGF from MZmine
The script takes as input a list of features to be deleted and the MGF file from [feature-based molecular networking (FBMN)](https://ccms-ucsd.github.io/GNPSDocumentation/featurebasedmolecularnetworking/). As output, a filtered MGF with spectra for only the feature IDs of interest is generated. This file can then be used to generate a FBMN that was prefiltered. 

NOTE: It is important to also filter the Feature Table (.csv file) exported from MZmine, so that the features in both files match.


Interative notebook here -> [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/helenamrusso/Python_scripts/main?urlpath=lab/tree/FBMN_filter_mgf_MZmine.ipynb)

The script: `filter_mgf_MZmine.py`


## FBMN - Filter MGF from MZmine
This script takes as input the sirius.mgf file exported from MZmine3, which contains SPECTYPE=CORRELATED MS for some MS1 - this causes an error in Qemistree when converting the mgf file to qza (Feature "1" has more than one MSLEVEL=1 record).
As output, a new sirius.mgf file is generated, in which the SPECTYPE=CORRELATED MS are removed.

The script: `SIRIUS export MZmine3_SPECTYPE removal.ipynb`
