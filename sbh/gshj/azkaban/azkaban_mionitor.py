# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    azkaban_mionitor
   Description :
   Author :       CBH
   date：         2020/7/20 15: 06
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/20 15: 06:
-------------------------------------------------
"""
from sbh.gshj.util.Connector_azkaban import *
import re

az = AzkabanConnector()
driver = az.Loginweb(url=r'https://192.168.4.216:8080/',
           driver_path=r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe')

driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@class='nav navbar-nav']/li[4]/a").click() #点击history

#输入jobname
driver.find_element_by_xpath("//*[@id='searchtextbox']").send_keys("azkaban_miontior")
#点击查询
driver.find_element_by_xpath("//*[@class='btn btn-primary btn-sm']").click()
#点击executor_id
driver.find_element_by_xpath("//*[@id='executingJobs']/tbody/tr[1]/td[1]/a").click()
#点击job_list
driver.find_element_by_xpath("//*[@id='jobslistViewLink']/a").click()
#点击detail
driver.find_element_by_xpath("//*[@class='details']/a").click()

txt = driver.find_element_by_xpath("//*[@id='logSection']")

pat = re.compile('[\u4e00-\u9fa5]+')
ret = re.search(pat,txt.text)


result=''
if ret.group() == '无数据插入':
    result= '任务全部执行成功！'
else:
    result = '任务执行失败,请检查！'
import json
import requests
import sys
import datetime
today = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
def send_msg(url,con_text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "text": {
            "content": "调度日期：{date_now},Azkaban-leslie运行情况：{con_text}".format(date_now=today,con_text=con_text),
            # "title": "阿兹卡班报错汇总",
            # "picUrl": "图片连接",
            # "messageUrl": "你需要发布的连接地址"
        }
    }
    r = requests.post(url,data = json.dumps(data),headers=headers)
    return r.text


url = 'https://oapi.dingtalk.com/robot/send?access_token=bf9a08e87fa9218b3ce330b1e2986387cccedc1f9f83e26209c72a4cdf5baf13'                #此处为丁丁机器人的地址，参考技术手册创建
con_text = str(result)
print(send_msg(url,con_text))
driver.quit()