# -*- coding: utf-8 -*-
# @File: Cx_oracle_connector.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/12  8:42

import cx_Oracle
conn = cx_Oracle.connect('his_bi/his_bi@192.168.10.154/orcl')
con = cx.connect('his_bi', 'his_bi', '192.168.10.154/orcl')
cursor = con.cursor()       #创建游标
cursor.execute("select * from TDER where ID='28'")  #执行sql语句
data = cursor.fetchone()        #获取一条数据
print(data)     #打印数据
cursor.close()  #关闭游标
con.close()     #关闭数据库连接






from sbh.gshj.util.Dict_date import *
from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.LogUitl import *
import datetime as dt
import pandas as pd
df = pd.read_csv(r'C:\Users\CBH\Desktop\bill_item.csv')
with PgSQLContextManager() as pg_cursor:
        file_path = r"C:\Users\CBH\Desktop\bill_item.csv"
        with open(file_path, 'r', encoding='utf-8') as f:
            insert_sql = """COPY his_bi.tmp_bms_bill_item FROM STDIN WITH (FORMAT CSV,DELIMITER ',',
escape '\t',
header true,
quote '"')"""
            pg_cursor.copy_expert(insert_sql, f)


