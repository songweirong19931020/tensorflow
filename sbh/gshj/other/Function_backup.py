# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Function_backup
   Description :
   Author :       CBH
   date：         2020/6/12 10: 43
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/12 10: 43:
-------------------------------------------------
"""
from sbh.gshj.util.account import PgSQLContextManager
import pandas as pd
import os,sys
with PgSQLContextManager() as db_cursor:
    select_sql = '''
    select
routine_schema, ---数据库名
specific_name, ----函数事件名
routine_definition ---函数内容
from information_schema.routines
where 
routine_schema ='his_bi'
    '''
    db_cursor.execute(select_sql)
    # 返回执行结果
    result = db_cursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = ['base_name', 'func_name', 'detail']
    df.to_excel('{name}.xls'.format(name=os.path.basename(sys.argv[0]).replace('.py','')), index=False)