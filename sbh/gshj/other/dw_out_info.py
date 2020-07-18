# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    connect_gs
   Description :
   Author :       CBH
   date：         2020/5/11 10: 47
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/11 10: 47:
-------------------------------------------------
"""

import psycopg2
import time

day_format_id = "'"+str(time.strftime("%Y%m%d", time.localtime()))+"'"

for i in range(10):
    print(i+1)
    print("'"+str(20200101+i)+"'")
conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres", database="postgres")
cur = conn.cursor()


list_time=['20200101','20200131','20200201','20200229','20200301','20200331','20200401','20200430','20200501','20200531','20200601','20200619']
list_function = ['fun_dwd_D05000_d','fun_dwd_D05001_d','fun_dwd_D05002_d','fun_dwd_D05003_d','fun_dwd_D05004_d','fun_dwd_D05005_d','fun_dwd_D05006_d','fun_dwd_D05007_d','fun_dwd_D05008_d','fun_dwd_D05009_d','fun_dwd_D05010_d','fun_dwd_D05011_d','fun_dwd_D05012_d','fun_dwd_D05013_d','fun_dwd_D05014_d','fun_dwd_D05015_d','fun_dwd_D05016_d','fun_dwd_D05017_d','fun_dwd_D05018_d','fun_dwd_D05019_d','fun_dwd_D05020_d','fun_dwd_D05021_d','fun_dwd_D05022_d','fun_dwd_D05023_d']

for t_time in range(len(list_time)):
    for i in range(len(list_function)):
        conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres",
                                database="postgres")
        cur = conn.cursor()
        sql = ''' select his_bi."''' + str(list_function[i]) + '"' + '''('{}','{}') '''.format(list_time[t_time],
                                                                                                list_time[t_time + 1])
        print(sql)
        cur.execute(sql)
        # data = cur.fetchall()
        conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
        cur.close()
        conn.close()



    conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres", database="postgres")
    cur = conn.cursor()
    day_format_id="'"+str(20200101+i)+"'"
    sql = """
    insert into his_bi.dwd_outp_inconme_d_temp(key,value,patient_id,visit_id,outp_visit_id,insert_date,																		 remark,st_date) 
     select 
                     'D00014' as key,
                     coalesce(sum(t.charges),0) as value ,
                     t.patient_id patient_id,
                     t.visit_id visit_id,
                     p.outp_visit_id outp_visit_id,
             now() insert_date,
                  '门诊患者总费用' remark,
                  to_char(t.enter_date,'yyyymmdd') AS st_date
       from his_bi.bms_bill_item t
      inner join his_bi.pts_outp_patient_visit p
           on t.patient_id = p.patient_id
          and t.visit_id = p.visit_id
      where t.enter_date >= to_date({day_format_id},'yyyyMMdd')
        and t.enter_date <  to_date({day_format_id},'yyyyMMdd')+1
        and t.in_out_flag = 'O' --只统计门诊患者
        and t.charges<>0
      group by to_char(t.enter_date,'yyyymmdd'),
                         t.patient_id,
                         t.visit_id,
                       p.outp_visit_id;
    """.format(day_format_id=day_format_id)
    print(sql)
    cur.execute(sql)
    #data = cur.fetchall()
    conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
    cur.close()
    conn.close()