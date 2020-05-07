import numpy as np
import pandas as pd
import re
import datetime

np.set_printoptions(suppress=True) #prevent numpy exponential
                                   #notation on print, default False
path = "C:/Users/Julien/Desktop/"
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)

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
print(df.to_string())

today = datetime.date.today()
day_num = int(today.strftime('%j'))
current_canada_deaths = 4232
season_length = 92

df['Curr_Deaths'] = [np.around(each*(day_num/(season_length+day_num))) for each in df['Deaths']]
wow = pd.read_html("https://en.wikipedia.org/wiki/Population_of_Canada")
population = wow[8]
population.columns = ['Year', "Pop", "Change"]
population = population.iloc[:-1,:]
population = population[['Year', "Pop"]]

data = df.merge(population, left_on='Season_Ending', right_on='Year')
data['Pop']= data['Pop'].astype(int)
data['Pop_multiplier'] = 1+(37_000_000-data['Pop'])/data['Pop']
data['Death_mult'] = data['Deaths'] * data['Pop_multiplier']
print(data.to_string())