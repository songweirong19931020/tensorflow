# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    dw_inp_info_m
   Description :
   Author :       CBH
   date：         2020/6/15 10: 49
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/15 10: 49:
-------------------------------------------------
"""
from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.Time_Util  import *
import os,sys
with PgSQLContextManager() as db_cursor:
    today = Get_Day()
    mon_id = Get_Last_Month()
    l_mon_id = Get_Last_2_Month()
    select_sql = """
    select his_bi."fun_dw_inp_patient_info_m"('{l_mon_id}','{mon_id}')
        """.format(mon_id=mon_id,l_mon_id=l_mon_id)
    db_cursor.execute(select_sql)
    ver_sql='''
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
job_name=os.path.basename(sys.argv[0]).replace('.py','')
if len(str(result[0][1]))>1:
    print('job_name:{},job_status:job-succsse,Job_executor_time:{},job-data_volume:{}'.format(job_name,today,
                                                                                              str(result[0][1])))
else:
    print('job_name:{},job_status:job-Failed,Job_executor_time:{},job-data_volume:{}'.format(job_name, today,
                                                                                              str(result[0][1])))