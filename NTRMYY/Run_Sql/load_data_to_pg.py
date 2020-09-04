# -*- coding: utf-8 -*-
# @File: load_data_to_pg.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/19  9:14
import datetime as dt
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *
with PgSQLContextManager() as pg_cursor:
    print("清除重复数据delete from ods.his_emr_cp_variance_record")
    pg_cursor.execute("delete from ods.his_emr_cp_variance_record ;")
    file_path = r"C:\Users\CBH\Desktop\oracle\cp_variance_record.csv"
    with open(file_path, 'r', encoding='utf-8') as f:
        insert_sql = """COPY ods.his_emr_cp_variance_record FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
escape '\t',
header true,
quote '"')"""
        pg_cursor.copy_expert(insert_sql, f)

import os
li = os.listdir(r'C:\Users\CBH\Desktop\oracle\exam_reservation')
for i in li:
    # file_path = os.path.join(r"C:\Users\CBH\Desktop\oracle\exam_reservation", i)
    # print(file_path)
    print(i)
    with PgSQLContextManager() as pg_cursor:
        file_path = os.path.join(r"C:\Users\CBH\Desktop\oracle\exam_reservation",i)
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            insert_sql = """COPY ods.his_ers_exam_reservation FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
    escape '\t',
    header true,
    quote '"')"""
            pg_cursor.copy_expert(insert_sql, f)



