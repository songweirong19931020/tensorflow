# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    azkaban
   Description :
   Author :       CBH
   date：         2020/6/12 09: 52
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/12 09: 52:
-------------------------------------------------
"""
import requests, json
import urllib3

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'

str_url='https://192.168.20.234:8443/'
# 登录信息
postdata = {'username': 'admin', 'password': 'admin'}

# 登录，通过verify=False关闭安全验证
login_url = str_url + '?action=login'
r = requests.post(login_url, postdata, verify=False).json()


postdata = {'session.id': r['session.id'], 'ajax': 'fetchexecflow', 'execid': 30}

fetch_url = str_url + '/executor?ajax=fetchexecflow'
ar = requests.get(fetch_url, postdata, verify=False)



postdata = {'session.id':  r['session.id'], 'ajax': 'fetchExecJobLogs', 'execid': '30', 'jobId': 'pg_d_00227', 'offset': 10,
    'length': 100}
fetch_url = str_url + '/executor?ajax=fetchExecJobLogs'
rz = requests.get(fetch_url, postdata, verify=False).json()