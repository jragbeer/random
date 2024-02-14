from bokeh.plotting import show
from bokeh.models import TextInput, CustomJS, Tabs, TabPanel, Button
from bokeh.models.widgets import Select, Div
from bokeh.io import curdoc
from bokeh.layouts import row, column
from docxtpl import DocxTemplate
import traceback
import time
import datetime
import os
import ast
import numpy as np
import pandas as pd
from pprint import pprint


# clear the webpage before visualization
doc = curdoc()
doc.clear()
doc.title = 'KC Logistics Data Input'

# pandas settings for terminal output
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

today = datetime.datetime.now()
path = os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/"
data_path = path + 'data/'

# constants
constants = {
"business_number": "13850 8288",
"terms": "Net 30 Days",
"customer_reference_#": "XXX",
"my_business_name":"KC Logistics Corp.",
"my_strt_name":"Kingston Road",
"my_strt_number":"1100",
"my_unit_name": "701",
"my_city":"Toronto",
"my_state":"ON",
"my_pc":"M1N1N4",
"my_email":"KCLogistics7@gmail.com",
}

canada_tax_rates = {
"AB": {"GST": 5, "PST": 0, "HST": 0},
"BC": {"GST": 5, "PST": 7, "HST": 0},
"MB":{"GST": 5, "PST": 7, "HST": 0},
"NB":{"GST": 0, "PST": 0, "HST": 15},
"NL":{"GST": 0, "PST": 0, "HST": 15},
"NS":{"GST": 0, "PST": 0, "HST": 15},
"NT":{"GST": 5, "PST": 0, "HST": 0},
"NU":{"GST": 5, "PST": 0, "HST": 0},
"ON":{"GST": 0, "PST": 0, "HST": 13},
"PE":{"GST": 0, "PST": 0, "HST": 15},
"QC":{"GST": 5, "PST": 9.975, "HST": 0},
"SK":{"GST": 5, "PST": 6},
"YT":{"GST": 5, "PST": 0},
}

us_states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

canada_province_names = {
  'AB': 'Alberta',
  'BC': 'British Columbia',
  'MB': 'Manitoba',
  'NB': 'New Brunswick',
  'NL': 'Newfoundland and Labrador',
  'NS': 'Nova Scotia',
  'NT': 'Northwest Territories',
  'NU': 'Nunavut',
  'ON': 'Ontario',
  'PE': 'Prince Edward Island',
  'QC': 'Quebec',
  'SK': 'Saskatchewan',
  'YT': 'Yukon'
}

database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv',
                       dtype={"del_strt_number":str,
                                                                                "pickup_strt_number":str}).replace(np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')

width_number = 400


def check_folder(folder_name):
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the 'data' folder
    data_folder_path = os.path.join(current_directory, 'data')

    # Construct the path to the folder we want to check
    folder_to_check_path = os.path.join(data_folder_path, folder_name)

    # Check if the folder exists
    if os.path.exists(folder_to_check_path) and os.path.isdir(folder_to_check_path):
        print(f"The folder '{folder_name}' exists in the 'data' folder.")
        return True
    else:
        print(f"The folder '{folder_name}' does not exist in the 'data' folder.")
        return False


def create_folder(folder_name):
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the 'data' folder
    data_folder_path = os.path.join(current_directory, 'data')

    # Construct the path to the folder to create
    folder_to_create_path = os.path.join(data_folder_path, folder_name)

    try:
        # Create the folder
        os.makedirs(folder_to_create_path)
        print(f"Folder '{folder_name}' created successfully in the 'data' folder.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists in the 'data' folder.")


def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """
    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param txt: text to wrap in tags_
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""


def is_number_tryexcept(s):
    """ Returns True if string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False

def update_kc_id(attr, old, new):
    pass
def update_edit():
    try:
        global database, skids_dict

        for x, y in skids_dict.items():
            assert y.value.isnumeric(), f"{x} ({y}) is not a number"

        edit_comm_dict = {x: (skids_dict[f"edit_commodity_skid_number{x}"].value,
                             skids_dict[f"edit_commodity_skid_length{x}"].value,
                             skids_dict[f"edit_commodity_skid_width{x}"].value,
                             skids_dict[f"edit_commodity_skid_height{x}"].value,
                             )
                         for x in range(1, 19)
                         }

        to_db_dict = {
            "kc_id": edit_select_kc_id.value,
            "pickup_unit_number": edit_pickup_unit_number.value,
            "pickup_strt_number": edit_pickup_strt_number.value,
            "pickup_pc": edit_pickup_pc.value.replace(' ', ""),
            "pickup_strt_name": edit_pickup_strt_name.value,
            "pickup_state": edit_select_pickup_state.value,
            "pickup_city": edit_pickup_city.value,
            "pickup_date": edit_pickup_date.value,
            "pickup_shipper_name": edit_pickup_shipper_name.value,
            "pickup_shipper_number": edit_pickup_shipper_number.value,
            "pickup_shipper_contact": edit_pickup_shipper_contact.value,

            "del_unit_number": edit_del_unit_number.value,
            "del_strt_number": edit_del_strt_number.value,
            "del_pc": edit_del_pc.value.replace(' ', ""),
            "del_strt_name": edit_del_strt_name.value,
            "del_state": edit_select_del_state.value,
            "del_city": edit_del_city.value,
            "del_date": edit_del_date.value,
            "del_consignee_number": edit_del_consignee_number.value,
            "del_consignee_name": edit_del_consignee_name.value,
            "del_consignee_contact": edit_del_consignee_contact.value,

            "del2_unit_number": edit_del2_unit_number.value,
            "del2_strt_number": edit_del2_strt_number.value,
            "del2_pc": edit_del2_pc.value.replace(' ', ""),
            "del2_strt_name": edit_del2_strt_name.value,
            "del2_state": edit_select_del2_state.value,
            "del2_city": edit_del2_city.value,
            "del2_date": edit_del2_date.value,
            "del2_consignee_number": edit_del2_consignee_number.value,
            "del2_consignee_name": edit_del2_consignee_name.value,
            "del2_consignee_contact": edit_del2_consignee_contact.value,

            "carrier": edit_other_carrier.value,
            "carrier_contact": edit_other_carrier_contact.value,
            "date_invoiced": edit_other_date_invoiced.value,
            "customer_invoice_status": edit_other_customer_invoice.value,
            "carrier_invoice_status": edit_other_carrier_invoice.value,

            "charge": edit_other_charge.value,
            "profit": edit_other_profit.value,
            "cost": edit_other_cost.value,
            "tax": edit_other_tax.value,
            "tax_type": edit_other_tax_type.value,
            "invoice_total": edit_other_invoice_total.value,

            "special_notes": edit_other_special_notes.value,
            "date_ordered": edit_other_date_ordered.value,

            "commodity": edit_commodity_commodity.value,
            "commodity_weight": edit_commodity_weight.value,
            "commodity_notes": edit_commodity_notes.value,
            "commodity_skids": str(edit_comm_dict),
        }
        # ensure the postal code/zip codes are somewhat correct
        assert len(to_db_dict['pickup_pc']) >= 5, "Pickup PC too short"
        assert len(to_db_dict['pickup_pc']) <= 7, "Pickup PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['pickup_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Pickup ZIP / Postal Code ({to_db_dict['pickup_pc']})"

        assert len(to_db_dict['del_pc']) >= 5, "del PC too short"
        assert len(to_db_dict['del_pc']) <= 7, "del PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['del_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid del ZIP / Postal Code ({to_db_dict['del_pc']})"

        # ensure that the fields have the required entries
        if (to_db_dict["del2_unit_number"] or
                to_db_dict["del2_city"] or
                to_db_dict["del2_state"] or
                to_db_dict["del2_strt_name"] or
                to_db_dict["del2_pc"] or
                to_db_dict["del2_strt_number"]):
            assert len(to_db_dict['del2_strt_number']) > 1 , "del 2 Street Number  needs to be filled."
            assert len(to_db_dict['del2_city']) > 1 , "del 2 City needs to be filled."
            assert len(to_db_dict['del2_strt_name']) > 1 , "del 2 Street Name needs to be filled."
            assert len(to_db_dict['del2_pc']) >= 5, "del 2 PC too short"
            assert len(to_db_dict['del2_pc']) <= 7, "del 2 PC too long"
            assert to_db_dict['del2_state'] == to_db_dict['del_state'], "del States must be equal"
            ensure_some_numbers = [x.isnumeric() for x in to_db_dict['del2_pc']]
            assert sum(ensure_some_numbers) >= 3, f"Not a valid del 2 ZIP / Postal Code ({to_db_dict['del2_pc']})"

        # ensure that the fields have the required entries
        assert len(to_db_dict['del_strt_number']) > 1, "del Street Number  needs to be filled."
        assert len(to_db_dict['del_city']) > 1, "del City needs to be filled."
        assert len(to_db_dict['del_strt_name']) > 1, "del Street Name needs to be filled."

        assert len(to_db_dict['pickup_strt_number']) > 1, "Pickup Street Number  needs to be filled."
        assert len(to_db_dict['pickup_city']) > 1, "Pickup City needs to be filled."
        assert len(to_db_dict['pickup_strt_name']) > 1, "Pickup Street Name needs to be filled."

        assert len(to_db_dict['carrier_contact']) > 1, "Carrier Contact needs to be filled."
        assert len(to_db_dict['customer_contact']) > 1, "Customer Contact needs to be filled."
        assert len(to_db_dict['carrier']) > 1, "Carrier needs to be filled."

        # ensure that only numbers are entered into Charge/Profit/Cost fields
        assert is_number_tryexcept(str(to_db_dict['charge'])), f"Charge is not a number ({str(to_db_dict['charge'])})"
        assert is_number_tryexcept(str(to_db_dict['cost'])), f"Cost is not a number ({str(to_db_dict['cost'])})"
        assert is_number_tryexcept(str(to_db_dict['profit'])), f"Profit is not a number ({str(to_db_dict['profit'])})"
        assert float(to_db_dict['charge']) - float(to_db_dict['cost']) == float(
            to_db_dict['profit']), "Charge - Cost =/= Profit"

        # assert the commodity information (aside from skids that was already done)
        assert str(to_db_dict['commodity_weight']).strip().isnumeric(), "Commodity Weight is not a number"
        assert len(to_db_dict['commodity']) > 1, "Commodity needs to be filled."
        assert len(to_db_dict['commodity_skids']) > 6, "Commodity Skids needs to be filled."

        # assert that the del date is after the pickup date
        assert to_db_dict['del_date'] >= to_db_dict['pickup_date'], "Pickup Date must be before del Date"

        # add the new data to the database file and write it to disk
        database_modified = pd.concat([database, pd.DataFrame(to_db_dict, index=[0])], ignore_index=True)
        # print(database_modified.to_string())
        database_modified.to_csv(data_path + 'kc_logistics_corp_booking_data.csv', index=False)

        # confirm that data for the KC_ID was added to the database file.
        edit_display_div.text = wrap_in_paragraphs(f"Data for {edit_select_kc_id.value} passed to the database")
        time.sleep(2)
        # reset the database file, with the newest row added
        database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv', dtype={"del_strt_number": str,
                                                                                        "pickup_strt_number": str}).replace(
            np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')
    except Exception as iee:
        print(iee)
        edit_display_div.text = wrap_in_paragraphs(f"Error: {iee}")

def update_new_tax_type(attr, old, new):
    pass
def update_search():
    new_kc_id = edit_select_kc_id.value
    data_dict_ = database[database['kc_id'] == new_kc_id].iloc[0].to_dict()
    skids_ = ast.literal_eval(data_dict_["commodity_skids"])
    empty_skids_ = {x: (0, 0, 0, 0) for x in range(1, 19)}
    skids_ = {**empty_skids_, **skids_}

    if (data_dict_["del2_unit_number"] or
        data_dict_["del2_city"] or
        data_dict_["del2_state"] or
        data_dict_["del2_strt_name"] or
        data_dict_["del2_pc"] or
        data_dict_["del2_strt_number"]):

        edit_pickup_del_layout.children.append(edit_del2_feature)
    else:
        if len(edit_pickup_del_layout.children) < 4:
            pass
        else:
            edit_pickup_del_layout.children = edit_pickup_del_layout.children[:-1]

    edit_display_div.text = wrap_in_paragraphs(f"""Now viewing {new_kc_id}""")

    # pickup
    edit_pickup_unit_number.value=str(data_dict_["pickup_unit_number"])
    edit_pickup_strt_number.value=str(data_dict_["pickup_strt_number"])
    edit_pickup_pc.value=str(data_dict_["pickup_pc"])
    edit_pickup_strt_name.value=str(data_dict_["pickup_strt_name"])
    edit_select_pickup_state.value=str(data_dict_["pickup_state"])
    edit_pickup_city.value=str(data_dict_["pickup_city"])
    edit_pickup_date.value = str(data_dict_['pickup_date'])
    # del
    edit_del_unit_number.value=str(data_dict_["del_unit_number"])
    edit_del_strt_number.value=str(data_dict_["del_strt_number"])
    edit_del_pc.value=str(data_dict_["del_pc"])
    edit_del_strt_name.value=str(data_dict_["del_strt_name"])
    edit_select_del_state.value=str(data_dict_["del_state"])
    edit_del_city.value=str(data_dict_["del_city"])
    edit_del_date.value = str(data_dict_['del_date'])
    edit_del_consignee_name.value = str(data_dict_['del_consignee_name'])
    edit_del_consignee_number.value = str(data_dict_['del_consignee_number'])
    edit_del_consignee_contact.value = str(data_dict_['del_consignee_contact'])

    edit_del2_unit_number.value=str(data_dict_["del2_unit_number"])
    edit_del2_strt_number.value=str(data_dict_["del2_strt_number"])
    edit_del2_pc.value=str(data_dict_["del2_pc"])
    edit_del2_strt_name.value=str(data_dict_["del2_strt_name"])
    edit_select_del2_state.value=str(data_dict_["del2_state"])
    edit_del2_city.value=str(data_dict_["del2_city"])
    edit_del2_date.value = str(data_dict_['del2_date'])
    edit_del2_consignee_name.value = str(data_dict_['del2_consignee_name'])
    edit_del2_consignee_number.value = str(data_dict_['del2_consignee_number'])
    edit_del2_consignee_contact.value = str(data_dict_['del2_consignee_contact'])

    # other
    edit_other_charge.value=str(data_dict_["charge"])
    edit_other_cost.value=str(data_dict_["cost"])
    edit_other_profit.value=str(data_dict_["profit"])
    edit_other_special_notes.value=str(data_dict_["special_notes"])
    edit_other_carrier_invoice.value=str(data_dict_["carrier_invoice_status"])
    edit_other_carrier.value = str(data_dict_['carrier'])
    edit_other_carrier_contact.value = str(data_dict_['carrier_contact'])
    edit_other_date_invoiced.value = str(data_dict_['date_invoiced'])
    edit_other_customer_invoice.value = str(data_dict_['customer_invoice_status'])



    edit_other_tax.value = str(data_dict_['tax'])
    edit_other_tax_type.value = str(data_dict_['tax_type'])
    edit_other_date_ordered.value = str(data_dict_['date_ordered'])
    edit_other_invoice_total.value = str(data_dict_['invoice_total'])

    edit_pickup_shipper_number.value = str(data_dict_['pickup_shipper_number'])
    edit_pickup_shipper_name.value = str(data_dict_['pickup_shipper_name'])
    edit_pickup_shipper_contact.value = str(data_dict_['pickup_shipper_contact'])

    # commodity
    edit_commodity_notes.value=str(data_dict_["commodity_notes"])
    edit_commodity_weight.value=str(data_dict_["commodity_weight"])
    edit_commodity_commodity.value=str(data_dict_["commodity"])
    for y in range(1,19):
        skids_dict[f"edit_commodity_skid_number{y}"].value=str(skids_[y][0])
        skids_dict[f"edit_commodity_skid_length{y}"].value = str(skids_[y][1])
        skids_dict[f"edit_commodity_skid_width{y}"].value = str(skids_[y][2])
        skids_dict[f"edit_commodity_skid_height{y}"].value = str(skids_[y][3])

def update_new():
    try:
        global database, new_skids_dict

        for x,y in new_skids_dict.items():
            assert y.value.isnumeric(), f"{x} ({y}) is not a number"

        new_comm_dict = {x:(new_skids_dict[f"new_commodity_skid_number{x}"].value,
                            new_skids_dict[f"new_commodity_skid_length{x}"].value,
                            new_skids_dict[f"new_commodity_skid_width{x}"].value,
                            new_skids_dict[f"new_commodity_skid_height{x}"].value,
                            )
            for x in range(1,19)
        }

        to_db_dict = {
        "kc_id": new_select_kc_id.value,
        "pickup_unit_number": new_pickup_unit_number.value,
        "pickup_strt_number": new_pickup_strt_number.value,
        "pickup_pc": new_pickup_pc.value.replace(' ', ""),
        "pickup_strt_name": new_pickup_strt_name.value,
        "pickup_state": new_select_pickup_state.value,
        "pickup_city": new_pickup_city.value,
        "pickup_date": new_pickup_date.value,
        "shipper_contact": new_pickup_shipper_contact.value,
        "shipper_name": new_pickup_shipper_name.value,
        "shipper_number": new_pickup_shipper_number.value,

        "del_unit_number": new_del_unit_number.value,
        "del_strt_number": new_del_strt_number.value,
        "del_pc": new_del_pc.value.replace(' ', ""),
        "del_strt_name": new_del_strt_name.value,
        "del_state": new_select_del_state.value,
        "del_city": new_del_city.value,
        "del_date": new_del_date.value,
        "del_consignee_number": new_del_consignee_number.value,
        "del_consignee_contact": new_del_consignee_contact.value,
        "del_consignee_name": new_del_consignee_name.value,

        "del2_unit_number": new_del2_unit_number.value,
        "del2_strt_number": new_del2_strt_number.value,
        "del2_pc": new_del2_pc.value.replace(' ', ""),
        "del2_strt_name": new_del2_strt_name.value,
        "del2_state": new_select_del2_state.value,
        "del2_city": new_del2_city.value,
        "del2_date": new_del2_date.value,
        "del2_consignee_number": new_del2_consignee_number.value,
        "del2_consignee_contact": new_del2_consignee_contact.value,
        "del2_consignee_name": new_del2_consignee_name.value,

        "carrier": new_other_carrier.value,
        "carrier_contact": new_other_carrier_contact.value,
        "date_invoiced": new_other_date_invoiced.value,
        "customer_invoice_status": new_other_customer_invoice.value,
        "carrier_invoice_status": new_other_carrier_invoice.value,

        "charge": float(new_other_charge.value), # the amount we're charging the customer
        "cost": float(new_other_cost.value), # cost to our company

        "date_ordered": new_other_date_ordered.value,
        "special_notes": new_other_special_notes.value,

        "commodity": new_commodity_commodity.value,
        "commodity_weight": float(new_commodity_weight.value),
        "commodity_notes": new_commodity_notes.value,
        "commodity_skids":str(new_comm_dict),
        }

        state = to_db_dict['del_state']
        tax_state = canada_tax_rates[state]
        tax_rate = sum([y/100 for x, y in tax_state.items() if y > 0])
        tax_type = '/'.join(sorted([x for x, y in tax_state.items() if y > 0]))

        calculated_vals = {
            "profit": float(to_db_dict['charge']) - float(to_db_dict['cost']),
            "tax": float(to_db_dict['charge']) * float(tax_rate),
            "tax_type": tax_type,
            "invoice_total": float(to_db_dict['charge']) + (to_db_dict['charge'] * tax_rate)
        }
        pprint(calculated_vals)
        print(tax_rate, tax_state, tax_type, state, )
        to_db_dict.update(calculated_vals)


        # ensure the postal code/zip codes are somewhat correct
        assert len(to_db_dict['pickup_pc']) >= 5, "Pickup PC too short"
        assert len(to_db_dict['pickup_pc']) <= 7, "Pickup PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['pickup_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid Pickup ZIP / Postal Code ({to_db_dict['pickup_pc']})"

        assert len(to_db_dict['del_pc']) >= 5, "del PC too short"
        assert len(to_db_dict['del_pc']) <= 7, "del PC too long"
        ensure_some_numbers = [x.isnumeric() for x in to_db_dict['del_pc']]
        assert sum(ensure_some_numbers) >= 3, f"Not a valid del ZIP / Postal Code ({to_db_dict['del_pc']})"

        # ensure that the fields have the required entries
        assert len(to_db_dict['del_strt_number']) > 1 , "del Street Number  needs to be filled."
        assert len(to_db_dict['del_city']) > 1 , "del City needs to be filled."
        assert len(to_db_dict['del_strt_name']) > 1 , "del Street Name needs to be filled."

        # ensure that the fields have the required entries
        if (to_db_dict["del2_unit_number"] or
                to_db_dict["del2_city"] or
                to_db_dict["del2_state"] or
                to_db_dict["del2_strt_name"] or
                to_db_dict["del2_pc"] or
                to_db_dict["del2_strt_number"]):
            assert len(to_db_dict['del2_strt_number']) > 1 , "del 2 Street Number  needs to be filled."
            assert len(to_db_dict['del2_city']) > 1 , "del 2 City needs to be filled."
            assert len(to_db_dict['del2_strt_name']) > 1 , "del 2 Street Name needs to be filled."
            assert len(to_db_dict['del2_pc']) >= 5, "del 2 PC too short"
            assert len(to_db_dict['del2_pc']) <= 7, "del 2 PC too long"
            ensure_some_numbers = [x.isnumeric() for x in to_db_dict['del2_pc']]
            assert sum(ensure_some_numbers) >= 3, f"Not a valid del 2 ZIP / Postal Code ({to_db_dict['del2_pc']})"

        assert len(to_db_dict['pickup_strt_number']) > 1 , "Pickup Street Number  needs to be filled."
        assert len(to_db_dict['pickup_city']) > 1 , "Pickup City needs to be filled."
        assert len(to_db_dict['pickup_strt_name']) > 1 , "Pickup Street Name needs to be filled."

        assert len(to_db_dict['carrier_contact']) > 1 , "Carrier Contact needs to be filled."
        assert len(to_db_dict['carrier']) > 1 , "Carrier needs to be filled."

        # ensure that only numbers are entered into Charge/Profit/Cost fields
        assert is_number_tryexcept(str(to_db_dict['charge'])), f"Charge is not a number ({str(to_db_dict['charge'])})"
        assert is_number_tryexcept(str(to_db_dict['cost'])), f"Cost is not a number ({str(to_db_dict['cost'])})"
        assert is_number_tryexcept(str(to_db_dict['profit'])), f"Profit is not a number ({str(to_db_dict['profit'])})"
        assert float(to_db_dict['charge']) - float(to_db_dict['cost']) == float(to_db_dict['profit']), "Charge - Cost =/= Profit"

        # assert the commodity information (aside from skids that was already done)
        assert is_number_tryexcept(to_db_dict['commodity_weight']), "Commodity Weight is not a number"
        assert len(to_db_dict['commodity']) > 1 , "Commodity needs to be filled."
        assert len(to_db_dict['commodity_skids']) > 6 , "Commodity Skids needs to be filled."

        # add the new data to the database file and write it to disk
        database_modified = pd.concat([database, pd.DataFrame(to_db_dict, index=[0])], ignore_index=True)
        # print(database_modified.to_string())
        database_modified.to_csv(data_path + 'kc_logistics_corp_booking_data.csv', index=False)

        # confirm that data for the KC_ID was added to the database file.
        new_display_div.text = wrap_in_paragraphs(f"Data for {new_select_kc_id.value} passed to the database")
        time.sleep(2)
        # reset the database file, with the newest row added
        database = pd.read_csv(data_path + 'kc_logistics_corp_booking_data.csv', dtype={"del_strt_number": str,
                                                                                        "pickup_strt_number": str}).replace(
            np.nan, '').drop_duplicates(subset=['kc_id'], keep='last')
        # find the next KC_ID value
        next_kc_id_ = 'KC' + str(max([int(x[2:]) for x in database['kc_id'].values]) + 1)
        new_select_kc_id.value = next_kc_id_
        new_select_kc_id.options = [next_kc_id_]
        edit_select_kc_id.options = database['kc_id'].to_list()

        # reset some fields so that a double tab doesn't add a second row of the same data
        new_del_unit_number.value = ""
        new_del_pc.value = ""
        new_del_strt_number.value = ""
        new_del_strt_name.value = ""
        new_del_city.value = ""
        new_del_date.value = ""
        new_del_consignee_contact.value = ""
        new_del_consignee_name.value = ""
        new_del_consignee_number.value = ""

        new_del2_unit_number.value = ""
        new_del2_pc.value = ""
        new_del2_strt_number.value = ""
        new_del2_strt_name.value = ""
        new_del2_city.value = ""
        new_del2_consignee_contact.value = ""
        new_del2_consignee_name.value = ""
        new_del2_consignee_number.value = ""

        new_pickup_strt_number.value = ""
        new_pickup_pc.value = ""
        new_pickup_unit_number.value = ""
        new_pickup_strt_name.value = ""
        new_pickup_city.value = ""
        new_pickup_date.value = ""
        new_pickup_shipper_name.value = ""
        new_pickup_shipper_contact.value = ""
        new_pickup_shipper_number.value = ""

        new_other_date_ordered.value = ""
        new_other_date_invoiced.value = ""

        new_other_profit.value = ""
        new_other_cost.value = ""
        new_other_charge.value = ""
        new_other_carrier.value = ""
        new_other_carrier_contact.value = ""
        new_other_date_invoiced.value = ""

        new_commodity_commodity.value = ""
        new_commodity_weight.value = ""
        new_commodity_notes.value = ""

    except Exception as eee:
        print(error_handling())
        print(eee)
        new_display_div.text = wrap_in_paragraphs(f"Error: {eee}")

def error_handling() -> str:
    """
    This function returns a string with all of the information regarding the error
    :return: string with the error information
    """
    return traceback.format_exc()
    
def update_create_invoice():
    global skids_dict

    if not check_folder(edit_select_kc_id.value):
        create_folder(edit_select_kc_id.value)

    edit_comm_dict = {x: (skids_dict[f"edit_commodity_skid_number{x}"].value,
                          skids_dict[f"edit_commodity_skid_length{x}"].value,
                          skids_dict[f"edit_commodity_skid_width{x}"].value,
                          skids_dict[f"edit_commodity_skid_height{x}"].value,
                          )
                      for x in range(1, 19)
                      }
    info_dict = {
        "kc_id": edit_select_kc_id.value,
        "pickup_unit_number": edit_pickup_unit_number.value,
        "pickup_strt_number": edit_pickup_strt_number.value,
        "pickup_pc": edit_pickup_pc.value.replace(' ', ""),
        "pickup_strt_name": edit_pickup_strt_name.value,
        "pickup_state": edit_select_pickup_state.value,
        "pickup_city": edit_pickup_city.value,
        "pickup_date": edit_pickup_date.value,
        "pickup_shipper_name": edit_pickup_shipper_name.value,
        "pickup_shipper_number": edit_pickup_shipper_number.value,
        "pickup_shipper_contact": edit_pickup_shipper_contact.value,

        "del_unit_number": edit_del_unit_number.value,
        "del_strt_number": edit_del_strt_number.value,
        "del_pc": edit_del_pc.value.replace(' ', ""),
        "del_strt_name": edit_del_strt_name.value,
        "del_state": edit_select_del_state.value,
        "del_city": edit_del_city.value,
        "del_date": edit_del_date.value,
        "del_consignee_number": edit_del_consignee_number.value,
        "del_consignee_name": edit_del_consignee_name.value,
        "del_consignee_contact": edit_del_consignee_contact.value,

        "del2_unit_number": edit_del2_unit_number.value,
        "del2_strt_number": edit_del2_strt_number.value,
        "del2_pc": edit_del2_pc.value.replace(' ', ""),
        "del2_strt_name": edit_del2_strt_name.value,
        "del2_state": edit_select_del2_state.value,
        "del2_city": edit_del2_city.value,
        "del2_date": edit_del2_date.value,
        "del2_consignee_number": edit_del2_consignee_number.value,
        "del2_consignee_name": edit_del2_consignee_name.value,
        "del2_consignee_contact": edit_del2_consignee_contact.value,

        "carrier": edit_other_carrier.value,
        "carrier_contact": edit_other_carrier_contact.value,
        "date_invoiced": edit_other_date_invoiced.value,
        "customer_invoice_status": edit_other_customer_invoice.value,
        "carrier_invoice_status": edit_other_carrier_invoice.value,

        "charge": edit_other_charge.value,
        "profit": edit_other_profit.value,
        "cost": edit_other_cost.value,
        "tax": edit_other_tax.value,
        "tax_type": edit_other_tax_type.value,
        "invoice_total": edit_other_invoice_total.value,

        "special_notes": edit_other_special_notes.value,
        "date_ordered": edit_other_date_ordered.value,




        "commodity": edit_commodity_commodity.value,
        "commodity_weight": edit_commodity_weight.value,
        "commodity_notes": edit_commodity_notes.value,
        "commodity_skids": str(edit_comm_dict),
    }
    # only worry about 'active' skids
    active_skids = {x:y for x,y in edit_comm_dict.items() if int(y[0]) > 0 }
    # create the different skids
    skids = ''
    for x,y in active_skids.items():
        if int(y[0]) > 1:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |" * int(y[0])
        else:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |"
    skids = skids[:-1].strip()
    # count the number of skids
    number_of_skids = sum([int(y[0]) for x,y in active_skids.items() if int(y[0]) > 0])

    # use the Word doc template
    document = DocxTemplate(data_path + "invoice_template.docx")
    # add extra variables to the info_dict
    context = {
               'skids': skids,
               'number_of_skids': number_of_skids,
               'business_number': constants['business_number'],
               'terms': constants['terms'],
               'cstmr_reference': constants['customer_reference_#'],
                }
    pprint(context)
    context.update(info_dict)
    document.render(context)
    save_path = data_path + f'{info_dict['kc_id']}/' + f"{info_dict['kc_id']}_invoice_{today.strftime('%F').replace('-','_')}.docx"
    document.save(save_path)
    text = f"{info_dict['kc_id']} INVOICE created at {datetime.datetime.now()}, saved to {save_path}"
    print(text)
    edit_display_div.text = wrap_in_paragraphs(f"""{text}<br>Now viewing {info_dict['kc_id']}""")

def update_create_bol():
    global skids_dict

    if not check_folder(edit_select_kc_id.value):
        create_folder(edit_select_kc_id.value)

    edit_comm_dict = {x: (skids_dict[f"edit_commodity_skid_number{x}"].value,
                          skids_dict[f"edit_commodity_skid_length{x}"].value,
                          skids_dict[f"edit_commodity_skid_width{x}"].value,
                          skids_dict[f"edit_commodity_skid_height{x}"].value,
                          )
                      for x in range(1, 19)
                      }
    info_dict = {
        "kc_id": edit_select_kc_id.value,
        "pickup_unit_number": edit_pickup_unit_number.value,
        "pickup_strt_number": edit_pickup_strt_number.value,
        "pickup_pc": edit_pickup_pc.value.replace(' ', ""),
        "pickup_strt_name": edit_pickup_strt_name.value,
        "pickup_state": edit_select_pickup_state.value,
        "pickup_city": edit_pickup_city.value,
        "pickup_date": edit_pickup_date.value,
        "pickup_shipper_name": edit_pickup_shipper_name.value,
        "pickup_shipper_number": edit_pickup_shipper_number.value,
        "pickup_shipper_contact": edit_pickup_shipper_contact.value,

        "del_unit_number": edit_del_unit_number.value,
        "del_strt_number": edit_del_strt_number.value,
        "del_pc": edit_del_pc.value.replace(' ', ""),
        "del_strt_name": edit_del_strt_name.value,
        "del_state": edit_select_del_state.value,
        "del_city": edit_del_city.value,
        "del_date": edit_del_date.value,
        "del_consignee_number": edit_del_consignee_number.value,
        "del_consignee_name": edit_del_consignee_name.value,
        "del_consignee_contact": edit_del_consignee_contact.value,

        "del2_unit_number": edit_del2_unit_number.value,
        "del2_strt_number": edit_del2_strt_number.value,
        "del2_pc": edit_del2_pc.value.replace(' ', ""),
        "del2_strt_name": edit_del2_strt_name.value,
        "del2_state": edit_select_del2_state.value,
        "del2_city": edit_del2_city.value,
        "del2_date": edit_del2_date.value,
        "del2_consignee_number": edit_del2_consignee_number.value,
        "del2_consignee_name": edit_del2_consignee_name.value,
        "del2_consignee_contact": edit_del2_consignee_contact.value,

        "carrier": edit_other_carrier.value,
        "carrier_contact": edit_other_carrier_contact.value,
        "date_invoiced": edit_other_date_invoiced.value,
        "customer_invoice_status": edit_other_customer_invoice.value,
        "carrier_invoice_status": edit_other_carrier_invoice.value,

        "charge": edit_other_charge.value,
        "profit": edit_other_profit.value,
        "cost": edit_other_cost.value,
        "tax": edit_other_tax.value,
        "tax_type": edit_other_tax_type.value,
        "invoice_total": edit_other_invoice_total.value,

        "special_notes": edit_other_special_notes.value,
        "date_ordered": edit_other_date_ordered.value,




        "commodity": edit_commodity_commodity.value,
        "commodity_weight": edit_commodity_weight.value,
        "commodity_notes": edit_commodity_notes.value,
        "commodity_skids": str(edit_comm_dict),
    }

    # only worry about 'active' skids
    active_skids = {x:y for x,y in edit_comm_dict.items() if int(y[0]) > 0 }
    # create the different skids
    skids = ''
    for x,y in active_skids.items():
        if int(y[0]) > 1:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |" * int(y[0])
        else:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |"
    skids = skids[:-1].strip()
    # count the number of skids
    number_of_skids = sum([int(y[0]) for x,y in active_skids.items() if int(y[0]) > 0])

    # use the Word doc template
    document = DocxTemplate(data_path + "BoL_template.docx")
    # add extra variables to the info_dict
    context = {
               'skids': skids,
               'number_of_skids': number_of_skids,
               'business_number': constants['business_number'],
               'terms': constants['terms'],
               'cstmr_reference': constants['customer_reference_#'],
                }
    pprint(context)
    context.update(info_dict)
    document.render(context)
    save_path = data_path + f'{info_dict['kc_id']}/' + f"{info_dict['kc_id']}_BoL_{today.strftime('%F').replace('-','_')}.docx"
    document.save(save_path)
    text = f"{info_dict['kc_id']} Bill of Lading created at {datetime.datetime.now()}, saved to {save_path}"
    print(text)
    edit_display_div.text = wrap_in_paragraphs(f"""{text}<br>Now viewing {info_dict['kc_id']}""")

def update_create_loadconf():
    global skids_dict

    if not check_folder(edit_select_kc_id.value):
        create_folder(edit_select_kc_id.value)

    edit_comm_dict = {x: (skids_dict[f"edit_commodity_skid_number{x}"].value,
                          skids_dict[f"edit_commodity_skid_length{x}"].value,
                          skids_dict[f"edit_commodity_skid_width{x}"].value,
                          skids_dict[f"edit_commodity_skid_height{x}"].value,
                          )
                      for x in range(1, 19)
                      }
    info_dict = {
        "kc_id": edit_select_kc_id.value,
        "pickup_unit_number": edit_pickup_unit_number.value,
        "pickup_strt_number": edit_pickup_strt_number.value,
        "pickup_pc": edit_pickup_pc.value.replace(' ', ""),
        "pickup_strt_name": edit_pickup_strt_name.value,
        "pickup_state": edit_select_pickup_state.value,
        "pickup_city": edit_pickup_city.value,
        "pickup_date": edit_pickup_date.value,
        "pickup_shipper_name": edit_pickup_shipper_name.value,
        "pickup_shipper_number": edit_pickup_shipper_number.value,
        "pickup_shipper_contact": edit_pickup_shipper_contact.value,

        "del_unit_number": edit_del_unit_number.value,
        "del_strt_number": edit_del_strt_number.value,
        "del_pc": edit_del_pc.value.replace(' ', ""),
        "del_strt_name": edit_del_strt_name.value,
        "del_state": edit_select_del_state.value,
        "del_city": edit_del_city.value,
        "del_date": edit_del_date.value,
        "del_consignee_number": edit_del_consignee_number.value,
        "del_consignee_name": edit_del_consignee_name.value,
        "del_consignee_contact": edit_del_consignee_contact.value,

        "del2_unit_number": edit_del2_unit_number.value,
        "del2_strt_number": edit_del2_strt_number.value,
        "del2_pc": edit_del2_pc.value.replace(' ', ""),
        "del2_strt_name": edit_del2_strt_name.value,
        "del2_state": edit_select_del2_state.value,
        "del2_city": edit_del2_city.value,
        "del2_date": edit_del2_date.value,
        "del2_consignee_number": edit_del2_consignee_number.value,
        "del2_consignee_name": edit_del2_consignee_name.value,
        "del2_consignee_contact": edit_del2_consignee_contact.value,

        "carrier": edit_other_carrier.value,
        "carrier_contact": edit_other_carrier_contact.value,
        "date_invoiced": edit_other_date_invoiced.value,
        "customer_invoice_status": edit_other_customer_invoice.value,
        "carrier_invoice_status": edit_other_carrier_invoice.value,

        "charge": edit_other_charge.value,
        "profit": edit_other_profit.value,
        "cost": edit_other_cost.value,
        "tax": edit_other_tax.value,
        "tax_type": edit_other_tax_type.value,
        "invoice_total": edit_other_invoice_total.value,

        "special_notes": edit_other_special_notes.value,
        "date_ordered": edit_other_date_ordered.value,




        "commodity": edit_commodity_commodity.value,
        "commodity_weight": edit_commodity_weight.value,
        "commodity_notes": edit_commodity_notes.value,
        "commodity_skids": str(edit_comm_dict),
    }

    # only worry about 'active' skids
    active_skids = {x:y for x,y in edit_comm_dict.items() if int(y[0]) > 0 }
    # create the different skids
    skids = ''
    for x,y in active_skids.items():
        if int(y[0]) > 1:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |" * int(y[0])
        else:
            skids = skids + f"{y[1]}x{y[2]}x{y[3]} |"
    skids = skids[:-1].strip()
    # count the number of skids
    number_of_skids = sum([int(y[0]) for x,y in active_skids.items() if int(y[0]) > 0])

    # use the Word doc template
    document = DocxTemplate(data_path + "load_confirmation_template.docx")
    # add extra variables to the info_dict
    context = {
               'skids': skids,
               'number_of_skids': number_of_skids,
               'business_number': constants['business_number'],
               'terms': constants['terms'],
               'cstmr_reference': constants['customer_reference_#'],
                }
    pprint(context)
    context.update(info_dict)
    document.render(context)
    save_path = data_path + f'{info_dict['kc_id']}/' + f"{info_dict['kc_id']}_loadconf_{today.strftime('%F').replace('-','_')}.docx"
    document.save(save_path)
    text = f"{info_dict['kc_id']} LOAD CONFIRMATION created at {datetime.datetime.now()}, saved to {save_path}"
    print(text)
    edit_display_div.text = wrap_in_paragraphs(f"""{text}<br>Now viewing {info_dict['kc_id']}""")

def update_kc_id_next(attkc_idr, old, new):
    pass

def add_new_del_destination():
    # There are 3 things normally, if only 3 now, add one more del. If there are 4, do not add another del.
    if len(new_pickup_del_layout.children) < 4:
        new_pickup_del_layout.children.append(new_del2_feature)

def add_edit_del_destination():
    # There are 3 things normally, if only 3 now, add one more del. If there are 4, do not add another del.
    if len(edit_pickup_del_layout.children) < 4:
        edit_pickup_del_layout.children.append(edit_del2_feature)


title_div = Div(text=wrap_in_paragraphs('KC Logistics Data Input', 'black', size=5), width = width_number)
new_info_div = Div(text=wrap_in_paragraphs("""New Data Input for KC Logistics Data """, 'black', size=3), width = 300)

new_display_div = Div(text="")

next_kc_id = 'KC' + str(max([int(x[2:]) for x in database['kc_id'].values]) + 1)

new_select_kc_id =  Select(title='KC_ID', value=next_kc_id, options=[next_kc_id], width=width_number)
new_select_kc_id.on_change('value', update_kc_id_next)

new_div_0 = Div(text = '_'*15)
new_div_1 = Div(text = '_'*15)
new_div_2 = Div(text = '_'*130)
new_div_3 = Div(text = '_'*130)

### PICKUP
new_div_pickup = Div(text=wrap_in_paragraphs("""Pickup""", 'black', size=3))

new_pickup_unit_number = TextInput(value=str(""), title="Pickup Unit Number", width= width_number)
new_pickup_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_strt_number = TextInput(value=str(""), title="Pickup Street Number", width= width_number)
new_pickup_strt_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_pc = TextInput(value=str(""), title="Pickup Postal Code/ZIP", width= width_number)
new_pickup_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_strt_name = TextInput(value=str(""), title="Pickup Street Name", width= width_number)
new_pickup_strt_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_pickup_state = Select(title='Pickup State', value=str(""), options=sorted(list(canada_province_names.keys()) + list(us_states.keys())), width=width_number)
new_select_pickup_state.on_change('value', update_kc_id)

new_pickup_city = TextInput(value=str(""), title="Pickup City", width= width_number)
new_pickup_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_date = TextInput(value=str("Monday January 1, 2024"), title="Pickup Date", width=width_number)
new_pickup_date.js_on_change("value",
                                CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_shipper_name = TextInput(value=str(""), title="Shipper Name", width= width_number)
new_pickup_shipper_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_shipper_contact = TextInput(value=str(""), title="Shipper Contact", width= width_number)
new_pickup_shipper_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_pickup_shipper_number = TextInput(value=str(""), title="Shipper Number", width= width_number)
new_pickup_shipper_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


# del
######################################
new_div_del = Div(text=wrap_in_paragraphs("""Delivery""", 'black', size=3))
new_div_del2 = Div(text=wrap_in_paragraphs("""del 2""", 'black', size=3))

new_del_unit_number = TextInput(value=str(""), title="Delivery Unit Number", width= width_number)
new_del_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_strt_number = TextInput(value=str(""), title="Delivery Street Number", width= width_number)
new_del_strt_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_pc = TextInput(value=str(""), title="Delivery Postal Code/ZIP", width= width_number)
new_del_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_strt_name = TextInput(value=str(""), title="Delivery Street Name", width= width_number)
new_del_strt_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_del_state = Select(title='Delivery State', value=str(sorted(list(canada_province_names.keys()))[0]), options=sorted(list(canada_province_names.keys()) + list(us_states.keys())), width=width_number)
new_select_del_state.on_change('value', update_kc_id)

new_del_city = TextInput(value=str(""), title="Delivery City", width= width_number)
new_del_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_date = TextInput(value=str("Monday January 1, 2024"), title="Delivery Date", width=width_number)
new_del_date.js_on_change("value",
                                CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_consignee_name = TextInput(value=str(""), title="Consignee Name", width= width_number)
new_del_consignee_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_consignee_contact = TextInput(value=str(""), title="Consignee Contact", width= width_number)
new_del_consignee_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del_consignee_number = TextInput(value=str(""), title="Consignee Number", width= width_number)
new_del_consignee_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


new_del2_unit_number = TextInput(value=str(""), title="Delivery 2 Unit Number", width=width_number)
new_del2_unit_number.js_on_change("value", CustomJS(
    code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_strt_number = TextInput(value=str(""), title="Delivery 2 Street Number", width=width_number)
new_del2_strt_number.js_on_change("value", CustomJS(
    code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_pc = TextInput(value=str(""), title="Delivery 2 Postal Code/ZIP", width=width_number)
new_del2_pc.js_on_change("value",
                              CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_strt_name = TextInput(value=str(""), title="Delivery 2 Street Name", width=width_number)
new_del2_strt_name.js_on_change("value", CustomJS(
    code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_select_del2_state = Select(title='Delivery 2 State', value=str(""),
                                    options=sorted(list(canada_province_names.keys()) + list(us_states.keys())),
                                    width=width_number)
new_select_del2_state.on_change('value', update_kc_id)

new_del2_city = TextInput(value=str(""), title="Delivery 2 City", width=width_number)
new_del2_city.js_on_change("value",
                                CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_date = TextInput(value=str("Monday January 1, 2024"), title="Delivery 2 Date", width=width_number)
new_del2_date.js_on_change("value",
                                CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_consignee_name = TextInput(value=str(""), title="Delivery 2 Consignee Name", width= width_number)
new_del2_consignee_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_consignee_contact = TextInput(value=str(""), title="Delivery 2 Consignee Contact", width= width_number)
new_del2_consignee_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_del2_consignee_number = TextInput(value=str(""), title="Delivery 2 Consignee Number", width= width_number)
new_del2_consignee_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_dest_button = Button(label="Add Delivery destination", button_type="success")
new_dest_button.on_click(add_new_del_destination)


# OTHER
################
new_div_other = Div(text=wrap_in_paragraphs("""Other""", 'black', size=3))

new_other_carrier = TextInput(value=str(""), title="Carrier", width= width_number)
new_other_carrier.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_carrier_contact = TextInput(value=str(""), title="Carrier Contact", width= width_number)
new_other_carrier_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_date_invoiced = TextInput(value=str(""), title="Date Invoiced", width= width_number)
new_other_date_invoiced.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_customer_invoice = Select(title='Customer Invoice Status', value=str("UNPAID"), options=["UNPAID", "PAID"], width=width_number)
new_other_customer_invoice.on_change('value', update_kc_id)

new_other_carrier_invoice = Select(title='Carrier Invoice Status', value=str("UNPAID"), options=["UNPAID", "PAID"], width=width_number)
new_other_carrier_invoice.on_change('value', update_kc_id)

new_other_charge = TextInput(value=str(0.0), title="Charge", width= width_number)
new_other_charge.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_profit = TextInput(value=str(""), title="Profit (auto-generated)", width= width_number)
new_other_profit.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_cost = TextInput(value=str(0.0), title="Cost", width= width_number)
new_other_cost.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_tax = TextInput(value=str(""), title="Tax (auto-generated)", width= width_number)
new_other_tax.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_tax_type = Select(title='Tax Type (auto-generated)', value=str("This depends on del province"), options=["This depends on del province"], width=width_number)
new_other_tax_type.on_change('value', update_new_tax_type)

new_other_invoice_total = TextInput(value=str(""), title="Total Invoice (auto-generated)", width= width_number)
new_other_invoice_total.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


new_other_special_notes = TextInput(value=str(""), title="Special Notes", width= 900)
new_other_special_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_other_date_ordered = TextInput(value=str(""), title="Date Ordered", width= width_number)
new_other_date_ordered.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))



# COMMODITY
##################
new_div_commodity = Div(text=wrap_in_paragraphs("""Commodity""", 'black', size=3))

new_commodity_commodity = TextInput(value=str(""), title="Commodity", width= width_number)
new_commodity_commodity.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_commodity_weight = TextInput(value=str(""), title="Weight (LBS)", width= 200)
new_commodity_weight.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_commodity_notes = TextInput(value=str(""), title="Notes", width= 900)
new_commodity_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


new_skids = {x:(0,0,0,0) for x in range(1,19)}

# SKIDS
new_skids_dict = {}
for x in range(1,19):
    new_skids_dict[f"new_commodity_skid_number{x}"] = TextInput(value=str(new_skids[x][0]), title="Number of Skids", width= 200)
    new_skids_dict[f"new_commodity_skid_number{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_height{x}"]  = TextInput(value=str(new_skids[x][3]), title="Skid Height (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_height{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_length{x}"] = TextInput(value=str(new_skids[x][1]), title="Skid Length (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_length{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    new_skids_dict[f"new_commodity_skid_width{x}"] = TextInput(value=str(new_skids[x][2]), title="Skid Width (Inches)", width= 200)
    new_skids_dict[f"new_commodity_skid_width{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

new_button = Button(label="Input Info to Database", button_type="primary", width=200)
new_button.on_click(update_new)

# EDIT / VIEW PAGE
#################################################################

edit_div_0 = Div(text = '_'*15)
edit_div_1 = Div(text = '_'*15)
edit_div_2 = Div(text = '_'*130)
edit_div_3 = Div(text = '_'*130)

start_kc_id = 'KC10'

data_dict = database[database['kc_id'] == start_kc_id].iloc[0].to_dict()

edit_info_div = Div(text=wrap_in_paragraphs("""Edit/View Data for KC Logistics Data""", 'black', size=4), width = 350)
edit_display_div = Div(text=wrap_in_paragraphs(f"""Now viewing {start_kc_id}""",), width = 350)

edit_select_kc_id = Select(title='KC_ID', value=start_kc_id, options=database['kc_id'].to_list(), width=150)
edit_select_kc_id.on_change('value', update_kc_id)

search_button = Button(label="Search Info in Database", button_type="success", width=150)
search_button.on_click(update_search)

edit_button = Button(label="Edit Info in Database", button_type="primary", width=150)
edit_button.on_click(update_edit)

create_loadconf_button = Button(label="Create Load Confirmation", button_type="warning", width=100)
create_loadconf_button.on_click(update_create_loadconf)

create_bol_button = Button(label="Create BoL", button_type="warning", width=100)
create_bol_button.on_click(update_create_bol)

create_invoice_button = Button(label="Create Invoice", button_type="warning", width=100)
create_invoice_button.on_click(update_create_invoice)


edit_add_dest_button = Button(label="Add del destination", button_type="success")
edit_add_dest_button.on_click(add_edit_del_destination)

### PICKUP
edit_div_pickup = Div(text=wrap_in_paragraphs("""Pickup""", 'black', size=3))

edit_pickup_unit_number = TextInput(value=str(data_dict["pickup_unit_number"]), title="Pickup Unit Number", width= width_number)
edit_pickup_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_strt_number = TextInput(value=str(data_dict["pickup_strt_number"]), title="Pickup Street Number", width= width_number)
edit_pickup_strt_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_pc = TextInput(value=str(data_dict["pickup_pc"]), title="Pickup Postal Code/ZIP", width= width_number)
edit_pickup_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_strt_name = TextInput(value=str(data_dict["pickup_strt_name"]), title="Pickup Street Name", width= width_number)
edit_pickup_strt_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_select_pickup_state = Select(title='Pickup State', value=str(data_dict["pickup_state"]), options=sorted(list(canada_province_names.keys()) + list(us_states.keys())), width=width_number)
edit_select_pickup_state.on_change('value', update_kc_id)

edit_pickup_city = TextInput(value=str(data_dict["pickup_city"]), title="Pickup City", width= width_number)
edit_pickup_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_date = TextInput(value=str(data_dict["pickup_date"]), title="Pickup Date", width= width_number)
edit_pickup_date.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_shipper_name = TextInput(value=str(data_dict["pickup_shipper_name"]), title="Shipper Name", width= width_number)
edit_pickup_shipper_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_shipper_contact = TextInput(value=str(data_dict["pickup_shipper_contact"]), title="Shipper Contact", width= width_number)
edit_pickup_shipper_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_pickup_shipper_number = TextInput(value=str(data_dict["pickup_shipper_number"]), title="Shipper Number", width= width_number)
edit_pickup_shipper_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


# del
######################################
edit_div_del = Div(text=wrap_in_paragraphs("""Delivery""", 'black', size=3))
edit_div_del2 = Div(text=wrap_in_paragraphs("""Delivery 2""", 'black', size=3))

edit_del_unit_number = TextInput(value=str(data_dict["del_unit_number"]), title="Delivery Unit Number", width= width_number)
edit_del_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_strt_number = TextInput(value=str(data_dict["del_strt_number"]), title="Delivery Street Number", width= width_number)
edit_del_strt_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_pc = TextInput(value=str(data_dict["del_pc"]), title="Delivery Postal Code/ZIP", width= width_number)
edit_del_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_strt_name = TextInput(value=str(data_dict["del_strt_name"]), title="Delivery Street Name", width= width_number)
edit_del_strt_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_select_del_state = Select(title='del State', value=str(data_dict["del_state"]), options=sorted(list(canada_province_names.keys()) + list(us_states.keys())), width=width_number)
edit_select_del_state.on_change('value', update_kc_id)

edit_del_city = TextInput(value=str(data_dict["del_city"]), title="Delivery City", width= width_number)
edit_del_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_date = TextInput(value=str(data_dict["del_date"]), title="Delivery Date", width= width_number)
edit_del_date.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_consignee_name = TextInput(value=str(data_dict["del_consignee_name"]), title="Delivery Consignee Name", width= width_number)
edit_del_consignee_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_consignee_contact = TextInput(value=str(data_dict["del_consignee_contact"]), title="Delivery Consignee Contact", width= width_number)
edit_del_consignee_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del_consignee_number = TextInput(value=str(data_dict["del_consignee_number"]), title="Delivery Consignee Number", width= width_number)
edit_del_consignee_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))



edit_del2_unit_number = TextInput(value=str(data_dict["del2_unit_number"]), title="Delivery 2 Unit Number", width= width_number)
edit_del2_unit_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_strt_number = TextInput(value=str(data_dict["del2_strt_number"]), title="Delivery 2 Street Number", width= width_number)
edit_del2_strt_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_pc = TextInput(value=str(data_dict["del2_pc"]), title="Delivery 2 Postal Code/ZIP", width= width_number)
edit_del2_pc.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_strt_name = TextInput(value=str(data_dict["del2_strt_name"]), title="Delivery 2 Street Name", width= width_number)
edit_del2_strt_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_select_del2_state = Select(title='Delivery 2 State', value=str(data_dict["del2_state"]), options=sorted(list(canada_province_names.keys()) + list(us_states.keys())), width=width_number)
edit_select_del2_state.on_change('value', update_kc_id)

edit_del2_city = TextInput(value=str(data_dict["del2_city"]), title="Delivery 2 City", width= width_number)
edit_del2_city.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_date = TextInput(value=str(data_dict["del2_date"]), title="Delivery 2 Date", width= width_number)
edit_del2_date.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_consignee_name = TextInput(value=str(data_dict["del2_consignee_name"]), title="Delivery 2 Consignee Name", width= width_number)
edit_del2_consignee_name.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_consignee_contact = TextInput(value=str(data_dict["del2_consignee_contact"]), title="Delivery 2 Consignee Contact", width= width_number)
edit_del2_consignee_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_del2_consignee_number = TextInput(value=str(data_dict["del2_consignee_number"]), title="Delivery 2 Consignee Number", width= width_number)
edit_del2_consignee_number.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


# OTHER
################
edit_div_other = Div(text=wrap_in_paragraphs("""Other""", 'black', size=3))

edit_other_carrier = TextInput(value=str(data_dict["carrier"]), title="Carrier", width= width_number)
edit_other_carrier.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_carrier_contact = TextInput(value=str(data_dict["carrier_contact"]), title="Carrier Contact", width= width_number)
edit_other_carrier_contact.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_date_invoiced = TextInput(value=str(data_dict["date_invoiced"]), title="Date Invoiced", width= width_number)
edit_other_date_invoiced.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_customer_invoice = Select(title='Customer Invoice Status', value=str(data_dict["customer_invoice_status"]), options=["UNPAID", "PAID"], width=width_number)
edit_other_customer_invoice.on_change('value', update_kc_id)

edit_other_carrier_invoice = Select(title='Carrier Invoice Status', value=str(data_dict["carrier_invoice_status"]), options=["UNPAID", "PAID"], width=width_number)
edit_other_carrier_invoice.on_change('value', update_kc_id)

edit_other_charge = TextInput(value=str(data_dict["charge"]), title="Charge", width= width_number)
edit_other_charge.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_profit = TextInput(value=str(data_dict["profit"]), title="Profit", width= width_number)
edit_other_profit.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_cost = TextInput(value=str(data_dict["cost"]), title="Cost", width= width_number)
edit_other_cost.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_special_notes = TextInput(value=str(data_dict["special_notes"]), title="Special Notes", width= 900)
edit_other_special_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_tax = TextInput(value=str(data_dict["tax"]), title="Tax", width= width_number)
edit_other_tax.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_tax_type = Select(title='Tax Type', value=str(data_dict["tax_type"]), options=["This depends on del province","GST", "HST"], width=width_number)
edit_other_tax_type.on_change('value', update_new_tax_type)

edit_other_invoice_total = TextInput(value=str(data_dict["invoice_total"]), title="Total Invoice", width= width_number)
edit_other_invoice_total.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_other_date_ordered = TextInput(value=str(data_dict["date_ordered"]), title="Date Ordered", width= width_number)
edit_other_date_ordered.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))


# COMMODITY
##################
edit_div_commodity = Div(text=wrap_in_paragraphs("""Commodity""", 'black', size=3))

edit_commodity_commodity = TextInput(value=str(data_dict["commodity"]), title="Commodity", width= width_number)
edit_commodity_commodity.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_commodity_weight = TextInput(value=str(data_dict["commodity_weight"]), title="Weight (LBS)", width= 200)
edit_commodity_weight.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

edit_commodity_notes = TextInput(value=str(data_dict["commodity_notes"]), title="Notes", width= 900)
edit_commodity_notes.js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

skids = ast.literal_eval(data_dict["commodity_skids"])
empty_skids = {x:(0,0,0,0) for x in range(1,19)}
skids = {**empty_skids, **skids}

# SKIDS
skids_dict = {}
for x in range(1,19):
    skids_dict[f"edit_commodity_skid_number{x}"] = TextInput(value=str(skids[x][0]), title="Number of Skids", width= 200)
    skids_dict[f"edit_commodity_skid_number{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_height{x}"]  = TextInput(value=str(skids[x][3]), title="Skid Height (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_height{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_length{x}"] = TextInput(value=str(skids[x][1]), title="Skid Length (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_length{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

    skids_dict[f"edit_commodity_skid_width{x}"] = TextInput(value=str(skids[x][2]), title="Skid Width (Inches)", width= 200)
    skids_dict[f"edit_commodity_skid_width{x}"].js_on_change("value", CustomJS(code="""console.log('text_input: value=' + this.value, this.toString())"""))

# LAYOUT

new_pickup_del_layout = row([
                      column([new_div_pickup, new_pickup_strt_number,
                              new_pickup_strt_name,
                              new_pickup_unit_number,
                              new_pickup_city,
                              new_select_pickup_state,
                              new_pickup_pc,
                              new_pickup_date,
                              new_pickup_shipper_name,
                              new_pickup_shipper_contact,
                              new_pickup_shipper_number,
                              ]),
                      new_div_0,
                      column([new_div_del, new_del_strt_number,
                              new_del_strt_name,
                              new_del_unit_number,
                              new_del_city,
                              new_select_del_state,
                              new_del_pc,
                              new_del_date,
                              new_del_consignee_name,
                              new_del_consignee_contact,
                              new_del_consignee_number,
                              ]), ])

new_del2_feature = column([new_div_del2, new_del2_strt_number,
                                new_del2_strt_name,
                                new_del2_unit_number,
                                new_del2_city,
                                new_select_del2_state,
                                new_del2_pc,
                                new_del2_date,
                                new_del2_consignee_name,
                                new_del2_consignee_contact,
                                new_del2_consignee_number,
                                ])

new_tab = TabPanel(
    child=column([row([new_info_div, new_select_kc_id, new_button, new_dest_button]),
                  new_display_div,
                    new_pickup_del_layout,
                  new_div_2,
                  new_div_other,
                  row([
                      column([
                          new_other_carrier,
                              new_other_carrier_contact,
                            new_other_date_ordered,
                              new_other_date_invoiced,
                              new_other_customer_invoice,
                              new_other_carrier_invoice,
                              ]),
                      new_div_1,
                      column([
                          new_other_charge,
                          new_other_cost,
                          new_other_tax_type,
                          new_other_tax,
                          new_other_invoice_total,
                          new_other_profit,
                      ]),
                  ]),
                  new_other_special_notes,
                  new_div_3,
                  new_div_commodity,
                  new_commodity_commodity,
                  new_commodity_weight,
                  new_commodity_notes,
                  row([new_skids_dict[f"new_commodity_skid_number1"], new_skids_dict[f"new_commodity_skid_length1"],
                       new_skids_dict[f"new_commodity_skid_width1"], new_skids_dict[f"new_commodity_skid_height1"]]),
                  row([new_skids_dict[f"new_commodity_skid_number2"], new_skids_dict[f"new_commodity_skid_length2"],
                       new_skids_dict[f"new_commodity_skid_width2"], new_skids_dict[f"new_commodity_skid_height2"]]),
                  row([new_skids_dict[f"new_commodity_skid_number3"], new_skids_dict[f"new_commodity_skid_length3"],
                       new_skids_dict[f"new_commodity_skid_width3"], new_skids_dict[f"new_commodity_skid_height3"]]),
                  row([new_skids_dict[f"new_commodity_skid_number4"], new_skids_dict[f"new_commodity_skid_length4"],
                       new_skids_dict[f"new_commodity_skid_width4"], new_skids_dict[f"new_commodity_skid_height4"]]),
                  row([new_skids_dict[f"new_commodity_skid_number5"], new_skids_dict[f"new_commodity_skid_length5"],
                       new_skids_dict[f"new_commodity_skid_width5"], new_skids_dict[f"new_commodity_skid_height5"]]),
                  row([new_skids_dict[f"new_commodity_skid_number6"], new_skids_dict[f"new_commodity_skid_length6"],
                       new_skids_dict[f"new_commodity_skid_width6"], new_skids_dict[f"new_commodity_skid_height6"]]),
                  row([new_skids_dict[f"new_commodity_skid_number7"], new_skids_dict[f"new_commodity_skid_length7"],
                       new_skids_dict[f"new_commodity_skid_width7"], new_skids_dict[f"new_commodity_skid_height7"]]),
                  row([new_skids_dict[f"new_commodity_skid_number8"], new_skids_dict[f"new_commodity_skid_length8"],
                       new_skids_dict[f"new_commodity_skid_width8"], new_skids_dict[f"new_commodity_skid_height8"]]),
                  row([new_skids_dict[f"new_commodity_skid_number9"], new_skids_dict[f"new_commodity_skid_length9"],
                       new_skids_dict[f"new_commodity_skid_width9"], new_skids_dict[f"new_commodity_skid_height9"]]),
                  row([new_skids_dict[f"new_commodity_skid_number10"], new_skids_dict[f"new_commodity_skid_length10"],
                       new_skids_dict[f"new_commodity_skid_width10"], new_skids_dict[f"new_commodity_skid_height10"]]),
                  row([new_skids_dict[f"new_commodity_skid_number11"], new_skids_dict[f"new_commodity_skid_length11"],
                       new_skids_dict[f"new_commodity_skid_width11"], new_skids_dict[f"new_commodity_skid_height11"]]),
                  row([new_skids_dict[f"new_commodity_skid_number12"], new_skids_dict[f"new_commodity_skid_length12"],
                       new_skids_dict[f"new_commodity_skid_width12"], new_skids_dict[f"new_commodity_skid_height12"]]),
                  row([new_skids_dict[f"new_commodity_skid_number13"], new_skids_dict[f"new_commodity_skid_length13"],
                       new_skids_dict[f"new_commodity_skid_width13"], new_skids_dict[f"new_commodity_skid_height13"]]),
                  row([new_skids_dict[f"new_commodity_skid_number14"], new_skids_dict[f"new_commodity_skid_length14"],
                       new_skids_dict[f"new_commodity_skid_width14"], new_skids_dict[f"new_commodity_skid_height14"]]),
                  row([new_skids_dict[f"new_commodity_skid_number15"], new_skids_dict[f"new_commodity_skid_length15"],
                       new_skids_dict[f"new_commodity_skid_width15"], new_skids_dict[f"new_commodity_skid_height15"]]),
                  row([new_skids_dict[f"new_commodity_skid_number16"], new_skids_dict[f"new_commodity_skid_length16"],
                       new_skids_dict[f"new_commodity_skid_width16"], new_skids_dict[f"new_commodity_skid_height16"]]),
                  row([new_skids_dict[f"new_commodity_skid_number17"], new_skids_dict[f"new_commodity_skid_length17"],
                       new_skids_dict[f"new_commodity_skid_width17"], new_skids_dict[f"new_commodity_skid_height17"]]),
                  row([new_skids_dict[f"new_commodity_skid_number18"], new_skids_dict[f"new_commodity_skid_length18"],
                       new_skids_dict[f"new_commodity_skid_width18"], new_skids_dict[f"new_commodity_skid_height18"]]),
                  ]),
    title="New",
)

edit_pickup_del_layout = row([
                        column([
                            edit_div_pickup,
                            edit_pickup_strt_number,
                    edit_pickup_strt_name,
                    edit_pickup_unit_number,
                    edit_pickup_city,
                    edit_select_pickup_state,
                    edit_pickup_pc,
                    edit_pickup_date,
                    edit_pickup_shipper_name,
                    edit_pickup_shipper_contact,
                    edit_pickup_shipper_number,
                                ]),
                  edit_div_0,
                  column([
                  edit_div_del,
                  edit_del_strt_number,
                  edit_del_strt_name,
                  edit_del_unit_number,
                  edit_del_city,
                  edit_select_del_state,
                  edit_del_pc,
                  edit_del_date,
                  edit_del_consignee_name,
                  edit_del_consignee_contact,
                  edit_del_consignee_number,
                          ]),])

edit_del2_feature = column([edit_div_del2, edit_del2_strt_number,
                                 edit_del2_strt_name,
                                 edit_del2_unit_number,
                                 edit_del2_city,
                                 edit_select_del2_state,
                                 edit_del2_pc,
                                 edit_del2_date,
                            edit_del2_consignee_name,
                            edit_del2_consignee_contact,
                            edit_del2_consignee_number,
                            ])

edit_tab = TabPanel(
    child=column([row([edit_info_div,edit_select_kc_id, column([row([search_button, edit_button,edit_add_dest_button,]),
                                                                row([create_bol_button, create_invoice_button, create_loadconf_button])])]),
edit_display_div,
edit_pickup_del_layout,
edit_div_2,
edit_div_other,
row([
column([
edit_other_carrier,
edit_other_carrier_contact,
edit_other_date_invoiced,
edit_other_customer_invoice,
edit_other_carrier_invoice,
edit_other_tax_type,
edit_other_cost,
edit_other_invoice_total,
edit_other_tax,
        ])    ,
edit_div_1,
column([


    edit_other_charge,
    edit_other_profit,
    edit_other_date_ordered,
]),
]),
edit_other_special_notes,
edit_div_3,
edit_div_commodity,
edit_commodity_commodity,
edit_commodity_weight,
edit_commodity_notes,
row([skids_dict[f"edit_commodity_skid_number1"], skids_dict[f"edit_commodity_skid_length1"], skids_dict[f"edit_commodity_skid_width1"], skids_dict[f"edit_commodity_skid_height1"]]),
row([skids_dict[f"edit_commodity_skid_number2"], skids_dict[f"edit_commodity_skid_length2"], skids_dict[f"edit_commodity_skid_width2"], skids_dict[f"edit_commodity_skid_height2"]]),
row([skids_dict[f"edit_commodity_skid_number3"], skids_dict[f"edit_commodity_skid_length3"], skids_dict[f"edit_commodity_skid_width3"], skids_dict[f"edit_commodity_skid_height3"]]),
row([skids_dict[f"edit_commodity_skid_number4"], skids_dict[f"edit_commodity_skid_length4"], skids_dict[f"edit_commodity_skid_width4"], skids_dict[f"edit_commodity_skid_height4"]]),
row([skids_dict[f"edit_commodity_skid_number5"], skids_dict[f"edit_commodity_skid_length5"], skids_dict[f"edit_commodity_skid_width5"], skids_dict[f"edit_commodity_skid_height5"]]),
row([skids_dict[f"edit_commodity_skid_number6"], skids_dict[f"edit_commodity_skid_length6"], skids_dict[f"edit_commodity_skid_width6"], skids_dict[f"edit_commodity_skid_height6"]]),
row([skids_dict[f"edit_commodity_skid_number7"], skids_dict[f"edit_commodity_skid_length7"], skids_dict[f"edit_commodity_skid_width7"], skids_dict[f"edit_commodity_skid_height7"]]),
row([skids_dict[f"edit_commodity_skid_number8"], skids_dict[f"edit_commodity_skid_length8"], skids_dict[f"edit_commodity_skid_width8"], skids_dict[f"edit_commodity_skid_height8"]]),
row([skids_dict[f"edit_commodity_skid_number9"], skids_dict[f"edit_commodity_skid_length9"], skids_dict[f"edit_commodity_skid_width9"], skids_dict[f"edit_commodity_skid_height9"]]),
row([skids_dict[f"edit_commodity_skid_number10"], skids_dict[f"edit_commodity_skid_length10"], skids_dict[f"edit_commodity_skid_width10"], skids_dict[f"edit_commodity_skid_height10"]]),
row([skids_dict[f"edit_commodity_skid_number11"], skids_dict[f"edit_commodity_skid_length11"], skids_dict[f"edit_commodity_skid_width11"], skids_dict[f"edit_commodity_skid_height11"]]),
row([skids_dict[f"edit_commodity_skid_number12"], skids_dict[f"edit_commodity_skid_length12"], skids_dict[f"edit_commodity_skid_width12"], skids_dict[f"edit_commodity_skid_height12"]]),
row([skids_dict[f"edit_commodity_skid_number13"], skids_dict[f"edit_commodity_skid_length13"], skids_dict[f"edit_commodity_skid_width13"], skids_dict[f"edit_commodity_skid_height13"]]),
row([skids_dict[f"edit_commodity_skid_number14"], skids_dict[f"edit_commodity_skid_length14"], skids_dict[f"edit_commodity_skid_width14"], skids_dict[f"edit_commodity_skid_height14"]]),
row([skids_dict[f"edit_commodity_skid_number15"], skids_dict[f"edit_commodity_skid_length15"], skids_dict[f"edit_commodity_skid_width15"], skids_dict[f"edit_commodity_skid_height15"]]),
row([skids_dict[f"edit_commodity_skid_number16"], skids_dict[f"edit_commodity_skid_length16"], skids_dict[f"edit_commodity_skid_width16"], skids_dict[f"edit_commodity_skid_height16"]]),
row([skids_dict[f"edit_commodity_skid_number17"], skids_dict[f"edit_commodity_skid_length17"], skids_dict[f"edit_commodity_skid_width17"], skids_dict[f"edit_commodity_skid_height17"]]),
row([skids_dict[f"edit_commodity_skid_number18"], skids_dict[f"edit_commodity_skid_length18"], skids_dict[f"edit_commodity_skid_width18"], skids_dict[f"edit_commodity_skid_height18"]]),
]),
    title="Edit/View",
)

tt = Tabs(tabs=[edit_tab, new_tab])
dashboard = row([tt])
curdoc().add_root(dashboard)
show(dashboard)
