# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    code_trsform
   Description :
   Author :       CBH
   date：         2020/7/27 08: 59
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/27 08: 59:
-------------------------------------------------
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\CBH\Desktop\校核抗菌药物数据\azkaban_execution_logs.csv')

str(df['log'][1]).encode('utf-8')