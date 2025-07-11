import pandas as pd
import hashlib
import requests
import os 
from io import StringIO

df1 = pd.read_csv('../data/raw/iowa1.csv')
df2 = pd.read_csv('../data/raw/iowa2.csv')
df3 = pd.read_csv('../data/raw/iowa3.csv')
df_accidents = pd.concat([df1, df2, df3], ignore_index=True)

df_ncei = pd.read_csv('../data/raw/ncei.csv')

date_time = pd.to_datetime(df_accidents['date_of_crash'])
df_accidents['year'] = date_time.dt.year

df_accidents = df_accidents[[
    'year', 'enviro_conditions', 'surface_conditions', 'weather_conditions',
    'crash_severity', 'fatalities', 'injuries', 'majinjury', 'mininjury',
    'possinjury', 'unkinjury', 'propdmg'
]]

df_accidents['enviro_conditions'] = df_accidents['enviro_conditions'].fillna('Unknown')
df_accidents['surface_conditions'] = df_accidents['surface_conditions'].fillna('Unknown')

filtered_test = df_accidents[
    ((df_accidents['weather_conditions'] == 'Rain') | 
    (df_accidents['weather_conditions'] == 'Sleet, hail') | 
    (df_accidents['weather_conditions'] == 'Freezing rain/drizzle')) & 
    ((df_accidents['surface_conditions'] == 'Wet') | 
    (df_accidents['surface_conditions'] == 'Unknown'))
]

df_ncei['year'] = df_ncei['Date'].apply(lambda x: int(str(x)[:4]))
df_ncei.rename(columns={'Value': 'precipitation'}, inplace=True)
df_ncei = df_ncei[['year', 'precipitation']]
df_ncei['year'] = df_ncei['year'].astype(int)
df_ncei = df_ncei[df_ncei['year'] >= 2014]

grouped_df = filtered_test.groupby([
    'year', 'enviro_conditions', 'surface_conditions', 
    'weather_conditions', 'crash_severity'
]).sum().reset_index()

yearly_counts = {'year': [], 'count': []}
current_year = None
count = 0

for index, row in filtered_test.iterrows():
    if row['year'] == current_year:
        count += 1
    else:
        if current_year is not None:
            yearly_counts['year'].append(current_year)
            yearly_counts['count'].append(count)
        current_year = row['year']
        count = 1

yearly_counts['year'].append(current_year)
yearly_counts['count'].append(count)

yearly_counts_df = pd.DataFrame(yearly_counts)

grouped_df_2 = filtered_test.groupby(['year']).sum().reset_index()
merged_df = pd.merge(df_ncei, grouped_df_2, on='year', how='inner')
merged_df = pd.merge(yearly_counts_df, merged_df, on='year', how='inner')
merged_df = merged_df[['year', 'precipitation', 'count', 'fatalities', 'injuries', 'majinjury', 'mininjury', 'possinjury', 'unkinjury', 'propdmg']]

merged_df.to_csv('../data/processed/integrated.csv', index=False)