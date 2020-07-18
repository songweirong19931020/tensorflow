# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    path_load_auto_write
   Description :
   Author :       CBH
   date：         2020/6/15 11: 10
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/15 11: 10:
-------------------------------------------------
"""
import os,sys

log_title='''

#coding=utf-8
from util.Acount_205 import PgSQLContextManager
from util.Time_Util import *
import os,sys
with PgSQLContextManager() as db_cursor:
    today = Get_Day()
    yesterday = Get_Yesterday()
    first_1= Get_Last_2_Month_id()
    select_sql = {sql}
    db_cursor.execute(select_sql)
'''.format(sql=sql)
#门诊
for num in range(4):
    num_i =248+num
    log1="""fun_dwd_D"""+'00'+str(num_i)+"""_d"""
    print(log1)
    select_sql_1 = """select his_bi.""" + '"' + log1 + '"'
    select_sql_2 = '''('{day_15}','{yesterday}');'''
    select_sql = '"""'+ select_sql_1 + select_sql_2 +'"""' + '.format(yesterday=yesterday,day_15 = day_15)'
    # print(select_sql)
    log_title = '''#coding=utf-8
from util.Acount_205 import PgSQLContextManager
from util.Time_Util import *
import os,sys
with PgSQLContextManager() as db_cursor:
    today = Get_Day()
    yesterday = Get_Yesterday()
    day_15 = Get_Last_Day_15()
    select_sql = {sql}
    db_cursor.execute(select_sql)
    '''.format(sql=select_sql)
    log_title = log_title + '''\njob_name=os.path.basename(sys.argv[0]).replace('.py','')
print('job_name:{},job_status:job-succsse,Job_executor_time:{}'.format(job_name,today))'''
    print(log_title)
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job'
    path2 =  'pg_d_'+str(num_i)+'_sql'+'.py'
    path = os.path.join(path1,path2)
    f = open(path, 'a')
    f.write(log_title)
    f.close()

#住院
for num in range(70):
    num_i =130+num
    log1="""fun_dwd_D"""+'00'+str(num_i)+"""_d"""
    print(log1)
    select_sql_1 = """select his_bi.""" + '"' + log1 + '"'
    select_sql_2 = '''('{day_id}','{day_id}');'''
    select_sql = '"""'+ select_sql_1 + select_sql_2 +'"""' + '.format(day_id=i)'
    # print(select_sql)
    log_title = '''#coding=utf-8
from util.Acount_205 import PgSQLContextManager
from util.Time_Util import *
import os,sys
list_day = Get_Time_Qj_30()
for i in list_day:
    with PgSQLContextManager() as db_cursor:
        select_sql = {sql}
        db_cursor.execute(select_sql)
        print("执行任务时间为:"+str(i))'''.format(sql=select_sql)
    log_title = log_title + '''\njob_name=os.path.basename(sys.argv[0]).replace('.py','')
print('job_name:{},job_status:job-succsse,Job_executor_time:{}'.format(job_name,today))'''
    print(log_title)
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job'
    path2 =  'pg_d_'+str(num_i)+'_sql'+'.py'
    path = os.path.join(path1,path2)
    f = open(path, 'a',encoding='utf-8')
    f.write(log_title)
    f.close()


#住院-新指标费用模块
for num in range(23):
    num_i =5000+num
    log1="""fun_dwd_D"""+'0'+str(num_i)+"""_d"""
    print(log1)
    select_sql_1 = """select his_bi.""" + '"' + log1 + '"'
    select_sql_2 = '''('{day_15}','{yesterday}');'''
    select_sql = '"""'+ select_sql_1 + select_sql_2 +'"""' + '.format(yesterday=yesterday,day_15=day_15)'
    # print(select_sql)
    log_title = '''#coding=utf-8
from util.Acount_205 import PgSQLContextManager
from util.Time_Util import *
import os,sys
with PgSQLContextManager() as db_cursor:
    today = Get_Day()
    yesterday = Get_Yesterday()
    day_15 = Get_Last_Day_15()
    select_sql = {sql}
    db_cursor.execute(select_sql)
    '''.format(sql=select_sql)
    log_title = log_title + '''\njob_name=os.path.basename(sys.argv[0]).replace('.py','')
print('job_name:{},job_status:job-succsse,Job_executor_time:{}'.format(job_name,today))'''
    print(log_title)
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job'
    path2 =  'pg_d_'+str(num_i)+'_sql'+'.py'
    path = os.path.join(path1,path2)
    f = open(path, 'a')
    f.write(log_title)
    f.close()






#获取flow名称
list_job_name = []
for i in os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job\name'):
    print(i.replace('.job',''))
    list_job_name.append(i.replace('.job',''))



###获取文件jobname---dwd
for i in os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job'):
    print(i)
    logjob1 = 'type=command\ncommand=python3 '
    logjob2 = "'" + str(i)+ "'"
    logjob = logjob1 +logjob2
    print(logjob)
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job'
    path2 = i.replace('_sql.py','')
    path = os.path.join(path1, path2)
    print(path)
    f = open(path+'.job', 'a')
    f.write(logjob)
    f.close()

###获取文件jobname---dw
for i in os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job\DW'):
    # print(i)
    logjob1 = 'type=command\ncommand=python3 '
    logjob2 = "'" + str(i)+ "'"
    logjob = logjob1 +logjob2
    # print(logjob)
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job\DW'
    path2 = i.replace('.py','')
    print(path2)
    path = os.path.join(path1, path2)
    print(path)
    f = open(path+'.job', 'a')
    f.write(logjob)
    f.close()

def replace_text(sql_text):
    with open(sql_text, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(sql_text, "w", encoding="utf-8") as f_w:
        for line in lines:
            if "Acount_205" in line:
                line = line.replace(line, "Acount_203")
            f_w.write(line)

#更改sql文件节点
for name_sql in os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job\newsql'):
    portion = os.path.splitext(name_sql)
    path = r'C:\Users\CBH\Desktop\azkaban\正式环境job\newsql'
    path1 = r'C:\Users\CBH\Desktop\azkaban\正式环境job\newjob'
    print(portion)
    if portion[1] == ".py":
        new_name = portion[0] + ".txt"
        print(new_name)
        os.rename(os.path.join(path,name_sql), os.path.join(path1,new_name))


import re
import os

files = os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job\newjob')

def replaceStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        str1 = re.sub('retry.backoff=1800000', 'retry.backoff=3600000', str)
        with open(file,'w', encoding='utf-8') as f:
            f.write(str1)

def addStr(file):
    with open(file, 'r', encoding='utf-8') as f:
        str = f.read()
        print(str)
        # str1 = re.sub('Get_Last_2_Month_id()', 'Get_Last_Day_30', str)
        with open(file,'a+', encoding='utf-8') as f:
            str1 = '\nretries=1\nretry.backoff=1800000'
            f.write(str1)


print(files)
for f in files:
    replaceStr("C:\\Users\\CBH\Desktop\\azkaban\\正式环境job\\newjob\\"+f)




import pandas  as pd

df = pd.read_csv(r'C:\Users\CBH\Desktop\20200711.log',header=None)
df_list = pd.DataFrame(df)
list_result = []
for ii in df_list.index:
    if ii % 2==0:
        print('舍弃')
    else:
        list_result.append(df_list.loc[ii].values)
    print(ii)
    date_time = df_list.loc[ii].values
    print(date_time)

df1 = pd.DataFrame(list_result)
df_time=[]
df_path=[]
df_job=[]
df_h_m=[]
df_day=[]
for i in df1[0]:
    print(str(i).split(" ")[1] + ':' +str(i).split(" ")[0])
    df_day.append(str(i).split(" ")[2])
    df_h_m.append(str(i).split(" ")[1] + ':' +str(i).split(" ")[0])
    # print(str(i).split(" ")[5])
    # df_path.append(str(i).split(" ")[5])
    df_time.append( " ".join(str(i).split(" ")[0:5]))
    # df_job.append(str(i).split(" ")[6])

dlr = pd.DataFrame(df_time)
dlr['path'] = pd.DataFrame(df_path)
dlr['job']=pd.DataFrame(df_job)
dlr['day'] = df_day
dlr['h_M'] = df_h_m
dlr.columns=['s_time','path','job','day','h_m']
dlr.to_csv("zj_sc_job.csv")




import os,sys
df = pd.read_csv(r'C:\Users\CBH\PycharmProjects\tensorflow\zj_sc_job.csv')
for i in range(len(df['job'])):
    log1 = '''sh {path} {job}'''.format(path = df['path'][i],job = df['job'][i])
    print(log1)
    path1 = r'C:\Users\CBH\Desktop\Azkaban3.47\zj'
    aa= str(df['job'][i].replace('.kjb','')).replace('/','\\')
    aa = aa.split('\\')[-1]
    # path2 = str(df['job'][i].replace('.kjb','')).replace('/','\\')
    path = os.path.join(path1,aa)
    print(path)
    f = open(path + '.sh', 'a')
    f.write(log1)
    f.close()


#job文件
df = pd.read_csv(r'C:\Users\CBH\PycharmProjects\tensorflow\zj_sc_job.csv')
for i in range(len(df['job'])):
    # print(i)
    text = '''type=command
command=sh /opt/earth/data-integration/kitchen.sh -file=/opt/earth/data-integration/etljob/{}
retries=1
retry.backoff=1800000'''.format(df['job'][i])
    print(text)
    path1 = r'C:\Users\CBH\Desktop\Azkaban3.47\zj'
    aa = str(df['job'][i].replace('.kjb', '')).replace('/', '\\')
    aa = aa.split('\\')[-1]
    # path2 = str(df['job'][-1].replace('.kjb','')).replace('/','\\')
    path = os.path.join(path1,aa )
    print(path)
    f = open(path + '.job', 'a')
    f.write(text)
    f.close()
    print(text)