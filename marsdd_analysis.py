import datetime
import os
import dotenv
import numpy as np
import pandas as pd
import polars as pl

# Pyarrow Strings (should be faster)
pd.options.future.infer_string = True
pd.options.mode.string_storage = "pyarrow"


path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")+ "/"
data_path = path + 'data/'
today = datetime.datetime.today()
print(today)

# load secrets to ENVs
dotenv.load_dotenv(path + '.env')

# location of IO files
in_file = data_path + "MaRS_Data_Analyst_-_Data_Set_for_Technical_Assignment.xlsx"
out_file = data_path + "output.parquet"

fdf = pd.read_excel(in_file, dtype_backend='pyarrow')
fdf['location_hq'] = fdf['HQ Location'].str.upper()
location_hq = []
for y in fdf['location_hq']:
    y = str(y)
    if 'CANADA' not in y:
        if 'UNITED KINGDOM' not in y:
            new_y = y + ', USA'
        else:
            new_y = y
    else:
        new_y = y
    location_hq.append(new_y)
fdf['location_hq'] = location_hq
fdf['location_country']  = fdf['location_hq'].str.split(',').str[-1].str.strip()

fdf = fdf.rename(columns = {'Companies':'company',
                            'Total Raised (in M) (in CAD)':"total_raised_cad",
'Last Financing Size (in M) (in CAD)':"last_financing_size_cad",
})
fdf.columns = [i.lower().replace(" ", "_") for i in fdf.columns]
fdf['last_financing_size_cad'] = (fdf['last_financing_size_cad'] * 1_000_000)
fdf['total_raised_cad'] = (fdf['total_raised_cad'] * 1_000_000)
fdf['employee_count'] =  fdf['employee_count'].fillna(1)
fdf['last_financing_date'] = pd.to_datetime(fdf['last_financing_date'])
fdf['year'] = fdf['last_financing_date'].dt.year

fdf = fdf.drop(columns = ['hq_location', 'description']).drop_duplicates().reset_index(drop=True)
fdf['active_investors'] = [str(i).split(',') for i in fdf['active_investors'].values]


# find duplicate rows/companies
duplicated = []
for col in ['company_id']:
    zz = pd.DataFrame(fdf['company_id'].value_counts())
    for w, p in zz.iterrows():
        if p['count'] > 1:
            # print(w)
            duplicated.append(w)
# all of the company_id that are duplicated across dataset, which ones are the same company or not
companies_to_be_reided = []
for x in duplicated:
    strikes = []
    dups = fdf[fdf['company_id'] == x]
    for col in ['company', 'employee_count', "total_raised_cad"]:
        z = dups['company'].value_counts()
        if z.max() == len(dups.index):
            pass
        else:
            strikes.append(col)
    if len(strikes) > 2:
        companies_to_be_reided.append(x)
# add "*" to the end of the company_id
for y in companies_to_be_reided:
    wow = fdf[fdf['company_id'] == y].index[0]
    fdf.at[wow, 'company_id'] = fdf[fdf['company_id'] == y]['company_id'].iloc[1] + "*"

print(fdf.sort_values(['employee_count']).to_string())

# QUESTION 1
# Which sector has seen the most financing growth over time?
question_1 = fdf.drop_duplicates(subset=['company', 'total_raised_cad'])
question_1 = question_1.groupby(['year','primary_industry_sector',]).agg({
    "company_id":"count",
    "total_raised_cad":"sum",
}).reset_index().sort_values(['primary_industry_sector', 'year'])
question_1 = question_1.rename(columns = {"company_id":"number_of_companies"})
question_1['raised_per_company_cad'] = question_1['total_raised_cad']/question_1['number_of_companies']
# switch to polars because syntax for window functions is easier and faster and then back to pandas
question_1 = (
  pl.from_pandas(question_1).with_columns([
       pl.col("total_raised_cad").pct_change().over("primary_industry_sector").mul(100).round(1).alias("total_raised_cad_yoy_pct_change"),
      pl.col("raised_per_company_cad").pct_change().over("primary_industry_sector").mul(100).round(1).alias("raised_per_company_cad_yoy_pct_change")
    ])
).to_pandas()
question_1['year'] = question_1['year'].astype(int)
question_1['total_raised_cad_total_pct_change'] = question_1.groupby('primary_industry_sector')['total_raised_cad'].apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100)).values
question_1['raised_per_company_cad_total_pct_change'] = question_1.groupby('primary_industry_sector')['raised_per_company_cad'].apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100)).values
print(question_1.to_string())

# QUESTION 2
# What is the mean & median financing for Early Stage VC and Late Stage VC for each country?



# QUESTION 3
# What is the mean & median number of employees per venture for each country?
question_3 = fdf.drop_duplicates(subset=['company', 'total_raised_cad']).sort_values("employee_count", ascending=True)
# find outliers in # of employees and remove
question_3['employee_count_dif'] = np.round(100*question_3['employee_count'].pct_change(),1)
question_3 = question_3[question_3["employee_count_dif"] < 2000]
question_3 = question_3.groupby(['location_country','year',]).agg(
venture_count=pd.NamedAgg(column="company", aggfunc="count"),
employee_count_sum=pd.NamedAgg(column="employee_count", aggfunc="sum"),
employee_count_median=pd.NamedAgg(column="employee_count", aggfunc="median"),
employee_count_mean=pd.NamedAgg(column="employee_count", aggfunc="mean"),
).reset_index().sort_values(['location_country',])
print(question_3.to_string())


# QUESTION 4
# Provide any other data visualizations and commentary/insights you think relevant

end = datetime.datetime.now()
print(end-today)