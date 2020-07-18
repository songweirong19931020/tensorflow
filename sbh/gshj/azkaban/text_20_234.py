# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    text_20_234
   Description :
   Author :       CBH
   date：         2020/6/27 11: 14
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/27 11: 14:
-------------------------------------------------
"""
import pymysql
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