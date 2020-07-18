# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    load_func
   Description :
   Author :       CBH
   date：         2020/5/12 09: 09
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/12 09: 09:
-------------------------------------------------
"""
import psycopg2
import time
import pandas as pd
month_format_id = "'" + str(time.strftime("%Y%m", time.localtime())) + "'"
conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres", database="postgres")
cur = conn.cursor()
sql = """
select
routine_schema, ---数据库名
specific_name, ----函数事件名
routine_definition ---函数内容
from information_schema.routines
where 
routine_schema ='his_bi'
"""


cur.execute(sql)
data = cur.fetchall()

#读取数据到df
df = pd.DataFrame(data)
df.columns=['base_name','func_name','detail']
df.to_excel(r'C:\Users\CBH\Desktop\work_job\function20200522.xls',index=False)

conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
cur.close()
conn.close()