# -*- coding: utf-8 -*-
# @File: Auto_write_model.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/15  13:00
import pandas as pd
import sys
df = pd.read_excel(r'C:\Users\CBH\Desktop\work_job\南通项目\Auto_write_model.xlsx')
df = pd.DataFrame(df)
# resule = lambda x:"'"+x+"',"
key_total=[]
condition = []
remark = []
def auto_write_list():
    for code in df.values:
        key_total.append(code[0])
        print(code[1])
        condition.append(code[1])
        print(code[2])
        remark.append(code[2])
    return key_total,condition,remark



# print(getattr(sys.modules['__main__'],'df'))
#
# lst = [('吃饭',1),('睡觉',2)]
#
# for index,value in enumerate(lst):
#     print(index,value[0])

