import numpy as np
import pandas as pd
import re
import datetime
import os
from pprint import pprint
import requests

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"}


pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
np.set_printoptions(suppress=True) #prevent numpy exponential notation on print

path = os.getcwd().replace("\\", "/") + "/data/"
today = datetime.date.today()
day_num = int(today.strftime('%j'))
# current coronavirus deaths, canada
total_corona_deaths = pd.read_html(requests.get("https://www.worldometers.info/coronavirus/", headers=header).text)[0]
total_corona_deaths.columns = [x.replace(',', "").replace(' ', "").lower() for x in total_corona_deaths.columns]
total_corona_deaths.set_index('countryother', inplace=True)
total_canadian_deaths = total_corona_deaths.loc['Canada']['totaldeaths']
print(total_canadian_deaths)
# number of days from October 1 to December 31 (first part of flu season)
season_length = 92

# data from research paper
df = pd.read_csv(path + 'covid_data.csv', engine='python', usecols=[x for x in range(0, 7) if x not in [4]], skipfooter=3)
df.columns = ['Season', "Strain", "Deaths", "Deaths_Range", "Hospital_Admissions", "Admissions_Range"]
df.fillna(0, inplace=True)
for each in ["Deaths",  "Hospital_Admissions", ]:
    df[each] = [int(str(x).replace(",", "")) for x in df[each]]
for each in ["Deaths_Range", "Admissions_Range"]:
    low = []
    high = []
    for i in df[each]:
        try:
            a = re.findall(r"\d{1,2},?\d+", i)
        except:
            a = ["0","0"]
        b = [int(x.replace(',', "")) for x in a]
        low.append(b[0])
        high.append(b[1])
    df[f"{each}_Low"] = low
    df[f"{each}_High"] = high
df.drop(columns=["Deaths_Range", "Admissions_Range"], inplace=True)
df = df[df['Deaths'] > 1000]
df['Season_Ending'] = [x[:2] + x[-2:] for x in df['Season']]
df['Season_Ending'].replace("1900", "2000", inplace=True)
df['Curr_Deaths'] = [np.around(each*(day_num/(season_length+day_num))) for each in df['Deaths']]
print(df.to_string())

# population data from wikipedia
wiki_population_tables = pd.read_html("https://en.wikipedia.org/wiki/Population_of_Canada")
population = wiki_population_tables[8] # current time period's population chart
population.columns = ['Year', "Pop", "Change"]
population = population.iloc[:-1, :]
population = population[['Year', "Pop"]]

# join data sets
data = df.merge(population, left_on='Season_Ending', right_on='Year')
data['Pop']= data['Pop'].astype(int)
data['Pop_multiplier'] = 1+(37_000_000-data['Pop'])/data['Pop']
data['Adj_Death_Pop'] = data['Deaths'] * data['Pop_multiplier']
print(data.to_string())
