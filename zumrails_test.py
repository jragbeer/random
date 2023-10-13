import datetime
import os
import pickle
import re
import string
from typing import Iterable

import dotenv
import googlemaps
import numpy as np
import pandas as pd
import scipy

# helpful articles
# [1] https://td.intelliresponse.com/cbaw/index.jsp?requestType=NormalRequest&source=100&id=4838&question=How+can+I+identify+transactions+I+don%27t+recognize
# [2] https://medium.com/brexeng/how-we-built-a-mostly-automated-system-to-solve-credit-card-merchant-classification-f9108029e59b
# [3] https://www.freedomthirtyfiveblog.com/2020/06/what-td-transaction-codes-mean.html

path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/")+ "/"
data_path = path + 'data/'
today = datetime.datetime.today()
print(today)

# load secrets to ENVs
dotenv.load_dotenv(path + '.env')

# location of IO files
in_file = data_path + "bank_transactions.csv"
out_file = data_path + "categorized_transactions.csv"

# Ryerson University, DT Toronto central
google_maps_starting_location = (43.6576585,-79.3788017)
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_API_KEY"))

# find website URLS
regex_to_find_website_urls = r"^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*"
# find account transfer-like transactions
regex_to_find_acct_transfers = r'TO:\s\d+'

# HTML
html_mappings = {
    "&AMP;": "&".upper(),
}
# helpful mappings, taken mostly from helpful articles [1]
replace_mappings = {
    # company specific
    "SHOPPERS DRUG M":"SHOPPERS DRUG MART".upper(),
    "AMZN": "AMAZON".upper(),
    "NSLSC":"NATIONAL STUDENT LOAN SERVICE CENTRE".upper(),
    # codes
    "E-TFR": "e-transfer".upper(),
    "ACCT BAL REBATE": "Account balance rebate".upper(),
    "EI": "Employment Insurance".upper(),
    "INS": "Insurance".upper(),
    "TFR-FR": "Transfer From".upper(),
    "BPY": "Bill Payment".upper(),
    "PAY":"Payroll Deposit".upper(),
    "MSP": "Misc Payments".upper(),
    # Interac Flash = contactless debit
    "_F": " Interac Flash".upper(),
    "_V": " Visa Debit".upper(),

}

# mapping to help categorize income-type rows
income_mapping = {
"Employment Income": {"PAYROLL DEPOSIT"},
"Government Income": {"EMPLOYMENT INSURANCE"},
"Other Income": {"TRANSFER FROM", "MISC PAYMENTS"},
}
inverse_income_mapping = {v: k for k, u in income_mapping.items() for v in u}

# mapping to help categorize expense-type rows
expenses_mapping = {
'Bills & Utilities': {'PHONE', 'INTERNET', 'TELEVISION', 'UTILITIES', 'BILL'},
'Entertainment': {'AMUSEMENT', 'ARTS', 'MOVIES', 'DVDS', 'MUSIC', 'NEWSPAPERS', 'MAGAZINES'},
'Fees & Charges': {'ATM FEE', 'BANK FEE', 'FINANCE CHARGE', 'LATE FEE', 'SERVICE FEE', 'TRADE COMMISSIONS',
                   "ACCOUNT FEE"},
'Financial': {'FINANCIAL', "INSURANCE", "FINANCE"},
'Food & Dining': {'SUPERMARKET', 'CATERING', 'COFFEE', 'FOOD', 'GROCERY', 'RESTAURANT', "FOODMART", },
'Gifts & Donations': {'CHARITY', 'GIFT', "E-TRANSFER",},
'Health & Fitness': {'DENTIST', 'DOCTOR', 'EYECARE', 'GYM', 'HEALTH', 'PHARMACY', 'SPORTS'},
'Home': {'FURNISHINGS', 'MORTGAGE', 'RENT'},
'Investments': {'MUTUAL FUNDS'},
'Loans': {'LOAN'},
'Pets': {'PET', 'VETERINARY'},
'Shopping': {'DOLLARAMA', 'BOOKS', 'CLOTHING', 'ELECTRONICS', 'SOFTWARE', 'HOBBIES', 'SPORTING', "COSTCO",
             "WALMART", "AMAZON"},
'Taxes': {'TAX'},
'Travel': {'AIR','TRAVEL', 'HOTEL', 'RENTAL','CAR', 'TAXI', 'VACATION', "PARKING"},
}
inverse_expenses_mapping = {v: k for k, u in expenses_mapping.items() for v in u}


def create_embedding_pickles():
    """
    This function reads GloVe word embeddings from text files, processes them, and creates pickle files for each
    embedding file.The pickle files are saved in the same directory with a .pickle extension.

    GloVe files are available in different dimensions:
    - glove.42B.300d.txt
    - glove.6B.50d.txt
    - glove.6B.100d.txt
    - glove.6B.200d.txt
    - glove.6B.300d.txt
    """
    # Iterate over each GloVe file
    for embedding_file in ["glove.42B.300d.txt", "glove.6B.50d.txt", "glove.6B.100d.txt", "glove.6B.200d.txt", "glove.6B.300d.txt"]:
        embeddings_dict = {}
        # Read the GloVe file and process each line
        with open(data_path + embedding_file, 'r') as f:
            for line in f:
                values = line.split()
                word = values[0]
                vector = np.asarray(values[1:], "float32")
                embeddings_dict[word] = vector

        # Save the processed embeddings as a pickle file
        pickle_out = open(data_path + embedding_file.replace('.txt', '.pickle'), "wb")
        pickle.dump(embeddings_dict, pickle_out)
        pickle_out.close()

def find_closest_embeddings(embedding: Iterable, embeddings_dict: dict) -> dict:
    """
    This function finds similar vectors to the input embedding using euclidean distance
    :param embedding: the specific embedding you're looking to compare with
    :param embeddings_dict: the dictionary with all of the embeddings
    :return: a dictionary
    """
    return sorted(embeddings_dict.keys(), key=lambda word: scipy.spatial.distance.euclidean(embeddings_dict[word], embedding))


def get_google_places_data(search_text:str) -> dict:
    """
    This function takes the input string and calls the Google Maps API. The first results' name and types fields are
    returned as a dictionary.
    :param search_text: the text that is sent to the API, must be minimum 3 letters
    :return: a dictionary with 2 fields, name:str and types:list
    """
    try:
        if len(search_text) < 3:
            raise ValueError
        # Try finding a place via Google Maps API
        geocode_result = gmaps.places(search_text, location=google_maps_starting_location)
        # only return a small part of the resulting JSON
        geo_place_result = {"name": geocode_result['results'][0]['name'], "types":geocode_result['results'][0]['types']}
    except (KeyError, ValueError, IndexError) as ie:
        geo_place_result = {"name": "", "types":[]}
    return geo_place_result

def split_string_combinations(input_text:str) -> list:
    """
    This function takes an input string, splits it into individual words, and
    generates combinations of adjacent words. It does not include combinations
    where words are not adjacent to each other.
    :param input_text: input string
    :return: a list with possible combos
    """
    # Split the input string into individual words
    words = input_text.split()
    combinations = []
    # Start with an individual word
    for i in range(len(words)):
        combination = words[i]
        combinations.append(combination)
        # Create combinations of adjacent words and add them to the list
        for j in range(i + 1, len(words)):
            combination = ' '.join(words[i:j + 1])
            combinations.append(combination)
    return combinations

def remove_codes(input_text: str) -> str:
    """
    This function removes information from the input string so that transaction codes that are similar to hashes such as
    T5JH7P are removed.
    :param input_text: the input string that will be changed to remove the code
    :return: a modified string
    """
    new_text = input_text
    # find codes which are between 4 and 10 chars in length, they must contain both alphas and numbers, remove them
    for hash in re.findall(r'\s*([0-9a-zA-Z]{4,10})\s*', input_text):
        numm = 0
        lett = 0
        for y in hash:
            if y in string.digits:
                numm = numm + 1
            if y.isalpha():
                lett = lett + 1
        if numm > 0 and lett > 0:
            new_text = new_text.replace(hash, "")
    returned_text = new_text.strip()
    # if the result is an empty string, then return the original, as it probably isn't a code
    if not returned_text:
        return input_text.strip()
    return new_text.strip()

def get_bare_text(input_text: str) -> str:
    """
    This function removes information from the input string so that only information that can help with naming a
    company remains.
    :param input_text: the input string that will be changed to get the bare information
    :return: a modified string
    """
    new_text = input_text
    new_text = replace_urls_with_domains(new_text)
    # remove punctuation from the string
    new_text = new_text.replace(".", " ").replace("/", " ").replace("*", " ").replace("#", " ")
    # search for long strings of digits in the string and remove them
    for hash in re.findall(r'(\d+)', new_text):
        new_text = new_text.replace(hash, " ")
    # remove common helpful keywords such as INTERAC FLASH and VISA DEBIT that wouldn't be helpful to find the name of the company
    new_text = new_text.replace("INTERAC FLASH", "").replace("VISA DEBIT", "").replace("  ", " ")
    return new_text.strip()

def replace_urls_with_domains(input_text: str) -> str:
    """
    This function uses a regular expression to find URLs in the input text
    and replaces them with the extracted domain and what follows the slashes.

    :param input_text: The string containing URLs to be replaced.
    :return: The modified text with URLs replaced by domains and paths.
    """
    # Use re.sub to find and replace URLs with domains and what comes after the slashes
    def replace_url_inner(match):
        domain = match.group(1)
        path = match.group(2) if match.group(2) else ''
        return f'{domain}{path}'
    # A regular expression pattern to match URLs within text
    pattern = r'https?://(?:www\d?\.)?(.*?)\.[a-z]+(/[^ ]*)?'
    modified_text = re.sub(pattern, replace_url_inner, input_text)
    return modified_text
def categorize_income(income_df: pd.DataFrame, income_mapping: dict) -> pd.DataFrame:
    """
    This function takes a DF of income data and categorizes the income descriptions
    based on pre-defined income_mapping. It also performs cleaning operations on the descriptions.

    :param income_df: DF containing income data, including a 'description' column.
    :param income_mapping: A dictionary containing mappings of keywords to income categories.
    :return: A modified DF with the 'Category' column added, indicating the income category.
    """
    income_df['clean_description'] = [remove_codes(i) for i in income_df['description'].values]
    # replace words regardless, these may be HTML tags that need to be converted to human-readable text
    new_col = []
    for text_val in income_df['clean_description'].values:
        for word_to_find, rplc in html_mappings.items():
            if word_to_find in text_val:
                text_val = text_val.replace(word_to_find,rplc)
        new_col.append(text_val)
    income_df['clean_description'] = new_col
    # replace the words surrounded by word boundaries, these are well known abbreviations, but may make NLP difficult
    clean_description = []
    for text_val in income_df['clean_description'].values:
        for word_to_find,rplc in replace_mappings.items():
            pattern = r"\b"+word_to_find+r"\b"
            results = re.findall(pattern, text_val)
            if results:
                text_val = text_val.replace(word_to_find,rplc)
        clean_description.append(text_val)
    income_df['clean_description'] = clean_description
    # assign a category to the clean_description descriptions using the income_mapping for obvious words
    category = []
    for text_val in income_df['clean_description'].values:
        new = "Other Income"
        for word_to_find,rplc in income_mapping.items():
            pattern = r"\b" + word_to_find + r"\b"
            results = re.findall(pattern, text_val)
            if results:
                new = rplc
                break
        category.append(new)
    income_df['Category'] = category
    income_df = income_df.drop(columns=['clean_description'])
    return income_df

def categorize_expense(expense_df: pd.DataFrame, expenses_mapping:dict) -> pd.DataFrame:
    """
    This function takes a DF of income data and categorizes the income descriptions
    based on pre-defined income_mapping. It also performs cleaning operations on the descriptions.

    :param expense_df: DF containing income data, including a 'description' column.
    :param expenses_mapping: A dictionary containing mappings of keywords to income categories.
    :return: A modified DF with the 'Category' column added, indicating the income category.
    """
    expense_df['clean_description'] = [remove_codes(i) for i in expense_df['description'].values]
    # replace words regardless, these may be HTML tags that need to be converted to human-readable text
    new_col = []
    for text_val in expense_df['clean_description'].values:
        for word_to_find,rplc in html_mappings.items():
            if word_to_find in text_val:
                text_val = text_val.replace(word_to_find,rplc)
        new_col.append(text_val)
    expense_df['clean_description'] = new_col
    # replace the words surrounded by word boundaries, these are well known abbreviations, but may make NLP difficult
    clean_description = []
    for text_val in expense_df['clean_description'].values:
        for word_to_find,rplc in replace_mappings.items():
            pattern = r"\b"+word_to_find+r"\b"
            results = re.findall(pattern, text_val)
            if results:
                text_val = text_val.replace(word_to_find,rplc)
        clean_description.append(text_val)
    expense_df['clean_description'] = clean_description
    expense_df['bare_description'] = [get_bare_text(i) for i in expense_df['clean_description'].values]

    # get the unique values that we will ask the Google Maps API to help classify, resulting in less API calls
    uniques = pd.DataFrame({'bare_description':expense_df['bare_description'].unique()}).drop_duplicates()
    uniques['google_result'] = [get_google_places_data(i) for i in uniques['bare_description'].values]

    # join the Google API results with DF
    expense_df = pd.merge(expense_df, uniques, on='bare_description', how = 'left')
    # from the resulting column, break out the name of the business
    expense_df['name_of_business'] = [i['name'] for i in expense_df['google_result']]
    # get the tags as a separate column, modifying some tags for better readability
    google_tags = []
    for x in expense_df['google_result']:
        inner_tags = []
        for each in x['types']:
            # remove _store as we're interested in the key word
            if each.endswith("_store"):
                each = each.replace("_store", "")
            inner_tags.append(each.replace("_", " ").upper())
        # use a sorted set for better readability
        google_tags.append(sorted(set(inner_tags)))
    expense_df['google_tags'] = google_tags
    expense_df = expense_df.drop(columns = ['google_result'])

    # create a list of tags for that row, based on the bare_description and google_tags columns
    tags = []
    for i in expense_df.itertuples():
        string_combo = split_string_combinations(i.bare_description)
        inner_t = []
        for each in string_combo:
            # to ensure not too many tags, keep only those that are in the expenses_mapping
            if ' ' in each:
                if each in inverse_expenses_mapping.keys():
                    inner_t.append(each)
            else:
                inner_t.append(each)
        tags.append(set(list(i.google_tags) + inner_t))
    expense_df['tags'] = tags

    category = []
    for i in expense_df.itertuples():
        text_vals = i.tags
        # default value, if it can't be classified otherwise
        new = "Other Expense"
        for xx in text_vals:
            for word_to_find,rplc in expenses_mapping.items():
                pattern = r"\b" + word_to_find + r"\b"
                results = re.findall(pattern, xx)
                if results:
                    new = rplc
                    break
        # if there's TO: XXXXXXXX with an acct number, it will be classified as a gift
        results_acct_trnfr = re.findall(regex_to_find_acct_transfers, i.clean_description)
        if results_acct_trnfr:
            new = "Gifts & Donations"
        category.append(new)
    expense_df['Category'] = category
    expense_df = expense_df.drop(columns = ["clean_description", "tags", "name_of_business", "bare_description", 'google_tags'])
    return expense_df

def categorize_transactions(input_file_location:str, output_file_location:str) -> None:
    """
    This function reads transaction data from an input CSV file, performs processing and categorization,
    and then saves the results to an output CSV file.

    :param input_file_location: the path of the input file
    :param output_file_location: The path where the output CSV file will be saved
    :return: None
    """
    idf = pd.read_csv(input_file_location)
    # normalize the column names by using lower-case only
    idf.columns = [i.lower() for i in idf.columns]
    # normalize the text by using upper-case only
    idf['description'] = idf['description'].str.upper()

    # split income and expense rows as they will be processed differently
    income = idf.dropna(subset=["credit"]).sort_values("description").reset_index(drop=True)
    expense = idf.dropna(subset=["debit"]).sort_values("description").reset_index(drop=True)

    # process the income and expense DFs independently
    income = categorize_income(income, inverse_income_mapping)
    expense = categorize_expense(expense, inverse_expenses_mapping)

    # recombine dataframes, format for output and then output as a CSV file to the output_file_location
    out_df = pd.concat([expense, income]).reset_index(drop=True)
    out_df.columns = [i.capitalize() for i in out_df.columns]
    out_df.to_csv(output_file_location, index=False)
    print(out_df.to_string())
    print(f"\rFile saved to: {output_file_location}")

categorize_transactions(input_file_location=in_file, output_file_location=out_file)

end = datetime.datetime.now()
print(end-today)
