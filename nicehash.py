import datetime
from time import mktime
import uuid
import hmac
import requests
import json
from hashlib import sha256
import optparse
import sys
import os
import pytz
from pprint import pprint
import pandas as pd
import numpy as np
import sqlite3
import logging
import pymongo

class nh_public_api:

    def __init__(self, host, verbose=False):
        self.host = host
        self.verbose = verbose

    def request(self, method, path, query, body):
        url = self.host + path
        if query:
            url += '?' + query

        if self.verbose:
            print(method, url)

        s = requests.Session()
        if body:
            body_json = json.dumps(body)
            response = s.request(method, url, data=body_json)
        else:
            response = s.request(method, url)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_current_global_stats(self):
        return self.request('GET', '/main/api/v2/public/stats/global/current/', '', None)

    def get_global_stats_24(self):
        return self.request('GET', '/main/api/v2/public/stats/global/24h/', '', None)

    def get_active_orders(self):
        return self.request('GET', '/main/api/v2/public/orders/active/', '', None)

    def get_active_orders2(self):
        return self.request('GET', '/main/api/v2/public/orders/active2/', '', None)

    def buy_info(self):
        return self.request('GET', '/main/api/v2/public/buy/info/', '', None)

    def get_algorithms(self):
        return self.request('GET', '/main/api/v2/mining/algorithms/', '', None)

    def get_markets(self):
        return self.request('GET', '/main/api/v2/mining/markets/', '', None)

    def get_algo_history(self, algo):
        query = f"algorithm={algo}"
        return self.request('GET', '/main/api/v2/public/algo/history', query, None)

    def get_currencies(self):
        return self.request('GET', '/main/api/v2/public/currencies/', '', None)

    def get_multialgo_info(self):
        return self.request('GET', '/main/api/v2/public/simplemultialgo/info/', '', None)

    def get_exchange_markets_info(self):
        return self.request('GET', '/exchange/api/v2/info/status', '', None)

    def get_exchange_trades(self, market):
        return self.request('GET', '/exchange/api/v2/trades', 'market=' + market, None)

    def get_candlesticks(self, market, from_s, to_s, resolution):
        return self.request('GET', '/exchange/api/v2/candlesticks', "market={}&from={}&to={}&resolution={}".format(market, from_s, to_s, resolution), None)

    def get_exchange_orderbook(self, market, limit):
        return self.request('GET', '/exchange/api/v2/orderbook', "market={}&limit={}".format(market, limit), None)
class nh_private_api:

    def __init__(self, host, organisation_id, key, secret, verbose=False):
        self.key = key
        self.secret = secret
        self.organisation_id = organisation_id
        self.host = host
        self.verbose = verbose

    def request(self, method, path, query, body):

        xtime = self.get_epoch_ms_from_now()
        xnonce = str(uuid.uuid4())

        message = bytearray(self.key, 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(str(xtime), 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(xnonce, 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(self.organisation_id, 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(method, 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(path, 'utf-8')
        message += bytearray('\x00', 'utf-8')
        message += bytearray(query, 'utf-8')

        if body:
            body_json = json.dumps(body)
            message += bytearray('\x00', 'utf-8')
            message += bytearray(body_json, 'utf-8')

        digest = hmac.new(bytearray(self.secret, 'utf-8'), message, sha256).hexdigest()
        xauth = self.key + ":" + digest

        headers = {
            'X-Time': str(xtime),
            'X-Nonce': xnonce,
            'X-Auth': xauth,
            'Content-Type': 'application/json',
            'X-Organization-Id': self.organisation_id,
            'X-Request-Id': str(uuid.uuid4())
        }

        s = requests.Session()
        s.headers = headers

        url = self.host + path
        if query:
            url += '?' + query

        if self.verbose:
            print(method, url)

        if body:
            response = s.request(method, url, data=body_json)
        else:
            response = s.request(method, url)

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def get_epoch_ms_from_now(self):
        now = datetime.datetime.now()
        now_ec_since_epoch = mktime(now.timetuple()) + now.microsecond / 1000000.0
        return int(now_ec_since_epoch * 1000)

    def algo_settings_from_response(self, algorithm, algo_response):
        algo_setting = None
        for item in algo_response['miningAlgorithms']:
            if item['algorithm'] == algorithm:
                algo_setting = item

        if algo_setting is None:
            raise Exception('Settings for algorithm not found in algo_response parameter')

        return algo_setting

    def get_accounts(self):
        return self.request('GET', '/main/api/v2/accounting/accounts2/', '', None)

    def get_accounts_for_currency(self, currency):
        return self.request('GET', '/main/api/v2/accounting/account2/' + currency, '', None)

    def get_withdrawal_addresses(self, currency, size, page):

        params = "currency={}&size={}&page={}".format(currency, size, page)

        return self.request('GET', '/main/api/v2/accounting/withdrawalAddresses/', params, None)

    def get_withdrawal_types(self):
        return self.request('GET', '/main/api/v2/accounting/withdrawalAddresses/types/', '', None)

    def withdraw_request(self, address_id, amount, currency):
        withdraw_data = {
            "withdrawalAddressId": address_id,
            "amount": amount,
            "currency": currency
        }
        return self.request('POST', '/main/api/v2/accounting/withdrawal/', '', withdraw_data)

    def get_my_active_orders(self, algorithm, market, limit):

        ts = self.get_epoch_ms_from_now()
        params = "algorithm={}&market={}&ts={}&limit={}&op=LT".format(algorithm, market, ts, limit)

        return self.request('GET', '/main/api/v2/hashpower/myOrders', params, None)

    def create_pool(self, name, algorithm, pool_host, pool_port, username, password):
        pool_data = {
            "name": name,
            "algorithm": algorithm,
            "stratumHostname": pool_host,
            "stratumPort": pool_port,
            "username": username,
            "password": password
        }
        return self.request('POST', '/main/api/v2/pool/', '', pool_data)

    def delete_pool(self, pool_id):
        return self.request('DELETE', '/main/api/v2/pool/' + pool_id, '', None)

    def get_my_pools(self, page, size):
        return self.request('GET', '/main/api/v2/pools/', '', None)

    def get_hashpower_orderbook(self, algorithm):
        return self.request('GET', '/main/api/v2/hashpower/orderBook/', 'algorithm=' + algorithm, None)

    def create_hashpower_order(self, market, type, algorithm, price, limit, amount, pool_id, algo_response):

        algo_setting = self.algo_settings_from_response(algorithm, algo_response)

        order_data = {
            "market": market,
            "algorithm": algorithm,
            "amount": amount,
            "price": price,
            "limit": limit,
            "poolId": pool_id,
            "type": type,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return self.request('POST', '/main/api/v2/hashpower/order/', '', order_data)

    def cancel_hashpower_order(self, order_id):
        return self.request('DELETE', '/main/api/v2/hashpower/order/' + order_id, '', None)

    def refill_hashpower_order(self, order_id, amount):
        refill_data = {
            "amount": amount
        }
        return self.request('POST', '/main/api/v2/hashpower/order/' + order_id + '/refill/', '', refill_data)

    def set_price_hashpower_order(self, order_id, price, algorithm, algo_response):

        algo_setting = self.algo_settings_from_response(algorithm, algo_response)

        price_data = {
            "price": price,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return self.request('POST', '/main/api/v2/hashpower/order/' + order_id + '/updatePriceAndLimit/', '',
                            price_data)

    def set_limit_hashpower_order(self, order_id, limit, algorithm, algo_response):
        algo_setting = self.algo_settings_from_response(algorithm, algo_response)
        limit_data = {
            "limit": limit,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return self.request('POST', '/main/api/v2/hashpower/order/' + order_id + '/updatePriceAndLimit/', '',
                            limit_data)

    def set_price_and_limit_hashpower_order(self, order_id, price, limit, algorithm, algo_response):
        algo_setting = self.algo_settings_from_response(algorithm, algo_response)

        price_data = {
            "price": price,
            "limit": limit,
            "marketFactor": algo_setting['marketFactor'],
            "displayMarketFactor": algo_setting['displayMarketFactor']
        }
        return self.request('POST', '/main/api/v2/hashpower/order/' + order_id + '/updatePriceAndLimit/', '',
                            price_data)

    def get_my_exchange_orders(self, market):
        return self.request('GET', '/exchange/api/v2/myOrders', 'market=' + market, None)

    def get_my_exchange_trades(self, market):
        return self.request('GET', '/exchange/api/v2/myTrades', 'market=' + market, None)

    def create_exchange_limit_order(self, market, side, quantity, price):
        query = "market={}&side={}&type=limit&quantity={}&price={}".format(market, side, quantity, price)
        return self.request('POST', '/exchange/api/v2/order', query, None)

    def create_exchange_buy_market_order(self, market, quantity):
        query = "market={}&side=buy&type=market&secQuantity={}".format(market, quantity)
        return self.request('POST', '/exchange/api/v2/order', query, None)

    def create_exchange_sell_market_order(self, market, quantity):
        query = "market={}&side=sell&type=market&quantity={}".format(market, quantity)
        return self.request('POST', '/exchange/api/v2/order', query, None)

    def cancel_exchange_order(self, market, order_id):
        query = "market={}&orderId={}".format(market, order_id)
        return self.request('DELETE', '/exchange/api/v2/order', query, None)

    def payout_call(self, size=5000, page=1):
        #1616987181
        #255135600000000
        query = f"beforeTimestamp=255135600000000&size={size}&page={page}"
        return self.request('GET', f"/main/api/v2/mining/rigs/payouts",query, None)

    def miner_stats(self, algo=20, prev=True):
        #1616987181
        #255135600000000
        if prev:
            query = f"algorithm={algo}&afterTimestamp=1616951999000&beforeTimestamp=1617928500000"
        else:
            query = f"algorithm={algo}"
        return self.request('GET', f"/main/api/v2/mining/rigs/stats/algo",query, None)

    def rig_status_overview(self, size=5000, page=1,):
        #1616987181
        #255135600000000
        query = f"size={size}&page={page}"
        return self.request('GET', f"/main/api/v2/mining/rigs2",query, None)

    def active_workers(self,):
        return self.request('GET', f"/main/api/v2/mining/rigs/activeWorkers",'', None)

    def rig_status(self,):
        return self.request('GET', f"/main/api/v2/mining/rigs2",'', None)

def convert_unix_timestamp_to_pandas_date(input_date):
    return pd.to_datetime(datetime.datetime.fromtimestamp(int(input_date)/1000),)

def get_payout_data():
    df = pd.DataFrame(private_api.payout_call()["list"])
    df.rename(columns={'amount':'gross_amount', 'feeAmount': 'nh_fee', }, inplace=True)
    df["currency"] = df["currency"].astype(str)
    df["currency"] = df["currency"].replace("{'enumName': 'BTC', 'description': 'BTC'}", "BTC", )
    df.drop(columns = ['metadata', 'accountType'], inplace=True)
    df['nh_fee'] = pd.to_numeric(df['nh_fee']).astype(np.float32)
    df['gross_amount'] = pd.to_numeric(df['gross_amount']).astype(np.float32)
    df['net_amount'] = df['gross_amount'] - df['nh_fee']
    df['created_datetime'] = [convert_unix_timestamp_to_pandas_date(i) for i in df['created']]
    df['timestamp'] = df['created_datetime'].dt.round('H')
    df = df.sort_values('timestamp', ascending=True,) # sort by time
    df['net_amount_cumsum'] = df['net_amount'].cumsum() # total bitcoin recieved
    return df
def miner_statistics():
    rr = private_api.miner_stats()
    kdf = pd.DataFrame(rr['data'], columns=rr['columns'])

    rr = private_api.miner_stats(prev=False)
    pdf = pd.DataFrame(rr['data'], columns=rr['columns'])

    idf = pd.concat([pdf, kdf])

    idf['time_datetime'] = [convert_unix_timestamp_to_pandas_date(i) for i in idf['time']]
    idf = idf.sort_values('time_datetime')
    idf['rejected']=idf['speed_rejected_target']+idf['speed_rejected_stale']+idf['speed_rejected_duplicate']+idf['speed_rejected_ntime']+idf['speed_rejected_other']
    idf['diff'] = idf['speed_accepted'] - idf['rejected']
    idf.drop_duplicates(inplace=True)
    return idf
def get_active_workers_stats():
    rr = private_api.active_workers()
    for each in rr['workers']:
        each['algorithm'] = each['algorithm']['description']
    return pd.DataFrame(rr['workers'])
def algo_history():
    for i in all_algos:
        a = public_api.get_algo_history(i)
        idf = pd.DataFrame(a)
        idf.columns = ['timestamp', 'speed', 'price']
        idf['datetime'] = [convert_unix_timestamp_to_pandas_date(x) for x in idf['timestamp']]
        print(idf)

def get_miner_stats_df(sql_table_info):
    ok = []
    for i in sql_table_info[sql_table_info['table_cat'] == 'miner_stats']['table_name']:
        ok.append(pd.read_sql(f"select * from {i}", sql_engine))
    idf = pd.concat(ok).drop_duplicates()
    idf['time_datetime'] = pd.to_datetime(idf['time_datetime'])
    idf.sort_values('time_datetime', ascending=False, inplace=True)
    # idf=idf.drop_duplicates(subset=['time_datetime',])
    return idf
def get_payout_data_df(sql_table_info):
    ok = []
    for i in sql_table_info[sql_table_info['table_cat'] == 'payout_data']['table_name']:
        ok.append(pd.read_sql(f"select * from {i}", sql_engine))
    idf = pd.concat(ok).drop_duplicates()
    idf['timestamp'] = pd.to_datetime(idf['timestamp'])
    idf['created_datetime'] = pd.to_datetime(idf['created_datetime'])
    idf.sort_values('created_datetime', ascending=True, inplace=True)
    idf=idf.drop_duplicates(subset=['id', 'created'])
    return idf

def create_new_db_with_table_name_changes(eng1, eng2):
    cur = eng1.cursor()
    result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table_names = sorted([i[0] for i in result])
    for ii, name in enumerate(table_names):
        ddf = pd.read_sql(f'select * from {name}', eng1)
        if '__' in name:
            ddf.to_sql(name, eng2, if_exists='replace', index=False)
        else:
            name1 = '_'.join(name.split('_')[:2])
            name2 = '_'.join(name.split('_')[2:])
            ddf.to_sql(name1+'__'+name2, eng2, if_exists='replace', index=False)
def get_names_of_latest_tables(eng1):
    cur = eng1.cursor()
    result = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table = pd.DataFrame({'table_name':[i[0] for i in result]})
    table['table_cat'] = table['table_name'].str.split('__').str.get(0)
    table['query_date'] = table['table_name'].str.split('__').str.get(1).str.split('_')
    table_append = pd.DataFrame(table['query_date'].to_list(), columns=['year', 'month', 'day', 'hour', 'minute'])
    for each in table_append.columns:
        table_append[each] = pd.to_numeric(table_append[each])
    new_table = pd.concat([table, table_append], axis=1)
    new_table['query_date'] = pd.to_datetime(new_table[['year', 'month', 'day', 'hour', "minute"]])
    return new_table
def get_newest_tables(sql_table_info):
    tmp_dict = {}
    for each in sql_table_info['table_cat'].unique():
        tmp_dict[each] = {}
        tmp_dict[each]['mrt'] = sql_table_info[sql_table_info['table_cat'] == each].sort_values('query_date', ascending=False)['table_name'].iloc[0] # most recent table
    return tmp_dict

def get_data_5mins():
    cur_time = datetime.datetime.now()
    engine = sqlite3.connect(data_path + "nicehash_data.db")
    miner_stats_df = miner_statistics()
    miner_stats_df.to_sql(f"miner_stats__{cur_time.strftime('%Y_%m_%d_%H_%M')}", engine, if_exists='replace', index=False,)
    logging.info(f"Miner Stats table added {cur_time}")
    active_workers = get_active_workers_stats()
    active_workers.to_sql(f"active_workers__{cur_time.strftime('%Y_%m_%d_%H_%M')}", engine, if_exists='replace', index=False)
    logging.info(f"Active Workers table added {cur_time}")
    rig_status_collection = mongodb['rig_status']
    rgsttus = private_api.rig_status()
    mongo_result1 = rig_status_collection.insert_one({'query_date': f'{cur_time}', **rgsttus})
    logging.info(f'Rig Status Data for {cur_time} in MongoDB, id: {mongo_result1.inserted_id}')
    logging.info(f"Private Data Pull done!")
def get_data_4hr():
    cur_time = datetime.datetime.now()
    engine = sqlite3.connect(data_path + "nicehash_data.db")
    payout_data = get_payout_data()
    payout_data.to_sql(f"payout_data__{cur_time.strftime('%Y_%m_%d_%H_%M')}", engine, if_exists='replace', index=False)
    logging.info(f"Payout Data table added {cur_time}")
    logging.info(f"1-hr Data Pull done!")
def get_data_1hr():
    cur_time = datetime.datetime.now()
    rig_overview_collection = mongodb['rig_status_overview']
    rig_overview = private_api.rig_status_overview()
    mongo_result2 = rig_overview_collection.insert_one({'query_date': f'{cur_time}', **rig_overview})
    logging.info(f'Rig Status Overview Data for {cur_time} in MongoDB, id: {mongo_result2.inserted_id}')
    logging.info(f"1-hr Data Pull done!")


def get_public_data_long_term():
    cur_time = datetime.datetime.now()
    engine = sqlite3.connect(data_path + "nicehash_data.db")
    algos = public_api.get_algorithms()
    algos_df = pd.DataFrame(algos['miningAlgorithms'])
    algos_df.to_sql(f"mining_algorithms__{cur_time.strftime('%Y_%m_%d_%H_%M')}", engine, if_exists='replace', index=False)
    logging.info(f"Mining Algorithm table added {cur_time}")
    logging.info(f"Public Data Long Term Pull done!")

path = os.getcwd().replace("\\", "/")+ "/"
data_path = path + 'data/'

api_creds = {}
with open(data_path + 'nicehash_api_key.txt', 'r') as file:
    for line in file:
        k = line.split(' = ')[0]
        v = line.split(' = ')[1].rstrip('\n')
        api_creds[k] = v

all_algos = [ "SCRYPT", "SHA256", "SCRYPTNF", "X11", "X13", "KECCAK", "X15", "NIST5", "NEOSCRYPT", "LYRA2RE", "WHIRLPOOLX", "QUBIT", "QUARK", "AXIOM", "LYRA2REV2", "SCRYPTJANENF16", "BLAKE256R8", "BLAKE256R14", "BLAKE256R8VNL", "HODL", "DAGGERHASHIMOTO", "DECRED", "CRYPTONIGHT", "LBRY", "EQUIHASH", "PASCAL", "X11GOST", "SIA", "BLAKE2S", "SKUNK", "CRYPTONIGHTV7", "CRYPTONIGHTHEAVY", "LYRA2Z", "X16R", "CRYPTONIGHTV8", "SHA256ASICBOOST", "ZHASH", "BEAM", "GRINCUCKAROO29", "GRINCUCKATOO31", "LYRA2REV3", "CRYPTONIGHTR", "CUCKOOCYCLE", "GRINCUCKAROOD29", "BEAMV2", "X16RV2", "RANDOMXMONERO", "EAGLESONG", "CUCKAROOM", "GRINCUCKATOO32", "HANDSHAKE", "KAWPOW", "CUCKAROO29BFC", "BEAMV3", "CUCKAROOZ29", "OCTOPUS" ]
# SQL DB (SQLITE3)
sql_engine = sqlite3.connect(data_path + "nicehash_data.db")

# MONGODB DATABASE
mongo_client = pymongo.MongoClient('localhost', 27017)
mongodb = mongo_client['Nicehash']

public_api = nh_public_api(api_creds['host'], )
private_api = nh_private_api(api_creds['host'], api_creds["organisation_id"], api_creds["key"], api_creds["secret"])
