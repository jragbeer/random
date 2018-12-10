import pandas as pd
import numpy as np
import wget
import datetime
import urllib

timee = datetime.datetime.now()

print(timee)

def cleandf(df):
    df.fillna(0, inplace=True)
    df.drop_duplicates(inplace=True)
    df.drop('Unnamed: 0', 1, inplace=True)
    df.Year = df.Year.astype('int')
    df.Age = df.Age.astype('int')
    df.G = df.G.astype('int')
    df.GS = df.GS.astype('int')


    df['ppg'] = df['PTS'] / df['G']
    df['rpg'] = df['TRB'] / df['G']
    df['drpg'] = df['DRB'] / df['G']
    df['orpg'] = df['ORB'] / df['G']
    df['apg'] = df['AST'] / df['G']

    df['Player'] = pd.Series([str(x).replace('*', '') for x in df['Player']], index=df.index)
    return df

df = pd.read_csv('Seasons_Stats.csv')
df = cleandf(df)

direc = 'C:/Users/Julien/PycharmProjects/csvsaving/static/'

p = 0
n = 0
for x in df.Player.unique():
    try:
        llast = x.lower().split()[1].replace("'", "").replace(".", "")
        ffirst = x.lower().split()[0].replace("'", "").replace(".", "")
        name = 'https://nba-players.herokuapp.com/players/{}/{}'.format(llast, ffirst)
        meta = urllib.request.urlopen(name).info()

        if int(meta['Content-Length']) < 75:
            continue
        else:
            filename = wget.download(name, out=direc + '{}_{}.png'.format(ffirst, llast))
            print("Content-Length:", meta)
            print('{}_{}'.format(ffirst,llast))
            p+=1
    except Exception as e:
        print(str(e))
        pass
        n+=1
print('number of pics', p)
print('number of no-pics', n)
print(datetime.datetime.now()-timee)