# **README**

## Overview

### Requirements
All packages and software dependencies as well as their versionss are specified in `doc/requirements.txt` are must be intalled before workflow execution.

### Code Notations
Each `.py` file in folder, `src`, has a respective `.ipynb` file in folder, `doc/code_notations`, that contains replica code and respective notations organizing and describe code processes. (`.ipynb` files are not intended to be run and are for notation purposes only.)

### Data Acquisition
The *NCEI* dataset is collected via a URL link. The *Iowa Open Data* dataset is collected via an API query. Both of these processes are included in the workflow as well as their respective integrity checks in the rule, `acquisition`.

### Workflow
All code in pure python is included in the folder, `src`, as `.py` files. This is the code used to run the workflow file, `Snakefile`. The `Snakefile` creates five rules: `runall`, `acquisition`, `integration`, `analysis`, and `modeling`.

- Rule `runall` executes all processes necessary to produce `heatmap.png`, `lineplot.png`, `lmplot.png`, `pairplot.png`, and `regression-output.md`.
- Rule `acquisition` takes `src/checksums/checksums.txt` as input and, using `src/acquisition.py`, uses links and API queries to fetch and integrity check all raw datasets and saves them to `data/raw`. (The Iowa Open Data dataset is saved as three separate *.csv* files to avoid usage of GitHub Large File Storage.)
- Rule `integration` takes all raw *.csv* files as input and, using `src/integration.py`, integrates the raw datasets into the processed, final dataset, `data/processed/integrated.csv`.
- Rule `analysis` takes `data/processed/integrated.csv` as input and, using `src/analysis.py`, creates graphs and analyzes the processed dataset. Rule `modeling` takes `data/processed/integrated.csv` as input and, using `src/modeling.py`, finds the best model.

To execute the workflow, the line:

```
snakemake --latency-wait 300
```

must be run in the terminal while in the `/src` directory.

## Licenses

### Dataset Created (`data/processed/integrated.csv`)
This dataset was derived from:

- National Centers for Environmental Information (NCEI) data, Creative Commons CC0 1.0 Universal (CC0), available at [https://www.ncei.noaa.gov](https://www.ncei.noaa.gov).
- Iowa Open Data, Creative Commons Attribution 4.0 International (CC BY 4.0), available at [https://data.iowa.gov](https://data.iowa.gov).

Modifications have been made to integrate and preprocess the data for analysis. Use of the data must comply with the respective licenses.

### Software Created:
Licensed under the MIT License. See `LICENSE.txt` for details.
