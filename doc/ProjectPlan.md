# **Project Plan**

# Overview
The overall goal of this project will be to explore a correlation phenomenon between the number of car accidents and amount of precipitation per month within Iowa, using data from a 2009-2024 timeframe. 

We hope that by combining the data from these two domains, we will be able to successfully communicate our findings through intuitive visualizations in the final part of the project. 
The precipitation data will be drawn from National Oceanic and Atmospheric Administration (NOAA), whilst the car accident data was made available by Iowa’s Open Data Platform. 

During the data integration efforts, we will observe the average precipitations for each month over our timeframe, and also find the average car accidents each month. This will involve grouping the data by month and aggregating it by mean. Once we determine that our data is accordingly formatted and in a tidy format that fits our intended use, containing 1 instance for each month, each record will have two columns: precipitation and number of crashes. From there, we will begin to build our final visualizations for the data.

After determining the existence of a possible relationship, we can have a better understanding of the possible number of car accidents based on any trends observed correlating with the amounts of precipitation. Long term changes in climate and precipitation could have implications for traffic safety requirements. This could prove a need for future increases in proactive measures in traffic safety amid increasing amounts of precipitation in certain regions.

The people who would benefit from this analysis are urban planners, emergency response services, and climate change researchers. Potential societal impacts of this analysis are more general awareness of the need for safe driving practices, especially during increased precipitation.

We can also construct a time-series analysis of precipitation over our 2009 to 2024 timeframe to determine how precipitation is changing, and then use that information to project precipitation into the future, and with that, project the amount of car crashes into the future.

# Research Question(s)
Is there a correlation between the number of car accidents and amount of precipitation per month basis within our 2009-2024 timeframe within Iowa?

# Team
Below explicitly details the assigned tasks of each team member, along with due dates for each person's tasks.

### Ben
* By Sunday 11/3
  * Aquire datasets and document dataset aquisition
    * Collect data from National Centers for Environmental Information and Iowa Department of Transportation, Motor Vehicle Division, while documenting steps in the data collection process in-depth
  * Implement integrity checks / checksums on the datasets
    * Utilize SHA-256 to ensure data integrity and that collected data is untampered
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report
    * Document process of task completion, including decisions made and challenges encountered

### Vital
* By Sunday 11/10
  * Programmatically integrate datasets using Python and Pandas
    * Ensure data sets are of consistent semantic and syntactic structure for data integration
    * Combine data into a singular dataframe for ease of analysis
  * Transparent data profiling and quality assessment
    * Ensure data completeness, readiness, and fit-for-use in final dataframe and document findings
    * Explore the nature of missing data, data correlation, and need for data transformation
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report
    * Document process of task completion, including decisions made and challenges encountered

### Ryan
* By Wednesday 11/13
  * Data cleaning using Python and Pandas
    * Utilize appropriate imputation methods to accurately clean data
    * Document obstacles faced during the data cleaning process and decisions made
  * Implement simple data analysis and/or visualization using SKLearn, Matplotlib, and PyCaret
    * Utilize SKLearn for model building and feature selection
    * Utilize Matplotlib to display trends and correlations in data
    * Utilize PyCaret to efficiently determine the best models
  * Write a summary of tasks completed, and any concerns or obstacles faced to add to the progress report
    * Document process of task completion, including decisions made and challenges encountered

On November 14th and/or November 15th we will meet up and compile our progress report together. We will put together the summaries that we previously prepared, and also further plan out our next steps for the project.

# Datasets
Our first dataset is a JSON dataset from [National Oceanic and Atmospheric Administration (NOAA)](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/33/pcp/1/0/2009-2024). This dataset is available under a Creative Commons CC0 1.0 Universal (CC0) license. This dataset contains precipitation for each month from 2009 to 2024.

Our second dataset is a CSV dataset from [Iowa Open Data](https://data.iowa.gov/Crashes/Vehicle-Crashes-in-Iowa/tw78-ziwj/about_data). This dataset is available under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. This dataset contains information on vehicle crashes from 2009 to 2024. The dataset includes information such as the time and date, major cause, environmental factors, road factors, surface conditions, weather conditions, and roadway conditions. We can filter this dataset based on `weather_condtions`, so that our analysis will focus on the accidents occurred in certain conditions.

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
