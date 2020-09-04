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

from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *


list_function = ['D00025',
'D00029',
'D00030',
'D00031',
'D00032',
'D00033',
'D00034',
'D00036',
'D00039',
'D00088',
'D00089',
'D00090',
'D00091',
'D00093',
'D00094',
'D00095',
'D00096',
'D00141',
'D00142',
'D00143',
'D00144',
'D05011',
'D05015',
'D05016',
'D05017',
]
list_time = ['20200101', '20200131', '20200201', '20200229', '20200301', '20200331', '{f_time}', '20200430',
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
from sbh.gshj.util.Dict_date import *
list_time=Get_Time_All(list_time=[])
Run_Sql_Date(list_time,list_function)

for t_time in range(len(list_time)):
    print(t_time)
for func in list_function:
    for time_list in list_time:
        with PgSQLContextManager() as db_cursor:
            sql = ''' select his_bi."fun_dwd_''' + str(func) + '_d"' + '''('{day_id}','{day_id}') '''\
                .format(day_id=time_list)
            print(sql)
            db_cursor.execute(sql)




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
# .strftime('%Y:%m:%d %H:%M:%S')
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
import datetime as dt
from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.LogUitl import *
import os
list_time=Get_Time_All(list_time=[])
list_time = Get_Month_All(month_time=[])
list_function=['fun_dwd_DU1017_d'
]

list_dir = os.listdir(r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200818')
list_func_name = []
for i in list_dir:
    print(str(i).replace('.sql',''))
    list_func_name.append(str(i).replace('.sql',''))


list_func_name=['fun_dw_outp_patient_info_m']
list_time = ['20200701',
'20200702',
'20200703',
'20200704',
'20200705',
'20200706',
'20200707',
'20200708',
'20200709',
'20200710',
'20200711',
'20200712',
'20200713',
'20200714',
'20200715',
'20200716',
'20200717',
'20200718',
'20200719',
'20200720',
'20200721',
'20200722',
'20200723',
'20200724',
'20200725',
'20200726',
'20200727',
'20200728',
'20200729',
'20200730',
'20200731',
]
log = Logger('auto.log', logging.ERROR, logging.DEBUG)

for f_name in list_func_name:
    for t_time in list_time:
        print(list_time.index(t_time))
        with PgSQLContextManager() as db_cursor:
            start_time = dt.datetime.now()
            sql = ''' 
             select dw."{f_name}"('{day_id}','{day_id}');
             '''.format(day_id=t_time,f_name = f_name)
            log.info("执行sql日期为：{}".format(t_time))
            log.info(sql)
            db_cursor.execute(sql)
            end_date = dt.datetime.now()
            log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')

for t_time in list_time:
    print(list_time.index(t_time))
    with PgSQLContextManager() as db_cursor:
        start_time = dt.datetime.now()
        sql = ''' 
         select dw."fun_dw_inp_patient_info_m"('{day_id}','{day_id}');
         '''.format(day_id = t_time)
        log.info("执行sql日期为：{}".format(t_time))
        log.info(sql)
        db_cursor.execute(sql)
        end_date = dt.datetime.now()
        log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')
    # print(list_time.index(t_time))
    # with PgSQLContextManager() as db_cursor:
    #     start_time = dt.datetime.now()
    #     sql = '''
    #      select his_bi."{function_nam}"('{day_id}','{day_id}');
    #      '''.format(day_id = t_time,function_nam = list_function[t_time])
    #     log.info("执行sql日期为：{}".format(t_time))
    #     log.info(sql)
    #     db_cursor.execute(sql)
    #     end_date = dt.datetime.now()
    #     log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')


list_func_time= ['202001','202002','202003','202004','202005','202006','202007']
list_func_time=['20200401','20200402']
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
for f_time in list_func_time:
    print(f_time)
    with PgSQLContextManager() as db_cursor:
        start_time = dt.datetime.now()
        sql = '''select his_bi."fun_dwd_D00200_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00201_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00202_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00203_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00204_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00205_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00206_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00207_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00208_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00209_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00210_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00215_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00216_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00217_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00218_d"('{f_time}', '{f_time}');
select his_bi."fun_dwd_D00219_d"('{f_time}', '{f_time}');
        '''.format(f_time=f_time)
        db_cursor.execute(sql)
        end_date = dt.datetime.now()
        log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')


for i in range(0,20):
    # print('D00'+str(i+200))
    print('select his_bi."fun_dwd_'+'D00'+str(i+200)+'_d'+'''"('{f_time}', '{f_time}');''')



import time
tupTime = time.localtime( 1597005380)#秒时间戳
stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
print(stadardTime)

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

list = [1,2]
import pandas as pd
df = pd.DataFrame(list)
df = pd.DataFrame()
try:
    if df.empty == True:
        print('successd!')
    else:
        1/0
except:
    raise ValueError('为处理ODS任务失败，而抛出异常！')