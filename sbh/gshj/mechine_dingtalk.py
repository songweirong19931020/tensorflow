# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    mechine_dingtalk
   Description :
   Author :       CBH
   date：         2020/6/27 10: 20
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/27 10: 20:
-------------------------------------------------
"""
import json
import requests
import sys
from sbh.gshj.util.account import PgSQLContextManager
import pandas as pd
def myjob():
    def send_msg(url,con_text):
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        data = {
            "msgtype": "text",
            "text": {
                "content": "Azkaban-leslie失败任务汇总：\n"+con_text+"@Leslie_Song",
                # "title": "阿兹卡班报错汇总",
                # "picUrl": "图片连接",
                # "messageUrl": "你需要发布的连接地址"
            }
        }
        r = requests.post(url,data = json.dumps(data),headers=headers)
        return r.text

    with PgSQLContextManager() as db_cursor:
        executor_sql = '''select project_name,flow_id,status from his_bi.azkaban_monitor_job where left("start",10)=to_char(CURRENT_DATE,'yyyy-mm-dd')
    and status = 'failed' order by start desc limit 10 '''
        db_cursor.execute(executor_sql)
        result = db_cursor.fetchall()
        print(result)
        df = pd.DataFrame(result)
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bf9a08e87fa9218b3ce330b1e2986387cccedc1f9f83e26209c72a4cdf5baf13'                #此处为丁丁机器人的地址，参考技术手册创建
    result_list = []
    if df.empty == False:
        for i in range(len(df[0])):
            con_text = '''项目名称：{project_name},执行失败任务名称:{executor_job}'''\
                .format(project_name=df[0][i],executor_job=df[1][i])
            print(con_text)
            result_list.append(con_text)
    else:
        result_list.append('任务全部执行成功！')
    print(send_msg(url,str(result_list)))

myjob()

# 以下为定时调度任务，在每天早上八点执行
# from datetime import date,datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# sched = BlockingScheduler()
# print('程序开始执行')
# # 在2009年11月6日执行
# sched.add_job(myjob, 'interval', hours=24, start_date='2020-8-14 08:00:00', end_date='2020-9-14 08:00:00')
# print('等待定时任务触发！')
# sched.start()