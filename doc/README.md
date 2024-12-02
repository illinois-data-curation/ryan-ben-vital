# README

## Overview

### Requirements
All packages and software dependencies as well as their versionss are specified in `requirements.txt` are must be intalled before workflow execution.

### Code Notations
Each `.py` file in folder, `../src`, has a respective `.ipynb` file in folder, `code_notations`, that contains replica code and respective notations organizing and describe code processes. (`.ipynb` files are not intended to be run and are for notation purposes only.)

### Data Acquisition
The *NCEI* dataset is collected via a URL link. The *data.iowa.gov* dataset is collected via an API query. Both of these processes are included in the workflow as well as their respective integrity checks in the rule, `acquisition`.

### Workflow
All code in pure python is included in `..src` as `.py` files. This is the code used to run the workflow file, `Snakefile`. The `Snakefile` creates five rules: `runall`, `acquisition`, `integration`, `analysis`, and `modeling`.

- Rule `runall` *****.
- Rule `acquisition` takes `../src/checksums.txt` as input and, using `../src/acquisition.py`, uses links and API queries to fetch and integrity check all raw datasets and saves them to `../data/raw`. (The Iowa dataset is saved as three separate *.csv* files to avoid usage of GitHub Large File Storage.)
- Rule `integration` takes all raw *.csv* files as input and, using `../src/integration.py`, integrates the raw datasets into the processed, final dataset, `../data/processed/integrated.csv`.
- Rule `analysis` takes `../data/processed/integrated.csv` as input and, using `../src/analysis.py`, creates graphs and analyzes the processed dataset. Rule `modeling` takes `../data/processed/integrated.csv` as input and, using `../src/modeling.py`, finds the best model.

To execute the workflow, the line:

```
--latency-wait 300
```

must be run in the terminal while in the `/src` directory.

## Licenses

### Datasets Used:
NCEI Dataset:
- Creative Commons CC0 1.0 Universal (CC0)
- URL: [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000)

Iowa Open Data Dataset:
- Creative Commons Attribution 4.0 International (CC BY 4.0)
- URL: [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data]((https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data))

### Datasets Created:


### Software Created: