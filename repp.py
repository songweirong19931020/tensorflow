# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    repp
   Description :
   Author :       CBH
   date：         2020/5/28 16: 39
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/28 16: 39:
-------------------------------------------------
"""

import time
import datetime
import pandas as pd
df = pd.read_excel(r'C:\Users\CBH\Desktop\dt.xlsx')
dt = datetime.datetime.now()

dt.strftime('%Y-%m-%d %H:%M:%S')
print(datetime.datetime.now()+datetime.timedelta(minutes=15)).strftime("%H:%M")

for i in range(0,97):
    print("""update
    his_bi.dim_hour_min_secound
    set
    type = '{}'
    where
    time
    between
    '{}' and '{}';""".format(str(df['dt'][i])+'-'+str(df['dt'][i+1]),df['dt'][i],df['dt'][i+1]))


df['dt'][1]