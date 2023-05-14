"""
Program:        toronto_data_eng.py
Description:    This is a collection of functions that are used to do the data manipulation for City of Toronto projects.
Arguments:      N/A
Returns:        N/A
By:  jragbeer, <add names as you work on this please>
Last Updated: 20230513
"""
import datetime
import os
import shutil
import sqlite3
import warnings
import zipfile
from typing import Optional
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
import numpy as np
import pandas as pd
import requests
from pprint import pprint
import urllib.request
import json
import chardet
from pathlib import Path

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)
np.random.seed(150)  # seed for reproducibility

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
data_path = path + "data/"
today = datetime.datetime.now()
print(today)
bad_lines = []
local_db = sqlite3.connect(data_path + "city_of_toronto.db")

def extract_geojson_to_db(name_of_zip_file: str) -> pd.DataFrame:
    extract_zip(name_of_zip_file)
    for f in os.listdir(data_path + 'tmpfiles/'):
        # read file
        with open(data_path + "tmpfiles/" + f, 'r', errors="ignore") as myfile:
            tmp_read = myfile.read()
            try:
                geojson = json.loads(tmp_read)
            except Exception as iee:
                pprint(iee)

    rows = []
    for each in geojson['features']:
        tmp_dict = dict(each['properties'])
        tmp_dict.update({'lat': each['geometry']['coordinates'][1],
                         'long': each['geometry']['coordinates'][0], })
        rows.append(tmp_dict)

    out_df = pd.DataFrame(rows)
    out_df.columns = [i.lower().replace('-', "_") for i in out_df.columns]
    out_df.to_sql("toronto_geojson_data", local_db, if_exists='replace', index=False)
    return out_df
def extract_colname_to_db(name_of_zip_file: str) -> None:
    extract_zip(name_of_zip_file)
    for f in os.listdir(data_path + 'tmpfiles/'):
        if f.endswith('.txt'):
            # read file
            with open(data_path + "tmpfiles/" + f, 'r', errors="ignore") as myfile:
                col_name_info = myfile.readlines()

    pprint(col_name_info)
def extract_zip(filee: str, name_of_tmp_folder: str = "tmpfiles") -> None:
    """
    This function takes a file inside of the /data/ folder and unzips it. It imputed_occupancy_data copies the file, then unzips it, then
    deletes the copied file.
    :param filee: Name of the file (not including path)
    :param name_of_tmp_folder: Mame of the folder to put the contents of the zip (not including path to /data/ folder)
    :return: None
    """
    try:
        os.mkdir(data_path + name_of_tmp_folder)  # make temp folder in the data folder
    except Exception:
        pass
    # copy file over to new temp directory
    shutil.copy(data_path + filee, data_path + f"{name_of_tmp_folder}\\{filee}")
    with zipfile.ZipFile(data_path + f"{name_of_tmp_folder}\\{filee}", "r") as zip_ref:
        zip_ref.extractall(data_path + name_of_tmp_folder)
    os.remove(data_path + f"{name_of_tmp_folder}\\{filee}")
def get_toronto_api_data(param_id: str, package_name: str) -> str:
    """
    This uses code found from the City of Toronto download page to download the data from the various datasets.
    Comments are taken from the 'For Developers' code samples on the page.
    Ex:
    https://open.toronto.ca/dataset/parking-tickets/
    https://open.toronto.ca/dataset/address-points-municipal-toronto-one-address-repository/

    :param param_id: Which data to download from the API
    :param package_name: Which type of file to download from the endpoint. Valid entries are: geojson or shapefile
    :return: Name of the zip file that was downloaded and is placed in the /data/tmpfile folder
    """
    # Toronto Open Data is stored in a CKAN instance. It's APIs are documented here:
    # https://docs.ckan.org/en/latest/api/

    # To hit our API, you'll be making requests to:
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"

    # Datasets are called "packages". Each package can contain many "resources"
    # To retrieve the metadata for this package and its resources, use the package name in this page's URL:
    url = base_url + "/api/3/action/package_show"
    params = {"id": param_id}
    package = requests.get(url, params=params).json()
    name_of_output_file = f"toronto_{param_id.replace('-','_')}_{package_name}_{today.strftime('%F').replace('-', '_')}"

    # To get resource data:
    for idx, resource in enumerate(package["result"]["resources"]):
        # To get metadata for non datastore_active resources:
        if not resource["datastore_active"]:
            if package_name in resource["name"].replace("-", "_"):
                url = base_url + "/api/3/action/resource_show?id=" + resource["id"]
                resource_metadata = requests.get(url).json()
                pprint(resource_metadata)
                # From here, you can use the "url" attribute to download this file
                response = resource_metadata['result']['url']
                dl_time = datetime.datetime.utcnow()
                new_name_of_output_file = name_of_output_file + '.' + resource_metadata['result']['format'].lower()
                urllib.request.urlretrieve(response, data_path + new_name_of_output_file)
                # Add name of file and time of DL to the dictionary, and put it into a SQL table
                out_dict = dict(resource_metadata['result'])
                out_dict.update({'name_of_output_file': new_name_of_output_file,
                                'utc_download_time': str(dl_time),
                                 'help': resource_metadata['help'],
                                 'success': resource_metadata['success']})
                download_response_df = pd.DataFrame(out_dict, index=[0])
                download_response_df.to_sql("download_responses", local_db, if_exists='append', index=False)
                print(f'Response for {param_id} ({package_name}) DL {str(dl_time)} captured in DB')
                return new_name_of_output_file
def extract_parking_data_readme_to_db(name_of_input_file: str) -> None:
    """
    Extract the README file, an xls file, and put the tables into SQL as "data_dictionary_" tables. Change the column
    names and the names of the table to match our specifications.
    :param name_of_input_file: Name of the input xls file.
    :return: None
    """
    # Find the name of the table
    x1df = pd.read_excel(data_path + name_of_input_file, sheet_name='Sheet1', skipfooter=2)
    name_of_first_table = x1df.columns[0]
    # Read the table and transform column names and drop blank rows
    first_table = pd.read_excel(data_path + name_of_input_file, sheet_name='Sheet1', skiprows=2, skipfooter=14)
    first_table.columns = [i.replace(" ", "_").replace("-", "_").lower() for i in first_table.columns]
    first_table = first_table.dropna()
    # Write the table into SQL as a data dictionary table
    first_table.to_sql("data_dictionary_" + name_of_first_table.replace(" ", "_").replace("-", "_").lower(), local_db, if_exists='replace', index=False)

    # Find the name of the table
    x2df = pd.read_excel(data_path + name_of_input_file, sheet_name='Sheet1', skiprows=17, skipfooter= 18)
    name_of_second_table = x2df.columns[0]
    # Read the table and transform column names and drop blank rows
    second_table = pd.read_excel(data_path + name_of_input_file, sheet_name='Sheet1', skiprows=18,)
    second_table.columns = [i.replace(" ", "_").replace("-", "_").lower() for i in first_table.columns]
    second_table = second_table.dropna()
    # Write the table into SQL as a data dictionary table
    second_table.to_sql("data_dictionary_" + name_of_second_table.replace(" ", "_").replace("-", "_").lower(), local_db, if_exists='replace', index=False)
def extract_parking_ticket_data(name_of_zip_file: str) -> pd.DataFrame:
    extract_location = f'tmpfiles/{name_of_zip_file.lower().replace(" ", "_").replace("-", "_").lower()}'
    if extract_location.endswith('.zip'):
        extract_location = extract_location.replace(".zip", "")
    extract_zip(name_of_zip_file, extract_location)
    all_data = []
    for f in os.listdir(data_path + extract_location):
        # read file
        filename = data_path + extract_location + "/" + f
        print(f'reading from {filename}')
        detected = chardet.detect(Path(filename).read_bytes())
        # detected is something like {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
        encoding = detected.get("encoding")
        assert encoding, "Unable to detect encoding, is it a binary file?"
        print('Encoding of CSV file: ', encoding)
        adf = pd.read_csv(filename,
                          engine='python',
                          encoding=encoding,
                          sep=',',
                          on_bad_lines='warn',
                          )
        adf.columns = [i.replace(" ", "_").replace("-", "_").lower() for i in adf.columns]
        all_data.append(adf)
    return pd.concat(all_data)

# # GET THE ZIP FILE WITH COORDINATES
# name_of_geojson_zip_file = get_toronto_api_data("address-points-municipal-toronto-one-address-repository", 'geojson')
# name_of_shapefile_zip_file = get_toronto_api_data("address-points-municipal-toronto-one-address-repository", 'shapefile')
#
# # EXTRACT COLUMN NAME INFO AND PUT CONTENTS INTO DB
# extract_colname_to_db(name_of_shapefile_zip_file)
# # EXTRACT GEOJSON ZIPFILE AND PUT CONTENTS INTO DB
# out_df = extract_geojson_to_db(name_of_geojson_zip_file)
#
#
# # # GET THE PARKING TICKETS DATA
# names_of_parking_data_zip_files = {}
# # # GET THE DATA DICTIONARY / README
# names_of_parking_data_zip_files['parking_ticket_data_readme'] = get_toronto_api_data("parking-tickets", 'parking_ticket_data_readme')
# extract_parking_data_readme_to_db(names_of_parking_data_zip_files['parking_ticket_data_readme'])
#
# all_dfs = []
# for y in range(2008, today.year):
#     names_of_parking_data_zip_files[y] = get_toronto_api_data("parking-tickets", f'parking_tickets_{y}')
#     tdf = extract_parking_ticket_data(names_of_parking_data_zip_files[y])
#     print(tdf.head().to_string())
#     all_dfs.append(tdf)
#
#
# parking_data = pd.concat(all_dfs)
# parking_data.to_sql("toronto_parking_tags_data", local_db, index=False, if_exists='replace')
#
# print(out_df.sample(100).to_string())
# print(parking_data.sample(100).to_string())


# parking_tags = pd.read_sql("select * from toronto_parking_tags_data", local_db)
# parking_tags.to_parquet(data_path + 'parking_tags.parquet', index=False)
# geojson_df = pd.read_sql("select * from toronto_geojson_data", local_db)
# geojson_df.to_parquet(data_path + 'geojson.parquet', index=False)


geojson_df = pd.read_parquet(data_path + 'geojson.parquet',)
parking_tags = pd.read_parquet(data_path + 'parking_tags.parquet',)
print(geojson_df.head().to_string())
print(datetime.datetime.now()-today)
