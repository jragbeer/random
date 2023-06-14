import datetime
import json
import time
import numpy as np
import pandas as pd
import os
import psutil
import pymongo
import datetime
import re, os, sys
import traceback
import pickle
from pprint import pprint
import bs4 as bs
import pdfkit
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options as firefox_options
# from selenium.webdriver.chrome.options import Options as chrome_options
import platform
from dateutil import parser
import sqlite3
import calendar
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib
import sqlalchemy
from typing import Iterable, Optional, Callable
import dask
from dask.distributed import get_client
import subprocess
from azure.storage.blob import BlobClient
from azure.storage.blob import BlobServiceClient
from io import BytesIO
from tqdm import tqdm
import pymysql
import mimetypes
import itertools
from meteostat import Hourly, Stations
import socket


path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")+ "/"
data_path = path + 'data/'
today = datetime.datetime.today()
print(today)

# secrets in a separate file
with open(path + "secrets.json") as f:
    secrets = json.load(f)

# logger
dagster_logger = logging.getLogger("dagster_logger")
dagster_logger.setLevel(logging.INFO)
# create console handler
handler = logging.StreamHandler()
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s, %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
dagster_logger.addHandler(handler)
# create console handler
handler2 = logging.FileHandler(data_path + "dagster_logger.log")
# add the handler to the logger
dagster_logger.addHandler(handler2)


# Azure BLOB Storage
adls_container_name = secrets["adls_container_name"]
adls_connection_string = secrets["adls_connection_string"]
adls_blob_account_endpoint = secrets["adls_blob_account_endpoint"]

# MYSQL Connection Strings
home_connection_string = f"mysql+pymysql://{secrets['local_db_username']}:{secrets['local_db_password']}@{secrets['local_db_address']}:{secrets['local_db_port']}/home"
# MYSQL Engines
home_engine = sqlalchemy.create_engine(home_connection_string)

# Local MongoDB
mongo_client = pymongo.MongoClient('localhost', 27017)
db_fmp = mongo_client['Finance_FMP_Information']
db_yfinance = mongo_client['Finance_YFinance_Information']

dbs = {
    'home':home_engine,
      
       'mongo':mongo_client}


client = pymongo.MongoClient('localhost', 27017)
mongo_db = client['dagster_test']




# UTILITY

def do_work(list_of_tasks:Iterable, wait_time:float=1) -> int:
    """
    This function simulates doing work and returning a number
    :param list_of_tasks: Iterable for a list of tasks to do that take *wait_time* seconds
    :param wait_time: Float or Int for the amount of time the task should take in seconds
    :return: a randomly generated integer between 1 and 10
    """
    for x in list_of_tasks:
        dagster_logger.info(x)
        time.sleep(wait_time)

    return np.random.randint(0,10)
def backup_databases():
    for finance_db in [
        "finance_1mins",
        "finance_5mins",
        "finance_daily",
        "finance_fundamental_data",
        "finance_standard",
                       ]:
        dagster_logger.info(f"{finance_db} dump starting now")
        t = rf"cd C:\Program Files\MySQL\MySQL Server 8.0\bin\ && mysqldump.exe -hlocalhost -u{secrets['local_db_username']} -p{secrets['local_db_password']} {finance_db} > {data_path + finance_db}_dump_latest.sql"
        execute_cmd(t)
        dagster_logger.info(f"{finance_db} complete in {datetime.datetime.now()-today} ")
def copy_backups_to_cloud():
    for finance_db in [
        "finance_1mins",
        "finance_5mins",
        "finance_daily",
        "finance_fundamental_data",
        "finance_standard",
                       ]:
        dagster_logger.info(f"{finance_db} migrating to BLOB")
        adls_upload_file(data_path + f"{finance_db}_dump_latest.sql", f"database_backups/{finance_db}_dump_latest.sql")
        dagster_logger.info(f"{finance_db} migration to BLOB complete.")

def table_drop_duplicates(list_of_table_names: list, engine: Optional[sqlalchemy.engine.base.Engine]=None, database:str='5mins'):

    if engine:
        new_engine = engine
    else:
        new_engine = sqlalchemy.create_engine(f"mysql+pymysql://{secrets['local_db_username']}:{secrets['local_db_password']}@127.0.0.1/finance_{database}")

    for ii, table_name in enumerate(tqdm(list_of_table_names)):
        try:
            if ii%25 == 0:
                dagster_logger.info(f'Dropping Duplicates on {table_name}')
            tmp_df = pd.read_sql(f'select * from ``{table_name}``', new_engine)
            try:
                tmp_df = tmp_df.sort_values('Datetime')
            except:
                tmp_df = tmp_df.sort_values('Date')
            try:
                tmp_df['Datetime'] = tmp_df['Datetime'].apply(lambda x: x.replace(tzinfo=None))
            except:
                try:
                    tmp_df['Date'] = tmp_df['Date'].apply(lambda x: x.replace(tzinfo=None))
                except:
                    pass
            tmp_df.drop_duplicates(inplace=True)
            tmp_df.to_sql(f"{table_name}", new_engine, index=False, if_exists='replace')
        except:
            dagster_logger.info(error_handling())
def db_drop_duplicates(engine: Optional[sqlalchemy.engine.base.Engine]=None, database: str = '5mins', num_splits:int = 4 ):
    # print time this function starts
    now = datetime.datetime.now()
    dagster_logger.info(now)
    if engine:
        new_engine = engine
    else:
        new_engine = sqlalchemy.create_engine(f"mysql+pymysql://{secrets['local_db_username']}:{secrets['local_db_password']}@127.0.0.1/finance_{database}")
    list_of_tables = list(np.ravel(pd.read_sql(f""" SELECT table_name FROM information_schema.tables where table_schema = 'finance_{database}';""", new_engine).values))
    input_list = list_of_tables
    """
    Split the input list into multiple sublists using Dask and execute the provided function on each split list.

    :param input_list: The input list to be split.
    :param func: The function to be executed on each split list.
    :param num_splits:  The number of splits to create from the input list.
    :return: None
    """
    # Calculate the size of each split
    split_size = len(input_list) // num_splits

    # Create the splits using Dask
    splits = [input_list[i:i + split_size] for i in range(0, len(input_list), split_size)]
    dagster_logger.info(f"{num_splits} splits each of around {split_size} size made.")

    running_cluster_location = pd.read_sql("""SELECT var, value FROM
     environment_variables WHERE 
     var = 'running_dask_cluster'""",  sqlalchemy.create_engine(home_connection_string))['value'].values[0]

    client = get_client(running_cluster_location)
    dagster_logger.info(str(running_cluster_location))
    dagster_logger.info(f"Using Dask Cluster: {str(client)}")

    # Create Dask delayed objects for each split and apply the provided function
    delayed_results = [dask.delayed(table_drop_duplicates)(list_of_table_names=split, database=database) for split in splits]

    # Compute the results using Dask's parallel processing capabilities
    dask.compute(*delayed_results)
    print("Shutting Down Dask Cluster")
    client.shutdown()

    dagster_logger.info(datetime.datetime.now()-today)

def convert_html_to_pdf(html_file, pdf_file_name):
    # Define path to wkhtmltopdf.exe
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # Point pdfkit configuration to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    # Convert HTML file to PDF
    pdfkit.from_file(html_file, output_path=pdf_file_name, configuration=config)
def wrap_in_paragraphs(txt:str, colour:str="DarkSlateBlue", size:int=4) -> str:
    """
    This function wraps text in paragraph, bold and font tags - according to the colour and size given.
    :param text: text to wrap in tags_
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""

def sendemail_(TEXT:str, HTML:str, SUBJECT:str = 'Daily Market Update', filename: Optional[str] = None, TO: Iterable = (secrets['my_email'],)):
    """

    This function sends emails to the email list depending on the para

    :param TEXT: text to send in an email
    :param HTML: text to send in an email, but in HTML (default)
    :param SUBJECT: integer that indicates if this is the email sent weekly (start of the week, monday at 7am)
    :param filename: if a file name is present, attach the file to the email and send it
    :return:
    """
    # This is a temporary fix. Be careful of malicious links
    # context = ssl._create_unverified_context()
    TO = list(TO)

    senders_email = secrets['senders_email']  # senders email
    senders_pswd = secrets['senders_pw'] # senders password

    # current date, and a date 5 days away
    curtime = datetime.datetime.now().date()
    week_from_today = curtime + datetime.timedelta(days=5)

     # Gmail Sign In
    gmail_sender = senders_email
    gmail_passwd = senders_pswd

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    # add the 2 parts of the email (one plain text, one html)
    part1 = MIMEText(TEXT, 'plain')
    part2 = MIMEText(HTML, 'html')
    # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part1)
    msg.attach(part2)

    if filename:
        ctype, encoding = mimetypes.guess_type(filename)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)

        with open(filename) as fp:
            attachment = MIMEText(fp.read(), _subtype=subtype)
        attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(filename))
        msg.attach(attachment)

    # connect to the GMAIL server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # login to the GMAIL server
    server.login(gmail_sender, gmail_passwd)

    try:
        # send email and confirm email is sent / time it is sent
        server.sendmail(gmail_sender, TO, msg.as_string())
        logging.info(str(curtime) + ' email sent')
    except Exception as e:
        # print error if not sent, and confirm it wasn't sent
        dagster_logger.info(str(e))
        dagster_logger.info(error_handling())
        dagster_logger.info(str(curtime) + ' error sending mail')

    server.quit()
def update_json_file(file_location: str, dictionary: dict) -> None:
    """Updates a JSON file with a dictionary key.

    Args:
        file_location (str): The file path of the JSON file.
        dictionary (dict): The dictionary to update the JSON file with.

    Returns:
        None: The function does not return a value.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If the JSON file has an invalid format.
        Exception: If any other error occurs during the update process.
    """
    try:
        # Load the JSON file
        with open(file_location, 'r') as file:
            data = json.load(file)

        # Update the JSON data with the dictionary
        data.update(dictionary)

        # Write the updated data back to the JSON file
        with open(file_location, 'w') as file:
            json.dump(data, file, indent=4)

        dagster_logger.info("Secrets JSON file updated successfully.")
    except FileNotFoundError:
        dagster_logger.info("File not found.")
    except json.JSONDecodeError:
        dagster_logger.info("Invalid JSON file format.")
    except Exception as e:
        dagster_logger.info(f"An error occurred: {str(e)}")
def error_handling() -> str:
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()

def execute_confirm_wait(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
            # dagster_logger.info(f"{args}, {kwargs} is done! ({func.__name__})")
        except TypeError as e:
            func()
            # dagster_logger.info(f"it's done! ({func.__name__})")
        time.sleep(0.05)
        return func
    return inner

def execute_script_with_cmd(script_name:str) -> str:
    output = execfile(script_name)
    dagster_logger.info(str(output))
    return str(output)
def execute_cmd(commands: str) -> str:
    try:
        out_var = subprocess.Popen(commands, shell=True)
        dagster_logger.info(f"{commands} | Running...")

        (output, err) = out_var.communicate()

        # Decode the output and error from bytes to string
        # Print the output and error
        if output:
            output = output.decode('utf-8')
            print("Output:")
            # This will give you the output of the command being executed
            dagster_logger.info("Command output: " + output.decode())

        if err:
            err = err.decode('utf-8')
            print("Error:")
            print(err)

        return output
    except:
        dagster_logger.info(error_handling())
        return "Did not run"

def execfile(filepath, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)


def process_list_with_dask(input_list: list, func: Callable, num_splits: int) -> None:
    """
    Split the input list into multiple sublists using Dask and execute the provided function on each split list.

    :param input_list: The input list to be split.
    :param func: The function to be executed on each split list.
    :param num_splits:  The number of splits to create from the input list.
    :return: None
    """
    # Calculate the size of each split
    split_size = len(input_list) // num_splits

    # Create the splits using Dask
    splits = [input_list[i:i + split_size] for i in range(0, len(input_list), split_size)]
    dagster_logger.info(f"{num_splits} splits each of around {split_size} size made.")

    running_cluster_location = pd.read_sql("""SELECT var, value FROM
     environment_variables WHERE 
     var = 'running_dask_cluster'""",  sqlalchemy.create_engine(home_connection_string))['value'].values[0]

    client = get_client(running_cluster_location)
    dagster_logger.info(str(running_cluster_location))
    dagster_logger.info(f"Using Dask Cluster: {str(client)}")

    # Create Dask delayed objects for each split and apply the provided function
    delayed_results = [dask.delayed(func)(split) for split in splits]

    # Compute the results using Dask's parallel processing capabilities
    dask.compute(*delayed_results)
    # dagster_logger.info("Shutting Down Dask Cluster")
    # client.shutdown()

def parse_date_features(
    idf_: pd.DataFrame, holidays_: Optional[list] = None
) -> pd.DataFrame:
    """
    This function adds several datetime-like features to the input dataframe and returns the dataframe. Optionally, a
    column is made if holiday dates are passed in. This function also creates cyclical hour and month variables.
    :param idf_: an input dataframe for ML that has a datetime index
    :param holidays_: a list of holidays for that region, this parameter is optional
    :return: the dataframe with new datetime-specific columns
    """
    idf = idf_.copy()
    idf.index = pd.to_datetime(idf.index)
    idf["hour"] = idf.index.hour
    idf["month"] = idf.index.month
    idf["year"] = idf.index.year
    idf["weekday"] = idf.index.weekday  # 0 is sunday
    idf["hour_sin"] = np.sin(idf.hour * (2.0 * np.pi / 24))
    idf["hour_cos"] = np.cos(idf.hour * (2.0 * np.pi / 24))
    idf["month_sin"] = np.sin((idf.month - 1) * (2.0 * np.pi / 12))
    idf["month_cos"] = np.cos((idf.month - 1) * (2.0 * np.pi / 12))
    if holidays_:
        idf["holiday"] = [1 if x in holidays_ else 0 for x in idf.index]
    return idf

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    new_iter = list(iterable)  # allows duplicate elements
    return itertools.chain.from_iterable(itertools.combinations(new_iter, r) for r in range(1, len(new_iter) + 1))




# WEATHER Functions
def hmdxx(temp, dew_temp):
    """

    This function returns the humidex reading given the air temp and dew temp.

    :param temp: air temp in Celsius
    :param dew_temp: dewpoint in Celsius
    :return: humidex reading as a float
    """
    return temp + (
        0.5555
        * (6.11 * np.exp(5417.7530 * ((1 / 273.16) - (1 / (273.15 + dew_temp)))) - 10)
    )

# download data from MeteoStat (INTL)
def weather_get_historical_data_for_all_intl(start_date=None, end_date=None):
    """
    Get all of the weather data from meteostat API for each of the items in weather_lat_long_map
    :return: a dictionary with Name of Location: df
    """
    weather_datas = {}
    large = []
    if start_date:
        first_date = start_date
    else:
        first_date = today-datetime.timedelta(days=31)
    if end_date:
        second_date = start_date
    else:
        second_date = today
    engine = sqlalchemy.create_engine(home_connection_string)
    weather_intl_cities_df = pd.read_sql("select * from weather_intl_city_locations", engine)
    for z in weather_intl_cities_df.itertuples():
        print(z.location)
        station = Stations().nearby(z.latitude, z.longitude).fetch(1)
        # Get hourly data
        weather_data = (
            Hourly(
                station,
                first_date,
                second_date,
                timezone="GMT",
                model=False,
            )
            .fetch()
            .reset_index()
        )
        weather_data["humidex"] = pd.Series(
            [
                np.round(
                    hmdxx(
                        x.temp,
                        x.dwpt,
                    ),
                    2,
                )
                for x in weather_data.itertuples()
            ],
            index=weather_data.index,
        )
        weather_data = weather_data.drop(
            columns=["snow", "tsun", "wpgt", "coco",
                     'wdir', 'wspd', 'pres']
        ).dropna(subset=["temp", "dwpt", "rhum"])
        weather_data = weather_data.rename(columns = {"temp":"temperature",
                                                      "time": "datetime_utc",
                                                      "dwpt": "dewpoint_temperature",
                                                      "rhum": "relative_humidity",
                                                      'prcp':'precipitation_mm',
                                                      })
        for number in range(10, 24):
            weather_data[f"hdh_{number}"] = [
                number - x if x < number else 0 for x in weather_data["temperature"]
            ]
            weather_data[f"cdh_{number}"] = [
                x - number if x > number else 0 for x in weather_data["temperature"]
            ]
        weather_data.columns = [i.lower() for i in weather_data.columns]
        # get the date features
        weather_data = (
            parse_date_features(weather_data.set_index("datetime_utc"))
            .reset_index()
            .sort_values(
                [
                    "datetime_utc",
                ]
            )
        )
        weather_data['location'] = z.location
        weather_data['latitude'] = z.latitude
        weather_data['longitude'] = z.longitude
        weather_datas[z.location] = weather_data
        large.append(weather_data)

    large_df = pd.concat(large)
    with engine.begin() as conn:
        large_df.to_sql(
            f"weather_historical_hourly",
            conn,
            index=False,
            if_exists="append",
        )
    return weather_datas

# download Weather data from Environment Canada
def weather_get_can_historical_data_daily(stationid, year=None):
    """
    grab most recent data (this year) from Weather Canada in csv form. The dataframe is sorted, column datatypes assigned
    and many columns are dropped.

    :param stationid: station ID to grab from
    :param year: year
    :return: returns a dataframe that's cleaned
    """

    date = datetime.datetime.now()
    if year:
        datastring = f"http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&time=utc&stationID={stationid}&Year={year}&Month=1&Day=14&timeframe=2&submit=Download+Data.csv"
    else:
        datastring = f"http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&time=utc&stationID={stationid}&Year={date.year}&Month=1&Day=14&timeframe=2&submit=Download+Data.csv"
    df = pd.read_csv(datastring)
    df.columns = df.columns.str.replace(r"\(°C\)", "")
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.upper()
    cols = [
        "Date/Time",
        "Year",
        "Month",
        "Day",
        "Max Temp",
        "Min Temp",
        "Mean Temp",
        "Total Precip (mm)",
    ]
    Wdata = df[[x.upper() for x in cols]]
    Wdata.rename(
        {
            "DATE/TIME": "DATETIME",
            "MAX TEMP": "MAX_TEMP",
            "MIN TEMP": "MIN_TEMP",
            "MEAN TEMP": "MEAN_TEMP",
            "TOTAL PRECIP (MM)": "TOTAL_PRECIP_MM",
        },
        axis="columns",
        inplace=True,
    )
    Wdata.dropna(thresh=4, inplace=True)
    Wdata.fillna(method="ffill", inplace=True)
    Wdata.fillna(method="bfill", inplace=True)
    Wdata.set_index("DATETIME", inplace=True)
    Wdata.index = pd.to_datetime(Wdata.index)
    Wdata = Wdata[Wdata.index < datetime.datetime.now() - datetime.timedelta(days=1)]
    Wdata = Wdata.sort_index()
    return Wdata


def weather_get_can_historical_data_hourly(stationid, year=None, month=None) -> pd.DataFrame:
    """
    grab most recent data (this month) from Weather Canada in csv form. The dataframe is sorted, column datatypes assigned
    and extra columns HOUR and HUMIDEX are added, while many are dropped

    :param stationid: station ID to grab from
    :param year: year
    :param month: month
    :return: returns a dataframe that's cleaned
    """
    try:
        date = datetime.datetime.now()
        if year and month:
            datastring = f"https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&time=UTC&stationID={stationid}&Year={year}&Month={month}&Day=14&timeframe=1&submit=Download+Data.csv"
        else:
            datastring = f"https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&time=UTC&stationID={stationid}&Year={date.year}&Month={date.month}&Day=14&timeframe=1&submit=Download+Data.csv"
        df = pd.read_csv(
            datastring,
            encoding="utf-8",
        )
        df.columns = df.columns.str.replace(r"\(°C\)", "", regex=True)
        df.columns = df.columns.str.replace(r"\(%\)", "", regex=True)
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.replace(" ", "_", regex=True)
        df.columns = df.columns.str.upper()
        df.rename(columns={"Dew_Point_Temp".upper(): "Dew_Temp".upper()}, inplace=True)
        print(df.to_string())
        cols = [
            "DATE/TIME_(UTC)",
            "Year",
            "Month",
            "Day",
            "Temp",
            "Rel_Hum",
            "Dew_Temp",
            "LATITUDE_(Y)",
            "LONGITUDE_(X)",

        ]
        Wdata = df[[x.upper() for x in cols]].copy()
        Wdata = Wdata.fillna(method="ffill")
        Wdata = Wdata.fillna(method="bfill")
        Wdata.rename(
            columns={
                "DATE/TIME_(UTC)": "datetime_utc",
                "TEMP": "temperature",
                "REL_HUM": "relative_humidity",
                "DEW_TEMP": "dewpoint_temperature",
                "PRECIP._AMOUNT_(MM)": "precipitation_mm",
                "LATITUDE_(Y)": "latitude",
                "LONGITUDE_(X)": "longitude",
            },
            inplace=True,
        )
        Wdata.set_index("datetime_utc", inplace=True)
        Wdata.index = pd.to_datetime(Wdata.index)
        Wdata = Wdata.sort_index()
        Wdata["hour"] = Wdata.index.hour
        Wdata["humidex"] = pd.Series(
            np.round([
                hmdxx(
                    x.temperature,
                    x.dewpoint_temperature,
                )
                for x in Wdata.itertuples()
            ],1),
            index=Wdata.index,
        )
        for number in range(10, 24):
            Wdata[f"hdh_{number}"] = [
                number - x if x < number else 0 for x in Wdata["temperature"]
            ]
            Wdata[f"cdh_{number}"] = [
                x - number if x > number else 0 for x in Wdata["temperature"]
            ]
        Wdata.columns = [i.lower() for i in Wdata.columns]
        # get the date features
        Wdata = (
            parse_date_features(Wdata)
            .sort_index()
        )
        try:
            Wdata["relative_humidity"] = Wdata[
                "relative_humidity"
            ].astype(np.int64)
        except ValueError:
            pass

        bad_indexs = []
        for z in Wdata.itertuples():
            if pd.isnull(z.relative_humidity) or z.relative_humidity == 'nan':
                if pd.isnull(z.temperature) or z.temperature == 'nan':
                    if pd.isnull(z.dewpoint_temperature) or z.dewpoint_temperature == 'nan':
                        bad_indexs.append(z.Index)
        Wdata = Wdata[~Wdata.index.isin(bad_indexs)].copy()
        return Wdata
    except Exception:
        print(error_handling())
        return pd.DataFrame()


def weather_get_historical_data_for_all_can_cities(start_year: int = 2000) -> None:
    """
    This function queries the API of Environment Canada on a month-by-month basis and puts the data into ADLS. Each year
    is retrieved in full. The full dataset is then placed into a different area of ADLS.
    @param start_year: the start year of the querying.
    @return: None
    """
    can_weather_station_info_df = pd.read_sql("select * from weather_canadian_weather_stations",home_engine, )
    for row in tqdm(can_weather_station_info_df.drop_duplicates(
        subset=["weather_station_id", "weather_station_name", 'city_name']
    ).itertuples()):
        for y in range(start_year, today.year + 1):
            for m in range(1, 13):
                idf = weather_get_can_historical_data_hourly(
                    row.weather_station_id, year=y, month=m
                )
                idf = idf[idf.index < pd.to_datetime(today.date())].reset_index()
                idf.columns = [i.lower() for i in idf.columns]
                idf['location'] = row.city_name
                print(idf.head(2).to_string())
                print(idf.tail(2).to_string())
                print(idf.shape)
                if idf.shape[0] > 0:
                    blob_name = rf"weather\historical\weather_historical_data_{row.weather_station_name.lower().replace(' ', '_')}_{y}_{m}.parquet"
                    print(blob_name)
                    idf.to_parquet(data_path + blob_name, index=False, )
                    with home_engine.begin() as conn:
                        idf.to_sql("weather_historical_hourly", conn, index=False, if_exists='append', schema='home')
                time.sleep(1)
        print(datetime.datetime.now() - today)


def weather_get_historical_data_for_all_can_cities_this_month() -> None:
    """
    This function queries the API of Environment Canada on a month-by-month basis and puts the data into ADLS. Each year
    is retrieved in full. The full dataset is then placed into a different area of ADLS.
    @param start_year: the start year of the querying.
    @return: None
    """
    noww = datetime.datetime.now().date()
    yesterday = noww - datetime.timedelta(days=1)
    engine = sqlalchemy.create_engine(home_connection_string)
    can_weather_station_info_df = pd.read_sql("select * from weather_canadian_weather_stations",engine, )
    for row in tqdm(can_weather_station_info_df.drop_duplicates(
        subset=["weather_station_id", "weather_station_name", 'city_name']
    ).itertuples()):
        y = noww.year
        m = noww.month
        today_months_weather_df = weather_get_can_historical_data_hourly(row.weather_station_id, y, m)
        print(today_months_weather_df.head().to_string())
            # .set_index('datetime_utc')
        today_months_weather_df = today_months_weather_df[
            today_months_weather_df.index < pd.to_datetime(noww)
        ].reset_index()
        today_months_weather_df.columns = [
            i.lower() for i in today_months_weather_df.columns
        ]
        today_months_weather_df['location'] = row.city_name
        dagster_logger.info(today_months_weather_df.head(2).to_string())
        if today_months_weather_df.shape[0] > 0:
            blob_name = rf"weather\historical\weather_historical_data_{row.weather_station_name.lower().replace(' ', '_')}_{y}_{m}.parquet"
            dagster_logger.info(blob_name)
            today_months_weather_df.to_parquet(data_path + blob_name, index=False, )
            with engine.begin() as conn:
                today_months_weather_df.to_sql("weather_historical_hourly", conn, index=False, if_exists='append', schema="home")
        # break
        # to handle first days of the month (and ensure that last month's data was fully captured)
        if noww.day == 1:
            yy = yesterday.year
            mm = yesterday.month
            dagster_logger.info("first of month", yy, mm)
            yes_months_weather_df = weather_get_can_historical_data_hourly(
                row.weather_station_id, yy, mm
            ).set_index('datetime_utc')
            yes_months_weather_df = yes_months_weather_df[
                yes_months_weather_df.index < pd.to_datetime(noww)
            ].reset_index()
            yes_months_weather_df.columns = [
                i.lower() for i in yes_months_weather_df.columns
            ]
            yes_months_weather_df['location'] = row.city_name
            dagster_logger.info(yes_months_weather_df.head(2).to_string())
            if yes_months_weather_df.shape[0] > 0:
                yblob_name = rf"weather\historical\weather_historical_data_{row.weather_station_name.lower().replace(' ', '_')}_{y}_{m}.parquet"
                dagster_logger.info(yblob_name)
                yes_months_weather_df.to_parquet(data_path + yblob_name, index=False, )
                with engine.begin() as conn:
                    yes_months_weather_df.to_sql("weather_historical_hourly", conn, index=False, if_exists='append', schema="home")
        # need time for the DB to commit the last transaction
        time.sleep(1)


def fix_empty_rows_weather_historical_hourly_table(engine=None):
    if engine:
        engine_to_use = engine
    else:
        engine_to_use = sqlalchemy.create_engine(home_connection_string)
    inner_df = pd.read_sql("select * from weather_historical_hourly", engine_to_use, )
    dagster_logger.info(f"Data Load Time: {datetime.datetime.now() - today} // {len(inner_df.index)} rows")
    bad_indexs = []
    for z in inner_df.itertuples():
        if pd.isnull(z.relative_humidity) or z.relative_humidity == 'nan':
            if pd.isnull(z.temperature) or z.temperature == 'nan':
                if pd.isnull(z.dewpoint_temperature) or z.dewpoint_temperature == 'nan':
                    bad_indexs.append(z.Index)

    inner_df = inner_df[~inner_df.index.isin(bad_indexs)].copy().drop_duplicates()
    dagster_logger.info(f"Now {len(inner_df.index)} rows")
    inner_df.to_sql("weather_historical_hourly", engine_to_use, if_exists='replace', index=False)
    dagster_logger.info(f'weather_historical_hourly cleaned of NAN rows in {datetime.datetime.now() - today}')



# PC STATS
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
def get_operating_system():
    system = platform.system()
    if system == 'Windows':
        return 'Windows'
    elif system == 'Linux':
        return 'Linux'
    else:
        return 'Unknown'
def heartbeat_func():
    """
    This function is the scheduler heartbeat. By reading the file, you can be sure that the scheduler is running.
    There's a random number printed on each line, along with the time of execution.
    @return: nothing
    """
    timee = datetime.datetime.now()
    with open('python_scheduler_heartbeat.log', 'a') as file:
        file.write(f"APscheduler | {np.random.randint(1,15)} |{timee}\n")
def get_pids(word = "python", platfrm = 'Windows'):
    if platfrm == 'Windows':
        command = f"""tasklist /v /fo csv  | findstr /i "{word}" """ # command line entry for finding *word* string in process list
        tmp = []
        for p in os.popen(command).readlines():
            wow = []
            for i, e in enumerate(p.split('","')): # comes in as CSV format with each variable in double quotes ""
                if i == 4: # the fourth value in each row may have commas between the numbers for thousands, etc, else remove punctation
                    wow.append(e.replace("\\\n", "").replace("'", "").replace(',', "").replace('"', "").replace(' K', '000'))
                else:
                    wow.append(e.replace("\\\n", "").replace("'", "").replace('"', ""))
            tmp.append(wow)
        tmp_df = pd.DataFrame(tmp, )
        try:
            # name each column, this is a best guess
            tmp_df.columns = ['process', 'pid', 'process_type', 'num', 'memory_use', 'unknown', 'parent', "weird_time", 'description']
            tmp_df = tmp_df[tmp_df['process'].str.contains(word)] # make sure the proces is the ones you want
            tmp_df["memory_use"] = tmp_df["memory_use"].astype(np.int64)
            return tmp_df
        except:
            return pd.DataFrame()
    elif platfrm == 'Linux':
        try:
            return pd.DataFrame()
        except:
            return pd.DataFrame()
def pc_usage():
    mem = dict(psutil.virtual_memory()._asdict()) # memory info
    # get the python's memory usage
    tmp_memdf = pd.concat([get_pids("python"),(get_pids('pycharm'))])
    python_memory_usage_kB = tmp_memdf['memory_use'].sum()
    # get the sql server's memory usage
    try:
        sql = get_pids("mysql")
        yy = sql['memory_use'].sum()
    except:
        try:
            sql = get_pids("sql")
            yy = sql['memory_use'].sum()
        except:
            yy = np.nan
    sql_memory_usage_kB = yy

    output_dict = {'memory_' + k + "_MB":np.round(v/1024**2,2) for k,v in mem.items()}
    output_dict.update({'cpu_pct': psutil.cpu_percent(), # gives a single float value
                        'cpu_cores': psutil.cpu_count(),
                        'cpu_freq': psutil.cpu_freq().current,
                        'pc_network_address': get_ip_address(),
                        "pc_os": platform.system(),
                        "pc_cpu": platform.processor(),
                 'python_memory_usage_GB': np.round(python_memory_usage_kB/1024**3,2),
                        'sql_memory_usage_GB': np.round(sql_memory_usage_kB / 1024 ** 3,),
             "query_time": str(datetime.datetime.now())})
    return output_dict
def get_pc_stats():
    t_df = pd.DataFrame(pc_usage(), index=[0])
    with sqlalchemy.create_engine(home_connection_string).connect() as conn:
        t_df.to_sql('operations_pc_stats', conn, if_exists='append', schema = 'home', index=False)
    dagster_logger.info("Row written to PC_STATS table")
