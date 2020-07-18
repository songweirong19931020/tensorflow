# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    dw_inp_paitent_info_m
   Description :
   Author :       CBH
   date：         2020/5/23 09: 46
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/23 09: 46:
-------------------------------------------------
"""
import psycopg2
import time
mon_id = "'"+str(time.strftime("%Y%m", time.localtime()))+"'"
conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres", database="postgres")
cur = conn.cursor()
sql = '''
select * from his_bi.dwd_inp_medical_d limit 10;
'''
cur.execute(sql)
#data = cur.fetchall()
conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
cur.close()
conn.close()