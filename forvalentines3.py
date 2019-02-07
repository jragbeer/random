import pandas as pd
import xlrd
import re

path = 'C:/Users/J_Ragbeer/Desktop/' #path on the CPU
df = pd.read_excel(path+"Tableau Data Returns2.xlsx", sheet_name = 'Summary', skiprows = 2, skipfooter = 1)
df.columns = df.columns.str.strip()
df.set_index('Investment', inplace = True)
unpivotcols = ['Region', 'Asset Class', 'Risk Class']
newdf = df[unpivotcols].copy()
df.drop(unpivotcols,1,inplace = True)
rr = [(x.split()[0], x.split()[1]) for x in df.columns]
df.columns = pd.MultiIndex.from_tuples(rr, names=['Investment', 'Period'])
df = df.stack()
for y in unpivotcols:
    a = [newdf.loc[x.Index[0], y] for x in df.itertuples()]
    df[str(y)] = pd.Series(a, index = df.index)
df.to_csv('converted.csv', index = True)
