import pandas as pd
import hmac
import hashlib
import requests
from io import StringIO


with open('checksums.txt', 'rb') as f:
    data = f.read()
    checksum_verify = str(data.split()[1]).split("'")[1]
url = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/13/pcp/1/9/1895-2024.csv?base_prd=true&begbaseyear=1901&endbaseyear=2000'
response = requests.get(url)
checksum = hashlib.sha256(response.text.encode('utf-8')).hexdigest()
if checksum == checksum_verify:
    print('NCEI checksum verification passed.\n')
    df_ncei = pd.read_csv(StringIO(response.text), skiprows=4)
    df_ncei.to_csv('data/raw/ncei.csv')
else:
   print('NCEI checksum verification failed.')


with open('checksums.txt', 'rb') as f:
    data = f.read()
    checksum_verify = str(data.split()[3]).split("'")[1]
endpoint = 'https://data.iowa.gov/resource/tw78-ziwj.csv?$limit=583174'
response = requests.get(endpoint)
checksum = hashlib.sha256(response.text.encode('utf-8')).hexdigest()
if checksum == checksum_verify:
    print('data.iowa.gov verification passed.\n')
    df_iowa = pd.read_csv(StringIO(response.text))
    df_iowa1 = df_iowa[0:194391]
    df_iowa2 = df_iowa[194391:388782]
    df_iowa3 = df_iowa[388782:]
    df_iowa1.to_csv('data/raw/iowa1.csv')
    df_iowa2.to_csv('data/raw/iowa2.csv')
    df_iowa3.to_csv('data/raw/iowa3.csv')
else:
   print('data.iowa.gov checksum verification failed.')