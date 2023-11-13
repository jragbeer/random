import datetime
import os
import dotenv
import numpy as np
import pandas as pd
import polars as pl

# Pyarrow Strings (should be faster)
pd.options.future.infer_string = True
pd.options.mode.string_storage = "pyarrow"
pd.options.display.float_format = '{:.2f}'.format

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")+ "/"
data_path = path + 'data/'
today = datetime.datetime.today()
print(today)

# load secrets to ENVs
dotenv.load_dotenv(path + '.env')

# location of IO files
in_file = data_path + "MaRS_Data_Analyst_-_Data_Set_for_Technical_Assignment.xlsx"

def make_q1_data(input_df: pd.DataFrame) -> pd.DataFrame:
    question_1 = input_df.copy().drop_duplicates(subset=['company', 'total_raised_cad'])
    question_1 = question_1.groupby(['year','primary_industry_sector',]).agg({
        "company_id":"count",
        "total_raised_cad":"sum",
    }).reset_index().sort_values(['primary_industry_sector', 'year'])
    # rename columns for easier analysis
    question_1 = question_1.rename(columns = {"company_id":"number_of_companies"})
    # find the per company $ raised values
    question_1['raised_per_company_cad'] = question_1['total_raised_cad']/question_1['number_of_companies']
    # switch to polars because syntax for window functions is easier and faster and then back to pandas
    question_1 = (
      pl.from_pandas(question_1).with_columns([
          # find the YoY % change for each column
           pl.col("total_raised_cad").pct_change().over("primary_industry_sector").mul(100).round(1).alias("total_raised_cad_yoy_pct_change"),
          pl.col("raised_per_company_cad").pct_change().over("primary_industry_sector").mul(100).round(1).alias("raised_per_company_cad_yoy_pct_change")
        ])
    ).to_pandas()
    question_1['year'] = question_1['year'].astype(int)
    # find the total % change from year1 of analysis to each year, not YoY
    question_1['total_raised_cad_total_pct_change'] = question_1.groupby('primary_industry_sector')['total_raised_cad'].apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100)).values
    question_1['raised_per_company_cad_total_pct_change'] = question_1.groupby('primary_industry_sector')['raised_per_company_cad'].apply(lambda x: x.div(x.iloc[0]).subtract(1).mul(100)).values
    # rename columns for better presentation
    question_1 = question_1.rename(columns = {
        'year':"Year",
        "number_of_companies":"No. of Companies",
        "primary_industry_sector":"Sector",
        "total_raised_cad": "Total Raised ($ CAD)",
        "raised_per_company_cad": "Raised per Company ($ CAD)",
        "total_raised_cad_yoy_pct_change": "Total Raised - YoY % Change ($ CAD)",
        "raised_per_company_cad_yoy_pct_change": "Raised per Company - YoY % Change ($ CAD)",
        "total_raised_cad_total_pct_change": "Total Raised - Total % Change  ($ CAD)",
        "raised_per_company_cad_total_pct_change": "Raised per Company - Total % Change ($ CAD)",
    })
    return question_1

def make_q2_data(input_df: pd.DataFrame) -> pd.DataFrame:
    # assumptions on what type of financing is early vs later stage
    early_stages = ["Angel (individual)", "Early Stage VC", "Seed Round", "Equity Crowdfunding"]
    later_stages = ["Accelerator/Incubator", "Later Stage VC", "PE Growth/Expansion"]
    # remove rows where there isn't an obvious location
    question_2 = input_df.copy().sort_values("last_financing_deal_type", ascending=True)
    question_2['location_hq'] = [x if x else np.nan for x in question_2['location_hq']]
    question_2 = question_2.dropna(subset=['location_hq'])
    # assign Early or Late stage to rows, drop rows that aren't Early or Late stage
    ww = []
    for y in question_2.itertuples():
        if y.last_financing_deal_type in early_stages:
            ww.append('Early')
        elif y.last_financing_deal_type in later_stages:
            ww.append("Late")
        else:
            ww.append(np.nan)
    question_2['stage_type'] = ww
    question_2 = question_2[question_2['stage_type'].isin(["Early", "Late"])]

    # find different metrics for each country/stage type by using groupby aggregations
    question_2 = question_2.groupby(['location_country','stage_type',]).agg(
    venture_count=pd.NamedAgg(column="company", aggfunc="count"),
    last_financing_size_cad_sum=pd.NamedAgg(column="last_financing_size_cad", aggfunc="sum"),
    last_financing_size_cad_median=pd.NamedAgg(column="last_financing_size_cad", aggfunc="median"),
    last_financing_size_cad_mean=pd.NamedAgg(column="last_financing_size_cad", aggfunc="mean"),
    employee_count_mean=pd.NamedAgg(column="employee_count", aggfunc="mean"),
    employee_count_sum=pd.NamedAgg(column="employee_count", aggfunc="sum"),
    active_investors_count_sum=pd.NamedAgg(column="active_investors_count", aggfunc="sum"),
    ).reset_index().sort_values(['location_country',])

    # round all numbers up and use ints instead of floats for easier viewing
    for x in question_2.select_dtypes(include='number'):
        question_2[x] = (np.ceil(question_2[x])).astype(int)

    # rename columns for better presentation
    question_2 = question_2.rename(columns = {
        "location_country":"Country",
        "stage_type":"Stage",
        "venture_count": "No. of Ventures",
        "last_financing_size_cad_sum": "Sum - Last Financing Size",
        "last_financing_size_cad_median": "Median - Last Financing Size",
        "last_financing_size_cad_mean": "Mean - Last Financing Size",
        "employee_count_mean": "Mean - Empl. Count",
        "employee_count_sum": "Sum - Empl. Count",
        "active_investors_count_sum": "No. of Active Investors",
    })
    question_2 = question_2.set_index(['Stage', "Country"]).stack().reset_index()
    # rename columns for better presentation
    question_2.columns = ['Stage', "Country", "Feature", "Value"]
    return question_2

def make_q3_data(input_df: pd.DataFrame) -> pd.DataFrame:
    question_3 = input_df.copy().drop_duplicates(subset=['company', 'total_raised_cad']).sort_values("employee_count",
                                                                                                     ascending=True)
    # find outliers in # of employees and remove them
    question_3['employee_count_dif'] = np.round(100 * question_3['employee_count'].pct_change(), 1)
    question_3 = question_3[question_3["employee_count_dif"] < 2000]

    question_3 = question_3.groupby(['location_country', 'year', ]).agg(
        venture_count=pd.NamedAgg(column="company", aggfunc="count"),
        employee_count_sum=pd.NamedAgg(column="employee_count", aggfunc="sum"),
        employee_count_median=pd.NamedAgg(column="employee_count", aggfunc="median"),
        employee_count_mean=pd.NamedAgg(column="employee_count", aggfunc="mean"),
    ).reset_index().sort_values(['location_country', ])

    # rename columns for better presentation
    question_3 = question_3.rename(columns={
        'year': "Year",
        "location_country": "Country",
        "venture_count": "No. of Ventures",
        "employee_count_sum": "Sum - Empl. Count",
        "employee_count_median": "Median - Empl. Count",
        "employee_count_mean": "Mean - Empl. Count",
    })
    question_3 = question_3.set_index(['Year', "Country"]).stack().reset_index()
    # rename columns for better presentation
    question_3.columns = ['Year', "Country", "Feature", "Value"]
    question_3['Value'] = np.ceil(question_3['Value'])
    return question_3

def make_q4_data(input_df: pd.DataFrame) -> pd.DataFrame:
    question_4 = input_df.copy().drop_duplicates(subset=['company', 'total_raised_cad']).sort_values("location_hq", ascending=True)
    question_4['location_hq'] = [x if x else np.nan for x in question_4['location_hq']]
    question_4 = question_4.dropna(subset=['location_hq'])
    # we want the info aggregated by year and also for ALL, so split the groupby analysis then concat later on
    # groupby by year
    tmp1_q4 = question_4.groupby(['year','location_hq']).agg(
    venture_count=pd.NamedAgg(column="company", aggfunc="count"),
    total_raised_cad_sum=pd.NamedAgg(column="total_raised_cad", aggfunc="sum"),
    country=pd.NamedAgg(column="location_country", aggfunc="max"),
    ).reset_index().sort_values(['year',])
    tmp1_q4["year"] = (tmp1_q4["year"].astype(int)).astype(str)
    tmp1_q4["total_raised_cad_sum"] = tmp1_q4["total_raised_cad_sum"].astype(int)
    # groupby all
    tmp_q4 = question_4 = question_4.groupby(['location_hq']).agg(
    venture_count=pd.NamedAgg(column="company", aggfunc="count"),
    total_raised_cad_sum=pd.NamedAgg(column="total_raised_cad", aggfunc="sum"),
    country=pd.NamedAgg(column="location_country", aggfunc="max"),
    ).reset_index()
    tmp_q4['year'] = 'Total'
    tmp_q4["total_raised_cad_sum"] = tmp_q4["total_raised_cad_sum"].astype(int)
    # concatenate both analysis
    question_4 = pd.concat([tmp_q4, tmp1_q4])
    # rename columns for better presentation
    question_4 = question_4.rename(columns = {
        "location_hq":"HQ",
        'year':"Year",
        "venture_count": "No. of Ventures",
        "total_raised_cad_sum": "Total Raised ($ CAD)",
        'country':"Country",
    })
    return question_4

def clean_dataset(fdf: pd.DataFrame) -> pd.DataFrame:
    # put USA for all locations without Canada / UK
    # remake the HQ Location column with updated Country values as well
    fdf['location_hq'] = fdf['HQ Location'].str.upper()
    location_hq = []
    for y in fdf['location_hq']:
        if pd.notnull(y):
            y = str(y)
        else:
            y = ''
        if 'CANADA' not in y:
            if 'UNITED KINGDOM' not in y:
                if y:
                    new_y = y + ', USA'
                else:
                    new_y = ''
            else:
                new_y = y
        else:
            new_y = y
        location_hq.append(new_y)
    fdf['location_hq'] = location_hq
    # find the country in each HQ Location by
    fdf['location_country']  = fdf['location_hq'].str.split(',').str[-1].str.strip()
    # change column names so python analysis is easier
    fdf = fdf.rename(columns = {'Companies':'company',
                                'Total Raised (in M) (in CAD)':"total_raised_cad",
    'Last Financing Size (in M) (in CAD)':"last_financing_size_cad",
    })
    fdf.columns = [i.lower().replace(" ", "_") for i in fdf.columns]
    # use the number in millions instead of the proxy
    fdf['last_financing_size_cad'] = (fdf['last_financing_size_cad'] * 1_000_000)
    fdf['total_raised_cad'] = (fdf['total_raised_cad'] * 1_000_000)
    # all companies must have at least 1 employee so fill all missing values with 1
    fdf['employee_count'] =  fdf['employee_count'].fillna(1)
    # find the most recent year of financing for each venture
    fdf['last_financing_date'] = pd.to_datetime(fdf['last_financing_date'])
    fdf['year'] = fdf['last_financing_date'].dt.year
    # drop unnecessary columns
    fdf = fdf.drop(columns = ['hq_location', 'description']).drop_duplicates().reset_index(drop=True)
    # create a few columns with the amount of investors and convert the long string to a list for easier analysis
    cntt = []
    ai = []
    for i in fdf['active_investors'].values:
        p = str(i).split(',')
        ai.append(p)
        cntt.append(len(p))
    fdf['active_investors_count'] = cntt
    fdf['active_investors'] = ai

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
    # add "*" to the end of the company_id where it is possibly a mistake with the company_id
    for y in companies_to_be_reided:
        wow = fdf[fdf['company_id'] == y].index[0]
        fdf.at[wow, 'company_id'] = fdf[fdf['company_id'] == y]['company_id'].iloc[1] + "*"
    fdf=fdf.sort_values(['last_financing_deal_type'])
    fdf['raised_per_investor_cad'] = fdf['total_raised_cad']/fdf['active_investors_count']
    # cleaned dataset is ready for further analysis
    return fdf


fdf = pd.read_excel(in_file, dtype_backend='pyarrow')
fdf = clean_dataset(fdf)
# print(fdf.to_string())
fdf.to_csv(data_path + "marsdd_cleaned_dataset.csv", index = False, )

# QUESTION 1
# Which sector has seen the most financing growth over time?
question_1 = make_q1_data(fdf)
# print(question_1.to_string())
question_1.to_csv(data_path + "marsdd_question_1b.csv", index = False, )

# QUESTION 2
# What is the mean & median financing for Early Stage VC and Late Stage VC for each country?
question_2 = make_q2_data(fdf)
# print(question_2.to_string())
question_2.to_csv(data_path + "marsdd_question_2.csv", index = False, )

# QUESTION 3
# What is the mean & median number of employees per venture for each country?
question_3 = make_q3_data(fdf)
# print(question_3.to_string())
question_3.to_csv(data_path + "marsdd_question_3a.csv", index = False, )

# QUESTION 4
# Provide any other data visualizations and commentary/insights you think relevant
# where are the best regions in the world for startups?
question_4 = make_q4_data(fdf)
# print(question_4.to_string())
question_4.to_csv(data_path + "marsdd_question_4.csv", index = False, )

end = datetime.datetime.now()
print(end-today)
