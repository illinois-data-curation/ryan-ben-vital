# Investigation of Correlation between Weather Events and Car Accidents In Iowa


## Archival Record
Link to archival record: [https://doi.org/10.5281/zenodo.14285990](https://doi.org/10.5281/zenodo.14285990)


## Contributors
Vitalijs Kurjanovics Kravcenko, Benjamin Leidig, Ryan Sponzilli


## Summary
The overall goal of the project was to explore a potential correlational relationship between the number of car accidents and the amount of precipitation by month within the state of Iowa. Two datasets were used from online sources for this project. Both sources are outlined in full detail under the Data Profile and References. The source datasets include observations from the years 1895 to 2024; however, the derived data used in the analysis and modeling (referred to as the integrated dataset) includes observations only from 2014 to 2024. By integrating the datasets from two domains—traffic records and historical precipitation measurements—the modeling and analysis aimed to provide insights into how weather conditions influence road safety. The findings of the study were communicated through intuitive visualizations and a predictive linear regression model.

To achieve this goal, precipitation data was used from the *National Oceanic and Atmospheric Administration* (NOAA), which provides monthly and yearly precipitation levels across Iowa. As for the car accident data, it was accessed from Iowa's *Open Data* Platform, which outlines various details regarding every car accident, ranging from injury count to property damage and current weather conditions. Integrating these datasets allowed us to examine a potential correlation or trend over the period from 2014 to 2024.

The project started with data profiling, quality assessment, and cleaning. This first phase of project development was critical to ensuring the data was usable for the analysis and modeling stages. This process involved refining our timeframe to 2014–2024 and narrowing our observations to just the car accidents that occurred during wet weather conditions. Once the integrated dataset was prepared, we proceeded into exploratory data analysis. During this second phase of the project, we utilized descriptive statistics and visualizations to uncover meaningful patterns.

The targeted audience who could benefit from this analysis includes urban planners, emergency response services, and climate change researchers. Potential societal impacts of this analysis could involve raising awareness of the need for safe driving practices, especially during increased or unexpected precipitation, as well as appropriate responses by departments responsible for transportation in terms of resource scaling. For example, efforts could include reducing speed limits during rainfall, ensuring proper vehicle maintenance, deploying extra road salt or sand during rainy months to improve traction, or increasing signage to warn drivers about potential hazards and accidents.

Through thorough data cleaning, exploratory visualizations, and a predictive linear regression model, the relationship between annual precipitation and total yearly car accidents was not only quantified but also contextualized for its potential applications. This highlights the value of the insights derived from the study and their broad implications for public safety and planning.

In conclusion, the project demonstrated a clear positive correlation between a rise in annual precipitation and total yearly car accidents. These findings are highly relevant for policymakers, transportation departments, and public safety initiatives. As previously stated, they emphasize the critical importance of safe driving practices and resource planning during adverse weather conditions, further underlining the practical value of such analyses in protecting communities.


## Data Profile

### National Centers for Environmental Information (NCEI)
**License:** Creative Commons CC0 1.0 Universal (CC0)

**Available at:** [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000)

**Included below is every dataset column, respective description, and respective data type:**

| Column Name | Description                                               | Data Type |
|-------------|-----------------------------------------------------------|-----------|
| `Date`      | The date of record in the format *YYYYMM*.                | Number    |
| `Value`     | The total precipitation amount for the respective date.   | Number    |
| `Anomaly`   | The anomaly for the respective date.                      | Number    |

**Description of acquisition process programmed in `acquisition.py` and notated in `acquisition.ipynb`:** To aide in the process of reproducibility and dynamic data accession, this dataset is download during the workflow via a URL link. Before accessing the dataset via URL, `src/checksums/checksums.txt` is read and the appropriate and correct checksum is saved into memory for this dataset. Next, the URL used directly links to the dataset download (CSV format). First, the response to the URL is fetched using the `requests` library. Second, the response is converted to text. Third, a checksum is created from the response text using the `hashlib` library. If the generated checksum matches the checksum saved into memory (from `src/checksums/checksums.txt`), the program moves onto the fourth step. If the generated checksum does not match the checksum saved into memory, the program is terminated and the statement, "NCEI checksum verification failed.", is printed. Fourth, the statement, "NCEI checksum verification passed.", is printed and, using the `StringIO` and `pandas` libraries, the response text is read into a *pandas* dataframe (skipping the first four rows that represent dataset metadata). Fifth, the dataframe is saved as a CSV in `data/raw/ncei.csv`.

**Notes on dataset usage:** Imported data is from time range year 1895 to 2024. Dataset includes columns: `Date`, `Value`, `Anomaly`. Column `Date` contains the date of record in the format *YYYYMM*. Column `Value` contains the total precipitation amount for the respective date in column `Date`. Column `Anomaly` contains the anomaly for the respective date in column `Date` and is not used in the analysis or model. The dataset was refined to years 2014 to 2024. This dataset is first read into *pandas* dataframe. The dataframe is then downloaded as a CSV. Modifications have been made to integrate and preprocess the data for analysis. Use of the data must comply with the respective licenses. 

### Iowa Open Data
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Available at:** [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data)

**The dataset was refined to the time range of years 2014 to 2024. Included below is every dataset column, respective description, and respective data type from the dataset website:**

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

**Description of acquisition process programmed in `acquisition.py` and notated in `acquisition.ipynb`:** To aide in the process of reproducibility and dynamic data accession, this dataset is download during the workflow via a SoQL query. Before accessing the dataset via URL, `src/checksums/checksums.txt` is read and the appropriate and correct checksum is saved into memory for this dataset. Next, the SoQL query used downloads the dataset in CSV format. First, the SoQL query is saved as the endpoint. Second, the response to the query is fetched using the `requests` library. Third, the response is converted to text. Fourth, a checksum is created from the response text using the `hashlib` library. If the generated checksum matches the checksum saved into memory (from `src/checksums/checksums.txt`), the program moves onto the fifth step. If the generated checksum does not match the checksum saved into memory, the program is terminated and the statement, "NCEI checksum verification failed.", is printed. Fifth, the statement, "NCEI checksum verification passed.", is printed and, using the `StringIO` and `pandas` libraries, the response text is read into a *pandas* dataframe (skipping the first four rows that represent dataset metadata). Sixth, to avoid the need for GitHub Large File Storage (GLFS), the dataframe is split into three separate dataframes of equal length. Seventh, the three, separated dataframes are saved as CSVs in `data/raw/iowa1.csv`, `data/raw/iowa2.csv`, and `data/raw/iowa3.csv`.

**Notes on dataset usage:** Imported data was limited to 583,174 rows (from year 2009 to 2024). Columns  `Year`, `Environmental Conditions`, `Surface Conditions`, `Weather Condition`, `Crash Severity`, `Number of Fatalities`, `Number of Injuries`, `Number of Major Injuries`, `Number of Minor Injuries`, `Number of Possible Injuries`, `Number of Unknown Injuries`, and `Amount of Property Damage` are used in the integrated dataset. This dataset is first read into *pandas* dataframe. The dataframe is then separated into three different dataframes. The dataframes are then downloaded as a CSVs. Modifications have been made to integrate and preprocess the data for analysis. Use of the data must comply with the respective licenses.


## Findings

**Link to the results:** [https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr](https://uofi.app.box.com/s/rhognoqb40zuhnnnxhyzgl4vb90p3rjr) (The `results` folder should be placed within the main repository folder. The `data` folder should also be placed within the main repository folder.)

After meticulously combining our data from two distinct sources into a single CSV file, we initiated our analysis with exploratory data analysis (EDA) to uncover patterns and relationships. This phase was crucial for understanding the structure and trends in the data before diving into modeling or deeper statistical analyses. Our findings are summarized through four distinct visualizations and one linear regression equation that together paint a comprehensive picture of the relationships in the dataset.

The first visualization is a pair plot showcasing precipitation plotted against nine other variables. This plot allows for a detailed examination of how precipitation interacts with different aspects of the dataset. From these scatterplots, we observed that precipitation exhibits a strong positive relationship with variables such as count, possinjury, mininjury, and propdmg. These relationships suggest that increases in precipitation are linked to a rise in minor accidents and associated property damage. Conversely, precipitation has only a weak positive correlation with uninjury, majinjury, and fatalities, implying that it may have a less significant effect on more severe accidents. A particularly notable finding is the strong negative relationship between precipitation and year, which suggests a decline in precipitation levels over time. This trend is critical, as it may influence the changing patterns of accidents over the years, leading to new considerations for future studies.

The second visualization, a heatmap, provides a succinct summary of the pair plot’s findings by displaying correlation coefficients for all variable pairs. To emphasize the importance of precipitation, we have highlighted its corresponding row and column. The heatmap reinforces the observed relationships, particularly the strong positive correlations between precipitation and variables associated with minor accidents, as well as its negative correlation with year. This graphical representation simplifies interpretation, offering a clear overview of the data's underlying relationships.

The third visualization is a line plot overlaying count (the number of accidents) and precipitation. This plot reveals a fascinating temporal trend: prior to 2017, the two variables do not appear to trend together, but after 2017, they both exhibit a downward trajectory. This shift suggests a potential change in environmental or behavioral factors influencing accidents and precipitation post-2017, warranting further investigation.

The fourth visualization is a linear model plot (lmplot), which reiterates the strong positive relationship between count and precipitation. While the data points are generally tightly clustered around the line of best fit, there is one notable outlier that may require further scrutiny. This outlier could represent an anomaly or an important exception to the general trend.

Finally, our analysis includes the following linear regression equation:

$\widehat{count} = 196.37210083007812 \cdot precipitation + 1943.09619140625$.

This equation quantifies the relationship between precipitation and car accidents, showing that for every additional inch of annual precipitation, we can expect approximately 196 additional accidents. These findings provide compelling evidence of a significant relationship between precipitation and car accidents, particularly in Iowa. This analysis underscores the importance of considering environmental factors in accident prediction and prevention.


## Future Work

Given the project’s focus on Iowa, expanding the scope to include other Midwestern states could provide a broader understanding of the observed trends. States like Wisconsin and Michigan, which experience diverse weather patterns due to the influence of the Great Lakes, could yield intriguing comparisons in both accident frequency and precipitation patterns. These states' unique geographical and climatic features might reveal whether similar relationships between precipitation and accidents are consistent across the Midwest. Moreover, investigating how these trends align or differ could uncover regional factors that influence road safety, such as local driving habits, seasonal weather variability, or state-specific policies.

Analyzing infrastructure across neighboring states could also offer valuable insights. For instance, comparing Iowa’s road systems with those of Wisconsin or Michigan from a civil engineering perspective might highlight discrepancies in design, maintenance, or safety measures. These comparisons could inform policy recommendations for improving infrastructure in areas where deficiencies contribute to higher accident rates. Additionally, identifying best practices in states with lower accident rates under similar weather conditions might provide actionable strategies for reducing accidents. Such cross-state analyses could benefit not just researchers but also policymakers, urban planners, and civil engineers aiming to enhance road safety.

In pre-processing the dataset, the current analysis focused specifically on accidents occurring during rain. However, other water-related road conditions, such as post-snow slush or flooding, might create comparable driving hazards. Including these scenarios in future studies could provide a more comprehensive understanding of how water-related factors influence road safety. Moreover, the decision to analyze data from a specific decade raises questions about how findings might change if the dataset were expanded to include years before 2009. Historical data could introduce new perspectives, particularly given advancements in automotive technology over the years. Today’s vehicles are equipped with far more sophisticated safety features than those a few decades ago, which could skew accident data if not properly accounted for. For example, what is considered a minor accident today might have been a major incident in the past due to differences in car safety standards and technologies.

The severity of accidents, including the presence of fatalities or injuries, serves as a critical marker for understanding temporal discrepancies in the dataset. Investigating these aspects more deeply could clarify how changing safety features and standards have influenced the definition and frequency of accidents over time.

Finally, extending the analysis beyond the Midwest to regions with markedly different climates could provide further contrasts. For example, examining a country like Colombia, where extreme precipitation, varying altitudes, and less developed infrastructure are prevalent, could offer fascinating insights. Unlike Iowa’s predominantly flat terrain, Colombia’s diverse geography might highlight how altitude and infrastructure deficiencies interact with precipitation to affect road safety. Such a study would provide a valuable global perspective, enriching the understanding of how environmental and infrastructural factors contribute to accidents in various contexts.


## Reproduction of Analysis

### Requirements
All packages, software dependencies, and the programming environment as well as their versions are specified in `doc/requirements.txt` and `doc/environment.md` and must be intalled before workflow execution.

### Code Notations
Each `.py` file in folder, `src`, has a respective `.ipynb` file in folder, `doc/code_notations`, that contains replica code and respective notations organizing and describe code processes. (`.ipynb` files are not intended to be run and are for notation purposes only.)

### Data Acquisition
The *NCEI* dataset is collected via a URL link. The *Iowa Open Data* dataset is collected via an API query. Both of these processes are included in the workflow as well as their respective integrity checks in the rule, `acquisition`.

### Running the Workflow
The workflow must be run with Python 3.11.1 and all dependencies listed in `requirements.txt`. The workflow must be executed from the `/src` directory. Please note that it may take several minutes to complete.

All code in pure python is included in the folder, `src`, as `.py` files. This is the code used to run the workflow file, `Snakefile`. The `Snakefile` creates five rules: `runall`, `acquisition`, `integration`, `analysis`, and `modeling`.

- Rule `runall` executes all processes necessary to produce `heatmap.png`, `lineplot.png`, `lmplot.png`, `pairplot.png`, and `regression-output.md`.
- Rule `acquisition` takes `src/checksums/checksums.txt` as input and, using `src/acquisition.py`, uses links and API queries to fetch and integrity check all raw datasets and saves them to `data/raw`. (The Iowa Open Data dataset is saved as three separate *.csv* files to avoid usage of GitHub Large File Storage.)
- Rule `integration` takes all raw *.csv* files as input and, using `src/integration.py`, integrates the raw datasets into the processed, final dataset, `data/processed/integrated.csv`.
- Rule `analysis` takes `data/processed/integrated.csv` as input and, using `src/analysis.py`, creates graphs and analyzes the processed dataset. Rule `modeling` takes `data/processed/integrated.csv` as input and, using `src/modeling.py`, finds the best model.

**To execute the workflow, the line:**

```
snakemake --cores 1 runall
```

****


## References

### Dataset Citations
NOAA National Centers for Environmental information, Climate at a Glance: Statewide Time Series, published November 2024, retrieved on December 5, 2024 from [https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series)

Iowa Department of Transportation, Motor Vehicle Division: Vehicle Crashes in Iowa, published July 2022, retrieved on December 5, 2024, from [https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data)

Use of the datasets must comply with the respective licenses.

### Software Citations
For dependencies, see `doc/requirements.txt`. Use of the software must comply with the respective licenses.

### Software Created
Licensed under the MIT License. See `LICENSE.txt` for details.