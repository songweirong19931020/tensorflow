# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    ver_sql
   Description :
   Author :       CBH
   date：         2020/6/15 10: 51
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/15 10: 51:
-------------------------------------------------
"""
from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.Time_Util  import *
import os,sys
with PgSQLContextManager() as db_cursor:
    mon_id = Get_Last_Month()
    ver_sql = '''
        select
        month_id,
        count(1)
        from
        his_bi.dw_inp_patient_info_m
        where
        month_id = '{mon_id}'
        GROUP BY
        month_id
        '''.format(mon_id=mon_id)
    db_cursor.execute(ver_sql)
    result = db_cursor.fetchall()