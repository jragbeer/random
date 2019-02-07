import pandas as pd
import xlrd
import re

def cleandf(idf):
    new = []
    # idf.drop([("Disposition Debt Activity", 'Disposition Debt Activity 2024.1'), ('Risk Class', 'Risk Class 2025.1'),
    #           ('Equity  Balances', 'Equity  Balances 2024.1')], 1, inplace=True)
    idf.drop([x for x in list(idf.columns) if re.search(r'\.1', x[1])], 1, inplace=True)

    for col in idf.columns:
        if re.compile('Unnamed:').search(col[0]):
            new.append((col[1], col[1]))
        else:
            if re.compile('20').search(str(col[1])):
                z = int(re.search('[0-9]+', col[1])[0])
                pass
            elif re.compile('\n').search(str(col[1])):
                z = str(col[1]).replace('\n', ' ')
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
                    idf['Risk Class', 'O/B'], idf['Risk Class', 'IPP Date'],
                           idf['Equity  Balances', 'Managed (Y/N)'],
                           idf['Step Up / Down', 'Dispo YR'],idf['Step Up / Down', 'Recap Y/N'],idf['Step Up / Down', 'AUM % Post Dispo'],
                           ], 1)
    # renames a few of the columns, so that they aren't tuples  (more clarity, matches output file)
    listofcolumns = []
    for x in dataframe.columns:
        if type(x) == tuple:
            listofcolumns.append(x[1])
        else:
            listofcolumns.append(x)
    dataframe.columns = listofcolumns
    return dataframe

path = 'C:/Users/J_Ragbeer/PycharmProjects/nlp/' #path on the CPU
df = pd.read_excel(path+"Staging Database Q1'19.xlsm", sheet_name = 'OXF Database', skiprows = 4, usecols="C:GD", header = [0,2], skipfooter = 21)
df = cleandf(df)
unpivotcolumns = ['O/B','IPP Date','Managed (Y/N)','Dispo YR','AUM % Post Dispo','Recap Y/N','Asset Class','EXT','Country', 'Investment', 'Investment Name', 'City', 'Currency', 'Region'] #list of columns that don't need pivoting
xdf = part1(df).replace('-', 0) #unpivoted table
df = df.stack() #pivot the table
df.drop([' ', 'Step Up / Down'],1,inplace = True)
df.drop(unpivotcolumns, 0, level = 1, inplace = True) #remove columns that don't need pivoting
for y in unpivotcolumns:
    a = []
    for x in df.itertuples():
        a.append(xdf.loc[x.Index[0], y])
    df[str(y)] = pd.Series(a, index = df.index)
df.fillna(0, inplace = True) # fill all NULLS with 0
# save to a CSV
df.to_csv(path+'feb.csv',index_label = ['SPARTA Code', 'Year'],
 # columns = ['Investment', 'EXT', 'Region', 'Asset Class', 'Country', 'City','Currency', 'O/B','IPP Date',
 #                                                  'Risk Class','Invested Capital Balances', 'Asset MTM Activity','Capex Activity', 'Acquisition Activity', 'Development Activity',
 #                                                  'Disposition Activity', 'Development Profit','Debt Balances','Refinancing Activity',
 #                                                  'Acquisition Activity (debt)','Development Activity (debt)','Disposition Activity (debt)', 'Equity  Balances']
)
