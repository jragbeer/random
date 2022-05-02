import os
import shutil
import pandas as pd
import datetime

today = datetime.datetime.now()
print(today)
path = "C:\\"

def get_size_path(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size
def get_size_tree(start_path = '.'):
    fun = []
    for dirpath, dnames, fnames in os.walk(start_path):
        stat = shutil.disk_usage(dirpath)
        try:
            zz = get_size_path(dirpath)
            fun.append({'path':dirpath, 'used_MB':zz/1024/1024, 'used_GB':zz/1024/1024/1024  })
        except:
            pass
    return pd.DataFrame(fun).drop_duplicates().sort_values('used', ascending=False).reset_index(drop=True)

df = get_size_tree(start_path = path)
print(df.head(100).to_string())
print(datetime.datetime.now()-today)
