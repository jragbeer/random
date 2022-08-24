import requests
import json
from typing import Optional
from pprint import pprint
import datetime
import pandas as pd
import numpy as np
from tqdm import tqdm

# basic functions
def submit_get_request(
    endpoint: str,
    session: Optional[requests.Session] = None,
) -> dict:
    """
    Generic function for get requests without any parameters, but with auth information.
    :param endpoint: API endpoint (URL + endpoint)
    :return: the result as a json / dictionary
    """
    if session:
        r = session.get(endpoint, )
    else:
        r = requests.get(endpoint,)
    return json.loads(r.text)
def get_latest_items(num_items = 1000):
    max_item = submit_get_request(max_item_url)
    array = []
    for num in tqdm(range(max_item-num_items-1, max_item+1)):
        array.append(submit_get_request(item_base_url + str(num) + ".json"))
    return pd.DataFrame(array).sort_values("id", ascending=False).reset_index()


base_url = "https://hacker-news.firebaseio.com/v0/"
user_base_url = base_url + "user/"
item_base_url = "https://hacker-news.firebaseio.com/v0/item/"
best_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
max_item_url = "https://hacker-news.firebaseio.com/v0/maxitem.json"
updates_url = "https://hacker-news.firebaseio.com/v0/updates.json?print=pretty"

df = get_latest_items(2000)
print(df.head(25).to_string())
print(len(df.index))

# pprint(submit_get_request(updates_url))
# pprint()
# # best_stories = submit_get_request(best_stories_url)
# # pprint(best_stories)
# # for x in best_stories[:3]:
# #     pprint(submit_get_request(item_base_url + str(x) + ".json"))
# it = submit_get_request(item_base_url + str(32581721) + ".json")
# it['human_time'] = datetime.datetime.utcfromtimestamp(it['time']).strftime('%Y-%m-%d %H:%M:%S')
# pprint(it)
#
# it = submit_get_request(item_base_url + str(32582588) + ".json")
# it['human_time'] = datetime.datetime.utcfromtimestamp(it['time']).strftime('%Y-%m-%d %H:%M:%S')
# pprint(it)
#
# us = submit_get_request(user_base_url + "twanvl" + ".json")
# us['created_human_time'] = datetime.datetime.utcfromtimestamp(us['created']).strftime('%Y-%m-%d %H:%M:%S')
# pprint(us)

