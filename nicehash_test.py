from nicehash import *

import os
rig_status_collection = mongodb['rig_status']

def build_basic_rig_stats_df():
    big = []
    for document in list(rig_status_collection.find({})):
        huh = []
        for kk in document['miningRigs']:
            cool = {'name':kk['name'], 'devices':{}}
            cool['devices']['device_name'] = [t['name'] for t in kk['devices'] if t['status']['description'] != 'Disabled']
            cool['devices']['power_usage'] = [t['powerUsage'] for t in kk['devices'] if t['powerUsage'] > 0]
            cool['devices']['speed'] = []
            for t in kk['devices']:
                try:
                    cool['devices']['speed'].append(t['speeds'][0]['speed'])
                except:
                    pass
            huh.append(cool)
        ww = pd.concat({x['name']:pd.DataFrame(x['devices']) for x in huh}).reset_index()
        ww.rename(columns = {'level_0': 'rig_name'}, inplace=True)
        ww.drop(columns=['level_1'], inplace=True)

        ww['device_id'] = (ww['rig_name'] + '_' + ww['device_name'].str.replace(' ', '_')).str.lower()
        for xx in ww.columns:
            try:
                ww[xx] = pd.to_numeric(ww[xx])
            except:
                pass
        # print(ww.to_string())
        ww['timestamp'] = pd.to_datetime(document['query_date'])
        big.append(ww)
    return pd.concat(big)


pprint(coinbase_sell_transactions())

# damn = build_basic_rig_stats_df()
# print(damn.to_string())
# for i in damn['rig_name'].unique():
#     aa = damn[damn['rig_name']==i].copy()
#     aa = aa.sort_values('timestamp', ascending=False,).set_index('timestamp')
#     bb = aa.resample('15min').mean()
#     bb['rig_name'] = i
#     print(bb)


