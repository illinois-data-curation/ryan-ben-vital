# Investigation of Correlation between Weather Events and Car Accidents In Iowa

## Archival Record
Link to archival record: [https://doi.org/10.5281/zenodo.14285990](https://doi.org/10.5281/zenodo.14285990)

## Contributors
Vitalijs Kurjanovics Kravcenko, Benjamin Leidig, Ryan Sponzilli

## Summary
The overall goal of this project is to explore a correlation phenomenon between the number of car accidents and amount of precipitation per month within Iowa, using data from a 2009-2024 timeframe. We combined data from these two domains to successfully communicate our findings through intuitive visualizations and a linear regression model. The precipitation data was drawn from National Oceanic and Atmospheric Administration (NOAA), whilst the car accident data was made available by Iowa’s Open Data Platform. The precipitation data and car accident metrics were integrated together for analysis. After data profiling, quality assessment, and cleaning, we moved on to exploratory data analysis, visualizations, and modeling. The people who would benefit from this analysis are urban planners, emergency response services, and climate change researchers. Potential societal impacts of this analysis are more general awareness of the need for safe driving practices, especially during increased precipitation.


## Data Profile

### National Centers for Environmental Information (NCEI)
License: Creative Commons CC0 1.0 Universal (CC0)

Available at: [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000)

Imported data is from time range year 1895 to 2024. Dataset includes columns: `Date`, `Value`, `Anomaly`. Column `Date` contains the date of record in the format *YYYYMM*. Column `Value` contains the total precipitation amount for the respective date in column `Date`. Column `Anomaly` contains the anomaly for the respective date in column `Date` and is not used in the analysis or model. The dataset was refined to years 2014 to 2024. Included below is every dataset column and respective description from the dataset website:

| Column Name | Description                                               | Data Type |
|-------------|-----------------------------------------------------------|-----------|
| `Date`      | The date of record in the format *YYYYMM*.                | Number    |
| `Value`     | The total precipitation amount for the respective date.   | Number    |
| `Anomaly`   | The anomaly for the respective date.                      | Number    |

### Iowa Open Data
License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Terms of Use according to dataset website: "See license."

Available at: [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data)

Imported data was limited to 583174 rows (from year 2009 to 2024). Columns  `Year`, `Environmental Conditions`, `Surface Conditions`, `Weather Condition`, `Crash Severity`, `Number of Fatalities`, `Number of Injuries`, `Number of Major Injuries`, `Number of Minor Injuries`, `Number of Possible Injuries`, `Number of Unknown Injuries`, and `Amount of Property Damage` are used in the integrated dataset. The dataset was refined to the time range of years 2014 to 2024. Included below is every dataset column and respective description from the dataset website:

| Column Name                          | Description                                                                                                                                                            | Data Type           |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| `Iowa DOT Case Number`               | Case number assigned by the DOT. 4 digit year + number assigned by the Motor Vehicle Division (e.g., 2001002534).                                                      | Number              |
| `Law Enforcement Case Number`        | The case number as assigned by the law enforcement agency.                                                                                                             | Text                |
| `Date of Crash`                      | Date of the crash.                                                                                                                                                     | Floating Timestamp  |
| `Month of Crash`                     | The month of year the crash occurred.                                                                                                                                  | Text                |
| `Day of Week`                        | The day of week the crash occurred.                                                                                                                                   | Text                |
| `Time of Crash`                      | The time of day the crash occurred in 24 hour format.                                                                                                                 | Text                |
| `Hour`                               | Hour of day the crash occurred derived from Time of Crash. 0000 Hours is from midnight to 1:00 AM.                                                                     | Text                |
| `DOT District`                       | The DOT district where the crash occurred derived from the county.                                                                                                    | Text                |
| `City Name`                          | Name of city where the crash was located where available or applicable.                                                                                               | Text                |
| `County Name`                        | Name of county where the crash was located where available.                                                                                                           | Text                |
| `Route with System`                  | Route with System where applicable.                                                                                                                                   | Text                |
| `Location Description`               | Description for the location of the crash.                                                                                                                            | Text                |
| `First Harmful Event`                | First harmful event contributing to the crash.                                                                                                                        | Text                |
| `Location of First Harmful Event`    | The location of the first harmful event relative to the roadway.                                                                                                      | Text                |
| `Manner of Crash/Collision`          | Description of the manner of the crash/collision.                                                                                                                     | Text                |
| `Major Cause`                        | Categorizes the major cause contributing to the crash.                                                                                                                | Text                |
| `Drug or Alcohol`                    | Indicates whether drugs or alcohol were a factor in the crash. Derived from Alcohol results, Drug results, and driver conditions.                                      | Text                |
| `Environmental Conditions`           | Highlights conditions in the environment that may have contributed to the crash.                                                                                      | Text                |
| `Light Conditions`                   | Describes light conditions at the time of the crash.                                                                                                                  | Text                |
| `Surface Conditions`                 | Describes surface conditions crash-wide.                                                                                                                              | Text                |
| `Weather Conditions`                 | Describes weather conditions at time of the crash.                                                                                                                    | Text                |
| `Roadway Contribution`               | Describes the roadway contributing circumstances.                                                                                                                     | Text                |
| `Roadway Type`                       | Describes the type of roadway junction or feature at location of the crash.                                                                                           | Text                |
| `Roadway Surface`                    | Indicates whether the roadway surface was paved or unpaved.                                                                                                           | Text                |
| `Work Zone`                          | Indicates whether the crash occurred within a construction work zone.                                                                                                 | Text                |
| `Crash Severity`                     | Indicates the severity of the crash based on fatalities, injuries, or property damage.                                                                                | Text                |
| `Number of Fatalities`               | Crash-wide total of all fatalities.                                                                                                                                   | Number              |
| `Number of Injuries`                 | Crash-wide total of all injuries.                                                                                                                                     | Number              |
| `Number of Major Injuries`           | Crash-wide total of all major injuries. Major injuries are generally incapacitating injuries, other than fatal, that prevent the injured individual from continuing normal activities. | Number |
| `Number of Minor Injuries`           | Crash-wide total of all minor injuries. Minor injuries are generally non-incapacitating injuries, evident to observers at the scene of the accident.                  | Number              |
| `Number of Possible Injuries`        | Crash-wide total of all possible injuries, excluding fatal, major, or minor injuries, where there is a complaint of pain or injury.                                    | Number              |
| `Number of Unknown Injuries`         | Crash-wide total of all unknown injuries.                                                                                                                             | Number              |
| `Amount of Property Damage`          | Crash-wide total of property damage, including non-vehicular.                                                                                                         | Number              |
| `Amount of Vehicles Involved`        | Total number of vehicles involved in the crash.                                                                                                                       | Number              |
| `Total Number of Occupants`          | Crash-wide total of occupants in all vehicles. Value "777" is unknown, unreported, or unavailable.                                                                    | Number              |
| `Travel Direction`                   | Cardinal direction of vehicles on primary roads (derived).                                                                                                            | Text                |
| `Location`                           | Point location for the site of the crash.                                                                                                                             | Point               |

Both datasets are downloaded in CSV format. Modifications have been made to integrate and preprocess the data for analysis. Use of the data must comply with the respective licenses. 

## Findings

Link to our results: [https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr](https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr)

After wrangling our data together from our two sources into a single csv file, we began with some exploratory data analysis. Our results consist of four different data visualizations and one linear regression equation. The first visualization is a pair plot that shows `precipitation` plotted against the other nine variables. From these plots we can see that precipitation exhibits a strong positive relationship with `count`, `possinjury`, `mininjury`, and `propdmg`, a weak positive relationship with `uninjury`, `majinjury`, and `fatalities`, and a strong negative relationship with `year`. This suggests that more precipitation results in more minor car accidents than more major car accidents. The second visualization is a heatmap and we have highlighted the row/column of the `precipitation` variable to draw attention to it. This heatmap essentially depicts the same observations that we saw in the pair plot, but in the form of correlation coefficients. The third visualization is a line plot with `count` (number of accidents), and `precipitation` overlayed on the same graph. In this graph we can see that prior to 2017 the two factors don't trend together, but after 2017 they both trend downward together. The fourth visualization is a linear model plot (lmplot). In this visualization look again at the strong positive relationship between `count` and `precipitation`. There is one major outlier, but the rest of the data points are fairly tight to the line of best fit. The other result that we produced is the following linear regression equation: $\widehat{count} = 196.37210083007812 \cdot precipitation + 1943.09619140625$. It shows that on average, for every additional inch of precipitation per year, we can expect 196 additional car accidents to occur. Overall, our findings indicate that a relationship does exist between precipitation and car accidents, specifically in Iowa.


## Future Work

WRITE ME

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