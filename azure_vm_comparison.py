import pandas as pd
import numpy as np
import lxml

url = "https://docs.microsoft.com/en-us/azure/virtual-machines/windows/compute-benchmark-scores"

dfs = []
for num, each in enumerate(pd.read_html(url)):
    if num == 0:
        print(each)
    else:
        dfs.append(each)

df = pd.concat(dfs).sort_values(["vCPUs",  "Avg Score"])
print(df.to_string())
