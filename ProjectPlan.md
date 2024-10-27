# Overview
The overall goal of our project is to determine if there is a relationship between the number of car accidents and amount of precipitation each month, using data from a timeframe from 2009-2024 in Iowa. We hope to uncover a relationship by combining data from these two domains, and then effectively communicate our findings through intuitive visualizations. 

More specifically, we are going to use precipitation data drawn from NOAA, and car accident data drawn from _____. During data integration, we will find average precipitations each month over our timeframe, and also find average car accidents each month over our timeframe. This will involve grouping the data by month and aggregating it by mean. After that we will have a tidy dataset that is fit for our use, containing 1 record for each month, and each record will have two columns, precipitation and number of crashes. From there, we can visualize the data.

After determining what sort of relationship exists, we can project expected future numbers of car accidents based on expected future amounts of precipitation. Long term changes in climate and precipitation could have implications on traffic safety requirements. This could prove a need for future increases in proactive measures in traffic safety amid increasing amounts of precipitation in certain regions.

The people who would benefit from this analysis are urban planners, emergency response services, and climate change researchers. Potential societal impacts of this analaysis are more general awareness of the need for safe driving practices, especially during increased precipitation.

# Research Question(s)
Is there a correlation between the number of car accidents and amount of precipitation per month basis within our 2009-2024 timeframe.

# Team
Below explicitly details the assigned tasks of each team member, along with due dates for each person's tasks.

### Ben
* By Sunday 11/3
  * Aquire datasets and document dataset aquisition
  * Implement integrity checks / checksums on the datasets
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report

### Vital
* By Sunday 11/10
  * Programmatically integrate datasets using Python and Pandas
  * Transparent data profiling and quality assessment
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report

### Ryan
* By Wednesday 11/13
  * Data cleaning using Python and Pandas
  * Implement simple data analysis and/or visualization using SKLearn and Matplotlib
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report


On 11/14 and/or 11/15 we will meet up and compile our progress report together.

# Datasets
Our first dataset is a json dataset from [National Oceanic and Atmospheric Administration (NOAA)](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/33/pcp/1/0/2009-2024). This dataset is available under a Creative Commons CC0 1.0 Universal (CC0) license.

Our second dataset is a csv dataset from [data.iowa.gov](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data). This dataset is available under a Creative Commons Attribution 4.0 International (CC BY 4.0) license.

# Timeline
We are splitting our project into two halves, one to be completed before the November 15 status report, and one before the final deadline.

### Before Nov 15 (Status Report Due), we will have the following tasks completed:
* By Sunday 11/3
  * Aquire datasets and document dataset aquisition
  * Implement integrity checks / checksums on the datasets
* By Sunday 11/10
  * Programmatically integrate datasets using Python and Pandas
* By Friday 11/15
  * Transparent data profiling, quality assessment, and cleaning using Python and Pandas
  * Implement simple data analysis and/or visualization using SKLearn and Matplotlib
  * 2 Page Status Report

### Before Dec 11 (Project Deadline), we will have the following tasks completed:
More specific dates and roles will be determined in the next status report.
* Create a reproducible package
* Create an automated end-to-end workflow execution
* Document accurate citations of data and software used
* Create metadata describing your package
* Archive your project in a repository, obtaining a persistent identifier
