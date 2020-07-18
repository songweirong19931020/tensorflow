# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    temp
   Description :
   Author :       CBH
   date：         2020/5/23 15: 07
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/23 15: 07:
-------------------------------------------------
"""
from sbh.gshj.util import account
import pandas as pd

with account.PgSQLContextManager() as db_cursor:
    select_sql = """select
    routine_schema, ---数据库名
    specific_name, ----函数事件名
    routine_definition ---函数内容
    from information_schema.routines
    where 
    routine_schema ='his_bi'
    and routine_definition like '%D002%%'
    """
    # 执行SQL语句 返回影响的行数
    db_cursor.execute(select_sql)
    # 返回执行结果
    result = db_cursor.fetchall()
    print(result)
    df = pd.DataFrame(result)
    df.to_excel('demo_func.xls')
    d1 = pd.read_excel(r'demo_func.xls')

    df1 = d1[2].str.split('\n', expand=True)
    df1.to_excel('demo_func1.xls')