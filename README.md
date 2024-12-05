# Investigation of Correlation between Weather Events and Car Accidents In Iowa

## Archival Record
Link to archival record: []()

## Contributors
Vitalijs Kurjanovics Kravcenko, Benjamin Leidig, Ryan Sponzilli

## Summary
WRITE SUMMARY HERE

## Data Profile

### National Centers for Environmental Information (NCEI)
License: Creative Commons CC0 1.0 Universal (CC0)

Available at: [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000)

Imported data is from time range year 1895 to 2024. Dataset includes columns: `Date`, `Value`, `Anomaly`. Column `Date` contains the date of record in the format *YYYYMM*. Column `Value` contains the total precipitation amount for the respective date in column `Date`. Column `Anomaly` contains the anomaly for the respective date in column `Date` and is not used in the this analysis.

### Iowa Open Data
License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Terms of Use according to dataset website: "See license."

Available at: [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data)

Imported data was limited to 583174 rows (from year 2009 to 2024). 


Both datasets are downloaded in CSV format. Modifications have been made to integrate and preprocess the data for analysis. Use of the data must comply with the respective licenses. 

## Findings

Link to results: [https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr](https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr)

## Reproducing

### Requirements
All packages, software dependencies, and the programming environment as well as their versions are specified in `doc/requirements.txt` and `doc/environment.md` and must be intalled before workflow execution.

### Code Notations
Each `.py` file in folder, `src`, has a respective `.ipynb` file in folder, `doc/code_notations`, that contains replica code and respective notations organizing and describe code processes. (`.ipynb` files are not intended to be run and are for notation purposes only.)

### Data Acquisition
The *NCEI* dataset is collected via a URL link. The *Iowa Open Data* dataset is collected via an API query. Both of these processes are included in the workflow as well as their respective integrity checks in the rule, `acquisition`.

### Running the Workflow
All code in pure python is included in the folder, `src`, as `.py` files. This is the code used to run the workflow file, `Snakefile`. The `Snakefile` creates five rules: `runall`, `acquisition`, `integration`, `analysis`, and `modeling`.

- Rule `runall` executes all processes necessary to produce `heatmap.png`, `lineplot.png`, `lmplot.png`, `pairplot.png`, and `regression-output.md`.
- Rule `acquisition` takes `src/checksums/checksums.txt` as input and, using `src/acquisition.py`, uses links and API queries to fetch and integrity check all raw datasets and saves them to `data/raw`. (The Iowa Open Data dataset is saved as three separate *.csv* files to avoid usage of GitHub Large File Storage.)
- Rule `integration` takes all raw *.csv* files as input and, using `src/integration.py`, integrates the raw datasets into the processed, final dataset, `data/processed/integrated.csv`.
- Rule `analysis` takes `data/processed/integrated.csv` as input and, using `src/analysis.py`, creates graphs and analyzes the processed dataset. Rule `modeling` takes `data/processed/integrated.csv` as input and, using `src/modeling.py`, finds the best model.

**To execute the workflow, the line:**

```
snakemake --latency-wait 300
```

**must be run in the terminal while in the `/src` directory.**

## References

### Dataset Citations
NOAA National Centers for Environmental information, Climate at a Glance: Statewide Time Series, published November 2024, retrieved on December 5, 2024 from [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series)

Iowa Department of Transportation, Motor Vehicle Division: Vehicle Crashes in Iowa, published July 2022, retrieved on December 5, 2024, from [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data)

Use of the datasets must comply with the respective licenses.

### Software Citations
For dependencies, see `doc/requirements.txt`. Use of the software must comply with the respective licenses.

### Software Created:
Licensed under the MIT License. See `LICENSE.txt` for details.