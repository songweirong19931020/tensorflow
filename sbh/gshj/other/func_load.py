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




