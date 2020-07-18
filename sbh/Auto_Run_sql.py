# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Auto_Run_sql
   Description :
   Author :       CBH
   date：         2020/6/30 16: 24
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/30 16: 24:
-------------------------------------------------
"""

from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.LogUitl import *


list_function = ['D00093', 'D00094', 'D00095', 'D00096', 'D00141', 'D00142', 'D00143', 'D00144']
list_time = ['20200101', '20200131', '20200201', '20200229', '20200301', '20200331', '20200401', '20200430',
             '20200501', '20200531', '20200601', '20200630']

def Run_Sql_Date(list_time,list_function):
    '''
    :param list_time: 时间列表
    :param list_function: 函数指标列表，格式：D00088
    :return:
    '''
    with PgSQLContextManager() as db_cursor:
        log = Logger('swr.log', logging.ERROR, logging.DEBUG)
        try:
            for t_time in range(len(list_time)):
                for i in range(len(list_function)):
                    sql = ''' select his_bi."fun_dwd_''' + str(list_function[i]) + '_d"' + '''('{}','{}') '''.format(
                        list_time[t_time],
                        list_time[
                            t_time + 1])
                    log.info(sql)
                    db_cursor.execute(sql)
        except:
            log.info("循环结束")
            print("循环结束")


def Run_Sql_Month(list_time,list_function):
    '''
    :param list_time: 时间列表 格式：'202001'
    :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
    :return: None
    '''
    with PgSQLContextManager() as db_cursor:
        log = Logger('swr.log', logging.ERROR, logging.DEBUG)
        try:
            for t_time in range(len(list_time)):
                for i in range(len(list_function)):
                    sql = ''' select ''' + str(list_function[i]) + '''('{}','{}') '''.format(
                        list_time[t_time],
                        list_time[
                            t_time + 1])
                    log.info(sql)
                    db_cursor.execute(sql)
        except:
            log.info("循环结束")
            print("循环结束")
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
from sbh.gshj.util.Dict_date import *
from sbh.gshj.util.account import PgSQLContextManager
from sbh.gshj.util.LogUitl import *
list_time=Get_Month_All(month_time=[])
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
for t_time in list_time:
    with PgSQLContextManager() as db_cursor:
        sql = ''' 
         select his_bi."fun_level_master_m"('{day_id}','{day_id}');
         '''.format(day_id = t_time)
        log.info("执行sql日期为：{}".format(t_time))
        log.info(sql)
        db_cursor.execute(sql)


'''
代替switch的方式推荐两种
1，字典 key,value的方式
2，lambda表达式方式result['a'](5)
'''
values = {
           '1': '星期一',
           '2': '星期二',
           '3': '星期三'
         }

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}


values_parm = {
    1: 'dim',
    2: 'dwd',
    3: 'dw_',
    4: 'ods',
    5: 'pts',
    6: 'bds',
    7: 'bms',
    8: 'dms',
    9: 'emr',
    10: 'v_d',
    11: 'ODS',
    12: 'uum',
    13: 'BMS',
    14: 'DIM',
    15: 'DWD',
         }
A=[]
B=[]
C=[]
aijs = {
    '1':lambda x: A.append(values_parm.get(1)) if x == values_parm.get(1) else None,
    '2':lambda x: values_parm.get(2) if x == values_parm.get(2) else None,
    '3':lambda x: values_parm.get(3) if x == values_parm.get(3) else None,


}

i = ['dwd_inp_medical_d', 'dim_date_info', 'dwd_inp_medical_d', 'dwd_inp_medical_d', 'ods_patient_opertion_info']
for gg in i:
    if aijs['1'](gg[0:3]) == None:
        continue
    print(aijs['1'](gg[0:3]))
for gg in i :
    if aijs['2'](gg[0:3]) == None:
        continue
    print(aijs['2'](gg[0:3]))

if i[0:3] == values_parm.get(1):
    list_new.append(values_result.get(1) + i)
    non_new.append(i)
    id_list.append(values_result.get(1))
elif i[0:3] == values_parm.get(2):
    list_new.append(values_result.get(2) + i)
    non_new.append(i)