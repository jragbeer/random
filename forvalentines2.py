import pandas as pd
import xlrd
import re

def cleandf(idf):

    # idf.drop([('Risk Class', '2024.1')],1,inplace = True)# empty column
    new = []
    for col in idf.columns:
        if re.compile('Unnamed:').search(col[0]):
            new.append((col[1], col[1]))
        else:
            if re.compile('20').search(str(col[1])):
                z = int(re.search('[0-9]+', col[1])[0])
                pass
            else:
                z = col[1]
            new.append((col[0], z))
    idf.columns = pd.MultiIndex.from_tuples(new)
    return idf
def part1(idf):
    """

    returns a dataframe containing just the columns that don't need pivoting. This takes IPP Date and O/B from the Risk Class header and adds it to the
    others where data isn't pivoted.

    :param idf: cleaned dataframe
    :return: dataframe with just the columns that don't require pivoting
    """
    dataframe = pd.concat([pd.DataFrame(idf['Investment']), idf['Investment Name'], idf['EXT'], idf['Region'], idf['Asset Class'], idf['Country'], idf['City'],idf['Currency'],
                    idf['Risk Class', 'O/B'], idf['Risk Class', 'IPP Date']], 1)
    # renames a few of the columns, so that they aren't tuples  (more clarity, matches output file)
    listofcolumns = []
    for x in dataframe.columns:
        if type(x) == tuple:
            listofcolumns.append(x[1])
        else:
            listofcolumns.append(x)
    dataframe.columns = listofcolumns
    return dataframe

path = 'C:/Users/J_Ragbeer/PycharmProjects/other/data/finance/' #path on the CPU
df = pd.read_excel(path+"Staging Database Q1'19.xlsm", sheet_name = 'OXF Database', skiprows = 4, usecols="C:GD", header = [0,2], skipfooter = 21)
print(df.head(20).to_string())
df = cleandf(df)
# df.drop([x for x in list(df.columns) if x.startswith('Unnamed') ],1,inplace = True)
print(df.head(20).to_string())
unpivotcolumns = ['Managed (Y/N)','Dispo YR','IPP Date','O/B','Asset Class','EXT','Country', 'Investment', 'Investment Name', 'City', 'Currency', 'Region'] #list of columns that don't need pivoting

df.drop(unpivotcolumns,1,inplace = True)
print(df.head(20).to_string())
# for x in df.columns:
#     try:
#         print(str(x), re.search('[0-9]+', x)[0], re.search('\D+', x)[0])
#     except:
#         pass
xdf = part1(df) #unpivoted table
df = df.stack() #pivot the table
print(df.head(20).to_string())
# unpivotcolumns = ['IPP Date','O/B','Asset Class','EXT','Country', 'Investment', 'Investment Name', 'City', 'Currency', 'Region'] #list of columns that don't need pivoting
# df.drop(unpivotcolumns, 0, level = 1, inplace = True) #remove columns that don't need pivoting
# print(df.head().to_string())
# for y in unpivotcolumns:
#     a = []
#     for x in df.itertuples():
#         a.append(xdf.loc[x.Index[0], y])
#     df[str(y)] = pd.Series(a, index = df.index)
# b = [x.Index[1] for x in df.itertuples()]
# df['Year'] = pd.Series(b, index = df.index) # add a 'year' column
# df.fillna(0, inplace = True) # fill all NULLS with 0
# # save to a CSV
# df.to_csv(path+'stuff1.csv',index_label = ['SPARTA Code', 'Year'], columns = ['Investment', 'EXT', 'Region', 'Asset Class', 'Country', 'City','Currency', 'O/B','IPP Date',
#                                                   'Risk Class','Invested Capital Balances', 'Asset MTM Activity','Capex Activity', 'Acquisition Activity', 'Development Activity',
#                                                   'Disposition Activity', 'Development Profit','Debt Balances','Refinancing Activity',
#                                                   'Acquisition Activity (debt)','Development Activity (debt)','Disposition Activity (debt)', 'Equity  Balances'])
#
#
