# -*- coding: utf-8 -*-
# @File: FunctionAutoRunSql.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/26  16:25

from NTRMYY.util.account import PgSQLContextManager
from NTRMYY.util.Dict_date import *
from NTRMYY.util.LogUitl import *
import datetime as dt
import pandas as pd
import os,sys
from multiprocessing import Process
log = Logger('auto.log', logging.ERROR, logging.DEBUG)
def Run_Sql_Month(list_time,list_func_name):
    '''
    :param list_time: 时间列表 格式：'202001'
    :param list_function: 函数列表:"fun_dw_inp_drgs_patient_m"
    :return: None
    '''
    try:
        for f_name in list_func_name:
            for t_time in list_time:
                print(list_time.index(t_time))
                with PgSQLContextManager() as db_cursor:
                    start_time = dt.datetime.now()
                    sql = ''' select dwd."{f_name}"('{day_id}','{day_id}'); '''.format(day_id=t_time,f_name = f_name)
                    log.info("执行sql日期为：{}".format(t_time))
                    log.info(sql)
                    db_cursor.execute(sql)
                    end_date = dt.datetime.now()
                    log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')
    except:
        log.info("循环结束")


# 查询所有function_name
# with PgSQLContextManager() as db_cursor:
#     sql = '''
#       select
# --  substring(specific_name from '%#"fun_dwd_D_______#"%' FOR '#'),
#  substring(specific_name from '^.{16}'),
# routine_schema, ---数据库名
# specific_name, ----函数事件名
# routine_definition ---函数内容
# from information_schema.routines
# where
# routine_schema ='dwd'
# GROUP BY
# routine_schema, ---数据库名
# specific_name, ----函数事件名
# routine_definition
# having  substring(specific_name from '^.{9}') = 'fun_dwd_D'
#     '''
#     db_cursor.execute(sql)
#     result = db_cursor.fetchall()
#     df = pd.DataFrame(result)
#     df.columns=['result','a','b','c']
#     #存放函数名称的列表
#     list_function_name=[]
#     for row in df.itertuples(index=True, name='Pandas'):
#         print(getattr(row,'result'))
#         list_function_name.append(getattr(row,'result'))

# list_dir = os.listdir(r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200825')
# list_func_name = []
# for i in list_dir:
#     print(str(i).replace('.sql',''))
#     list_func_name.append(str(i).replace('.sql',''))

# Run_Sql_Month(list_time=list_time,list_function=list_func_name)

# for t_time in range(len(list_time)):
#     print(list_time.index(t_time))
#     for i in range(len(list_func_name)):
#         with PgSQLContextManager() as db_cursor:
#             start_time = dt.datetime.now()
#             sql = ''' select dwd."''' + list_func_name[i] + '''"('{day_id}','{day_id}') '''.format(
#                 day_id=list_time[t_time])
#             log.info("执行sql日期为：{}".format(t_time))
#             log.info(sql)
#             db_cursor.execute(sql)
#             end_date = dt.datetime.now()
#             log.info(f'执行完成时间为：{(end_date-start_time).seconds}s')


if __name__ == '__main__':
    # list_func1=['fun_dwd_DU1017_d',]
    # list_func2=[ 'fun_dwd_DU1011_d',]
    # list_func3=[ 'fun_dwd_DU1015_d']
    # # list_func4=['fun_dwd_DI0013_d',
    # # 'fun_dwd_DI0014_d','fun_dwd_DI2021_d']
    list_time = Get_Time_Qj_30(list_time=[])
    with PgSQLContextManager() as db_cursor:
        sql = '''
          select
    --  substring(specific_name from '%#"fun_dwd_D_______#"%' FOR '#'),
     substring(specific_name from '^.{16}'),
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition ---函数内容
    from information_schema.routines
    where
    routine_schema ='dwd'
    GROUP BY
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition
    having  substring(specific_name from '^.{9}') = 'fun_dwd_D'
        '''
        db_cursor.execute(sql)
        result = db_cursor.fetchall()
        df = pd.DataFrame(result)
        df.columns = ['result', 'a', 'b', 'c']
        # 存放函数名称的列表
        list_function_name = []
        for row in df.itertuples(index=True, name='Pandas'):
            print(getattr(row, 'result'))
            list_function_name.append(getattr(row, 'result'))
    # p1 = Process(target=Run_Sql_Month,args=(list_time,list_func1))
    # p2 = Process(target=Run_Sql_Month,args=(list_time,list_func2))
    # p3 = Process(target=Run_Sql_Month, args=(list_time, list_func3))
    # # p4 = Process(target=Run_Sql_Month, args=(list_time, list_func4))
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    #第二种优雅的写法
    # list_dir = os.listdir(r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200825')
    # list_func_name = []
    # for i in list_dir:
    #     print(str(i).replace('.sql', ''))
    #     list_func_name.append(str(i).replace('.sql', ''))

    # list_func_name=['fun_dwd_DI2003_d','fun_dwd_DI2004_d','fun_dwd_DI2009_d']
    n = 2
    list_result = [list_function_name[i:i + n] for i in range(0, len(list_function_name), n)]
    #
    # for i in list_result:
    #     print(i)
    p_lst = []
    for arg in list_result:
        print(arg)
        p = Process(target=Run_Sql_Month, args=(list_time,arg))
        p.start()
        p_lst.append(p)
