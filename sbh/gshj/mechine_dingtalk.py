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
import pymysql
def send_msg(url,con_text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "Azkaban-leslie失败任务汇总："+con_text,
            # "title": "阿兹卡班报错汇总",
            # "picUrl": "图片连接",
            # "messageUrl": "你需要发布的连接地址"
        }
    }
    r = requests.post(url,data = json.dumps(data),headers=headers)
    return r.text
if __name__ == '__main__':
    conn = pymysql.connect(host="192.168.20.234", user ="root", password ="123456", database ="azkaban", charset ="utf8")
    cursor = conn.cursor()
    sql = '''
    SELECT
    flow_id,
        CASE
WHEN STATUS = 50 THEN
        'success'
WHEN STATUS = 70 THEN
        'failed'
WHEN STATUS = 30 THEN
        'running'
END AS STATUS,
CONCAT((end_time - start_time)/60000, '分钟')  as time

FROM
        azkaban.execution_flows
where
FROM_UNIXTIME(left(start_time, 10) ,'%Y-%m-%d %h:%m:%s') >= curdate()
and STATUS = 70
ORDER BY
        start_time DESC

    '''
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    # 关闭数据库连接
    conn.close()
    url = 'https://oapi.dingtalk.com/robot/send?access_token=bf9a08e87fa9218b3ce330b1e2986387cccedc1f9f83e26209c72a4cdf5baf13'                #此处为丁丁机器人的地址，参考技术手册创建
    con_text = str(data)
    print(send_msg(url,con_text))