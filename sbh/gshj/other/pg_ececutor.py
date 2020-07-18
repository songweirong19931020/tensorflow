# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    pg_ececutor
   Description :
   Author :       CBH
   date：         2020/6/12 09: 15
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/12 09: 15:
-------------------------------------------------
"""
from sbh.gshj.util.account import PgSQLContextManager

with PgSQLContextManager() as db_cursor:
    month=202003
    for i in range(0,4):
        m = month+i
        select_sql = '''select his_bi."fun_dw_outp_patient_info_m"('{month}', '{month}')'''.format(month=m)
        print(select_sql)
        db_cursor.execute(select_sql)
        print(month+i)
