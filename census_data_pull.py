import json
import pandas as pd
import numpy as np
import requests
from pprint import pprint
import datetime
import pickle
import time

timee = datetime.datetime.now()
# Get GEO_UID for each FSA, this is used in following GET request
initial = requests.get('https://www12.statcan.gc.ca/rest/census-recensement/CR2016Geo.json?lang=E&geos=FSA&cpt=35',
                  headers={'User-Agent': 'Mozilla/5.0'})
data = json.loads(initial.text[2:]) # remove leading '//' from REST response
initial_df = pd.DataFrame(columns = data['COLUMNS'], data = data['DATA'])
ok = {}
for z in initial_df.itertuples():
    # API request for data using GEO_UID
    request = requests.get(f'https://www12.statcan.gc.ca/rest/census-recensement/CPR2016.json?lang=E&dguid={z.GEO_UID}&topic=4&notes=0&stat=0',
                      headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(request.text[2:])
    df = pd.DataFrame(columns = data['COLUMNS'], data = data['DATA'])
    # point = np.asarray(df[df['TEXT_NAME_NOM'] == "Population, 2016"]['T_DATA_DONNEE'])[0]
    point2 = np.asarray(df[df['TEXT_NAME_NOM'] == "Total - Occupied private dwellings by structural type of dwelling - 100% data"]['T_DATA_DONNEE'])[0]
    # ok[str(z.GEO_NAME_NOM)] = point
    ok[str(z.GEO_NAME_NOM)] = point2

pickle_out = open("census_data_households.pickle","wb")
pickle.dump(ok, pickle_out)
pickle_out.close()
print(datetime.datetime.now()-timee)
