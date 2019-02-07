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
    else:
        return 'Leveraged'
path = 'C:/Users/J_Ragbeer/PycharmProjects/nlp/' #path on the CPU
df = pd.read_excel(path+"Tableau Data Returns Revisedxlsx.xlsx", sheet_name = 'Summary', skiprows = 2)
df.columns = df.columns.str.strip()
df.fillna(6, inplace = True)
df.set_index('Investment', inplace = True)
unpivotcols = ['Region', 'Asset Class', 'Risk Class']
newdf = df[unpivotcols].copy()
df.drop(unpivotcols,1,inplace = True)
rr = [(x.split()[0].replace('U', '').replace('L', '').strip(), x.split()[1].strip(), stuff(x)) for x in df.columns]
for x in range(len(rr)):
    if rr[x][0] == 'RCN':
        rr[x] = ('RC', rr[x][1], rr[x][2])
df.columns = pd.MultiIndex.from_tuples(rr, names=['Investment', 'Period', 'Leverage'])
xdf = df[['CASH']].stack(level = 'Period')
df.drop(['CASH'],1,level =0 ,inplace=True)
df = df.stack(level = 'Leverage').stack()
xdf.columns = xdf.columns.droplevel(1)
pp = [xdf.loc[(x.Index[0],x.Index[2]), 'CASH'] for x in df.itertuples()]
df['CASH'] = pd.Series(pp, index = df.index)
for y in unpivotcols:
    a = [newdf.loc[x.Index[0], y] for x in df.itertuples()]
    df[str(y)] = pd.Series(a, index = df.index)
df.to_csv(path + 'converted3.csv', index = True)

