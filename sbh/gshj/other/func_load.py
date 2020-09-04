# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    func_load
   Description :
   Author :       CBH
   date：         2020/6/2 18: 00
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/2 18: 00:
-------------------------------------------------
"""
from sbh.gshj.util import account
import time
from datetime import datetime, date, timedelta
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y%m%d")
day_format_id = "'"+str(time.strftime("%Y%m%d", time.localtime()))+"'"
with account.PgSQLContextManager() as db_cursor:
    select_sql = """
      select his_bi."fun_dw_outp_fsjz"('{a}','{a}')
        """.format(a=yesterday)
    print(select_sql)
    # 执行SQL语句 返回影响的行数
    db_cursor.execute(select_sql)
    # 返回执行结果
    result = db_cursor.fetchall()
    print(result)




from sbh.gshj.util.Dict_date import *
from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.LogUitl import *
import datetime as dt
list_time=Get_Time_All(list_time=[])

for i in range(0,round(len(list_time)/2)+1):
    print(list_time[i])

for i in range(round(len(list_time)/2)+1,len(list_time)):
    print(list_time[i])

