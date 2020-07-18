# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    transform_dict
   Description :
   Author :       CBH
   date：         2020/5/23 09: 24
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/23 09: 24:
-------------------------------------------------
"""
import pandas  as pd

df = pd.read_csv(r'C:\Users\CBH\Desktop\temp.csv',error_bad_lines=False,encoding='utf-8')
df = df['a'].str.split('\t',expand=True)
df.to_csv(r'C:\Users\CBH\Desktop\temp11.csv')