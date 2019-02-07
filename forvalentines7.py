import pandas as pd
import xlrd
import re
def stuff(y):
    c = re.search(r'L', y)
    d = re.search(r'U', y)
    if c:
        return 'Leveraged'
    if d:
        return 'Unleveraged'
path = 'C:/Users/J_Ragbeer/PycharmProjects/nlp/' #path on the CPU
df = pd.read_excel(path+"Tableau Data ReturnsFeb7.xlsx", sheet_name = 'Summary', skiprows = 2, skipfooter = 1)
df.columns = df.columns.str.strip()
df.set_index('Investment', inplace = True)
unpivotcols = ['Region', 'Asset Class', 'Risk Class']
newdf = df[unpivotcols].copy()
df.drop(unpivotcols,1,inplace = True)
rr = [(x.split()[0], x.split()[1], stuff(x)) for x in df.columns]
df.columns = pd.MultiIndex.from_tuples(rr, names=['Investment', 'Period', 'Financing'])
df = df.stack(level = [1])
df = df.stack()
for y in unpivotcols:
    a = [newdf.loc[x.Index[0], y] for x in df.itertuples()]
    df[str(y)] = pd.Series(a, index = df.index)
df.columns = [x.replace('U', '').replace('L', '') for x in list(df.columns)]
print(df.head(100).to_string())
df.to_csv(path + 'converted2.csv', index = True)

