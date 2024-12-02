# **Progress Report**

## Updates on Individual Tasks

### Ben - Monday, November 4th

Completed programmatic data acquisition and integrity checks on datasets. Since the datasets are not intuitively programmatically downloadable from their respective websites, alternative methods were used. For the [NCEI precipitation dataset](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024?base_prd=true&begbaseyear=1901&endbaseyear=2000), the site API is cumbersome and perplexing. Instead, the *requests* library is used to retrieve a direct link to the CSV download on the webpage. The response text is then read by StringIO and then converted into a pandas dataframe (`df_ncei`). For the [Iowa Open Data auto-accident dataset](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data), the Socrata API is used, with a modified setting to account for the size of the dataset. The default record limit for the API is 1,000 rows, however, using the suffix "?$limit=583174" in our API endpoint, we can modify the record limit to the size of the dataset (583174 rows). Then, the *requests* library is used to retrieve the API endpoint. The response text is then read by StringIO and then converted into a pandas dataframe (`df_accidents`).

Before each response text is converted into a dataframe, an integrity check is done on the response. To start, SHA-256 hash is created from the response using hashlib. If this checksum is found in the checksum set of real checksums (called `checksums`), then the response text is converted into a pandas dataframe.

Lastly, some modifications on the datasets were completed. For `df_accident`, the `date_of_crash` column was used to create a new column, `year`. The dataframe was then shortened to include only the columns `year`, `enviro_conditions`, `light_conditions`, `surface_conditions`, `weather_conditions`, `crash_severity`, `fatalities`, `injuries`, `majinjury`, `mininjury`, `possinjury`, `unkinjury`, and `propdmg`. For `df_ncei`, the `Date` column was used to create a new column, `year`. Then, the column `Value` was renamed to `precipitation`. The dataframe was then shortened to include only the columns `year` and `precipitation`.

### Vital - Sunday, November 10th 

Completed the outlined tasks surrounding quality assessment of the data and examining the readiness of the dataset for the final fit-for-use format expected during hand-in date. Format of datasets had a clear distinction between the formatting of the dates, Ben's hand-off served as a key starting point from which I have dug deeper into the attributes and extracted the key components we are going to want to use for our models. Some explicit missing data required attention by simply categorizing into pre-established `Unknown` categories, as well as a discovery of additional features we did not consider in the beginning such as fatalities, injuries and property damage. Isolated the analysis into two dataframes the team is currently evaluating to understand with which are we looking to go forward. 

Started off by identifying the value types per column that seemed interesting to take into accountability for final model creation utilizing `.unique()`, which lead to the discovery of previously mentioned missing values. Adressed this by filling the missing values with corrersponding `Unknown` value per respective column due to prior existance of said value as an option. Given our primary focus on raining conditions, narrowed the scope of `weather_conditions` and `surface_conditions` to the weather pattern that most accurately described regular raining: `Rain, Sleet hail, Freezing rain/drizzle` within `weather_conditions` and `Wet` within `surface_conditions`

Proceeded to work on `df_ncei` where Ben left off by converting the `year` column into an integer to ensure manipulation that followed would be interpreted as numeric rather than string. Due to the limitation of the Iowa Dataset with dates, narrowed the overall scope of `years` to start at 2014 and upwards, giving us a 10 year range of data precipitation to work with. Created initial `grouped_df` dataframe containing a grouped assessment of the total crashes per year given `crash_severity` and respective features to get an overview of how the data will be shaped. Noticed there was not a clear overview showcasing the total number of accidents per year, thus deployed a brief loop that cycled through each row and classified it per respective year. Provided a comparatory `grouped_df_2` in which every single data is grouped by merely `year` to successfully be merged with `yearly_counts_df` dataframe generated with previously mentioned loop. 

General overview dataframe currently is `merged_df`, through which we're assessing how we can retrace some of the previous analysis steps and account for additional insights we might want to tackle within the third phase of the project entailing the use of `scikit-learn` and the building of a model. 

### Ryan - Tuesday, November 12th

Completed tasks of creating simple data visualizations and models. I picked up from where Vital left off and began by Saving `merged_df` in `data/integrated.csv`. I began with some exploratory data analysis by analyzing the correlation matrix of the integrated dataset. I observed that `precipitation` and `count` had the strongest relationship with a coefficient of 0.635. I produced a heatmap visualization of the correlation coefficient matrix using the *seaborn* and *matplotlib* packages. The visual highlights the correlations associated with `precipitation`, our target variable of interest.

I created a pairplot using *seaborn* and *matplotlib* to graphically visualize the relationship between precipitation and the other variables. Most variables have a positive relationship, with the exception of `year`. `count` displays one of the tightest spread among data points. I created an lmplot with *seaborn* and *matplotlib* to focus further in on the relationship between `precipitation` and `count`.

Next, I decided to make a visualization to show how both `count` and `precipitation` change through our time interval together. This is a lineplot with both variables on two separate y axes and year on the x axis. This visual shows that both `precipitation` and `count` tend to change in sync for the most part, but not always.

Finally, I created a simple linear model to predict `count` based on `precipitation`. I used *pycaret* to create and compare different regressions consisting of: normal linear regression, ridge regression, lasso regression, elastic net regression, and huber regression. The best model was the elastic net regression with an $R^2$ of -0.4852. The equation is as follows: $\widehat{count}$ $=$ $200.10318$ $*$ $precipitation$ $+$ $1930.2559$.

All the visualizations were saved to the results folder.

## Updated Project Vision

The overall goal of this project will be to explore a correlation phenomenon between the number of car accidents and amount of precipitation per month within Iowa, using data from a 2014-2024 timeframe. 

## Updated Timeline and Next Task Assignments

Everyone needs to:

* Move their code steps to .py files for the workflow
    * Export any intermediate data to csv files
* Add markdown annotations to their code notebook

On Saturday 11/16 we will meet up and knock out the following tasks together:

Ryan
* Automated Workflow (cf. Week 9-10)
    * Snakemake workflow automating your end-to-end analysis workflow from acquisition to result visualization.
    * Run All script that can be used to re-execute your end-to-end analysis workflow in the form of a `Snakefile`
    * Documentation describing the steps required to repeat your workflow included in `README.md`

Ben
* Reproducible package (cf. Week 8)
    * Sufficient information to allow someone else to reproduce your analysis including:
        * Documentation describing steps someone else needs to take to reproduce your results included as an overview in `README.md` and in-depth in `analysis.ipynb`
        * Data or documentation describing how to obtain data used overviewed included as an overview in `README.md` and in-depth in `acquisition.ipynb`
        * All code, workflow scripts, etc., needed to reproduce your results included in `Snakefile`, `acquisition.py`, `integration.py`, and `analysis.py` files
        * Actual results of your analysis including output files, visualizations, etc. included in `../results`
        * Specification of software dependencies (e.g., requirements.txt) and record of specific packages used (e.g., output of pip freeze) included in `requirements.txt`
    * Licenses for data and software created as part of your project reviewed in-depth in `README.md`

Vital
* Citation of data and software used (cf. Weeks 11-12)
    * Accurate citations of the data and/or software used in your project in conformance with standards included in `README.md`
* Metadata describing your dataset and package (cf. Week 12)
    * Data dictionary or codebook as text file, PDF, or self-describing data formats included in `dictionary.pdf`
    * Descriptive metadata describing your project in conformance with a standard such as DataCite, Schema.org
* Archival record (cf. Week 13)
    * An copy of your project submitted to the Zenodo long-term archive or a CodeOcean capsule
* Persistent Identifier (cf. Week 13)
    * Persistent identifier obtained from the long-term archive