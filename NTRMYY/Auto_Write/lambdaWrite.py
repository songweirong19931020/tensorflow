# -*- coding: utf-8 -*-
# @File: lambdaWrite.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/25  13:52


#rep表达式处理sql的拼接
Rep = lambda x,y,z:str(x)+"(case when key='"+str(y)+"' then value else 0 end) as "+str(z)+','
import pandas as pd

df = pd.read_excel(r'C:\Users\CBH\Desktop\work_job\南通项目\split_sql.xlsx')

#itertuples循环遍历+getattr效率最好
for row in  df.itertuples(index=True, name='Pandas'):
    print(Rep(getattr(row,'A_type'),getattr(row,'condition_2'),getattr(row,'condition_4')))
