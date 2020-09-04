# -*- coding: utf-8 -*-
# @File: Test.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/8/27  15:43

import os
list_func = []

list_dir = os.listdir(r'C:\Users\CBH\Desktop\work_job\南通项目\function_job\20200825')
list_func_name = []
for i in list_dir:
    print(str(i).replace('.sql',''))
    list_func_name.append(str(i).replace('.sql',''))

n = 6
list_result = [list_func_name[i:i + n] for i in range(0, len(list_func_name), n)]



for i in list_result:
    print(i)
