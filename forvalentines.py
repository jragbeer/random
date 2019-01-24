import pandas as pd
import xlrd
import re

def cleandf(idf):
    idf.drop([('Risk Class', '2024.1')],1,inplace = True)
    new = []
    for col in idf.columns:
        if re.compile('Unnamed:').search(col[0]):
            new.append((col[1], col[1]))
        else:
            if re.compile('20').search(str(col[1])):
                z = int(str(col[1]).split('.')[0])
            else:
                z = col[1]
            new.append((col[0], z))
    idf.columns = pd.MultiIndex.from_tuples(new)
    return idf
def part1(idf):
    dataframe = pd.concat([pd.DataFrame(idf['Investment']), idf['Investment Name'], idf['EXT'], idf['Region'], idf['Asset Class'], idf['Country'], idf['City'],idf['Currency'],
                    idf['Risk Class', 'O/B'], idf['Risk Class', 'IPP Date']], 1)
    yy = []
    for x in dataframe.columns:
        if type(x) == tuple:
            yy.append(x[1])
        else:
            yy.append(x)
    dataframe.columns = yy
    return dataframe

path = 'C:/Users/J_Ragbeer/PycharmProjects/other/data/finance/' #path on the CPU
df = pd.read_excel(path+'final.xlsm', sheet_name = 'OXF Database', skiprows = 4, usecols="C:CY", header = [0,2], skipfooter = 21)
df = cleandf(df) #clean df
xdf = part1(df) #unpivoted table
df = df.stack() #pivot the table
newlist = ['IPP Date','O/B','Asset Class','EXT','Country', 'Investment', 'Investment Name', 'City', 'Currency', 'Region'] #list of columns that don't need pivoting
df.drop(newlist, 0, level = 1, inplace = True) #remove columns that don't need pivoting
for y in newlist:
    a = []
    for x in df.itertuples():
        a.append(xdf.loc[x.Index[0], y])
    df[str(y)] = pd.Series(a, index = df.index)
b = [x.Index[1] for x in df.itertuples()]
df['Year'] = pd.Series(b, index = df.index) # add a 'year' column
df.fillna(0, inplace = True) # fill all NULLS with 0
# save to a CSV
df.to_csv(path+'stuff2.csv',index_label = ['SPARTA Code', 'Year'], columns = ['Investment', 'EXT', 'Region', 'Asset Class', 'Country', 'City','Currency', 'O/B','IPP Date',
                                                  'Risk Class','Invested Capital Balances', 'Asset MTM Activity','Capex Activity', 'Acquisition Activity', 'Development Activity',
                                                  'Disposition Activity', 'Development Profit','Debt Balances','Refinancing Activity',
                                                  'Acquisition Activity (debt)','Development Activity (debt)','Disposition Activity (debt)', 'Equity  Balances'])