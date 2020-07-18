# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    auto_unpload
   Description :
   Author :       CBH
   date：         2020/6/18 12: 18
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/18 12: 18:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import lxml
import os, sys
import pandas as pd

# chrome_options= webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #配置不显示chrome
# chrome_options.add_argument('--disable-gpu')

# list_time=['04:00','04:01','04:02','04:03','04:04','04:05','04:06','04:07','04:08','04:09','04:10','04:11','04:12','04:13','04:14','04:15','04:16','04:17','04:18','04:19','04:20','04:21','04:22','04:23','04:24','04:25','04:26','04:27','04:28','04:29','04:30','04:31','04:32','04:33','04:34','04:35','04:36','04:37','04:38','04:39','04:40','04:41','04:42','04:43','04:44','04:45','04:46','04:47','04:48','04:49','04:50','04:51','04:52','04:53','04:54','04:55','04:56','04:57','04:58','04:59','05:00','07:58','07:59','08:00','08:01','08:02','08:03','08:04','08:05','08:06','08:07','08:08','08:09','08:10','08:11','08:12','08:13','08:14','08:15','08:16','08:17','08:18','08:19','08:20','08:21','08:22','08:23','08:24','08:25','08:26','08:27','08:28','08:29','08:30','08:31','08:32','08:33','08:34','08:35','08:36','08:37','08:38','08:39','08:40','08:41','08:42','08:43','08:44','08:45','08:46','08:47','08:48','08:49','08:50','08:51','08:52','08:53','08:54','08:55','08:56','08:57','08:58','08:59','09:00','09:01','09:02','09:03','09:04','09:05','09:06','09:07','09:08','09:09','09:10','09:11','09:12','09:13','09:14','09:15','09:16','09:17','09:18','09:19','09:20','09:21','09:22','09:23','09:24','09:25','09:26','09:27','09:28','09:29','09:30','09:31','09:32','09:33','09:34','09:35','09:36','09:37','09:38','09:39','09:40','09:41','09:42','09:43','09:44','09:45','09:46','09:47','09:48','09:49','09:50','09:51','09:52','09:53','09:54','09:55','09:56','09:57','09:58','09:59','10:00']
list_time = ['5:41','5:58','5:59','6:04','6:25','6:30','5:20','5:29','5:31','5:43','5:30','6:22','6:26','6:27','5:37','5:42','5:54','5:55','6:05','6:21','6:24','6:29','5:36','5:38','5:52','5:57','6:13','6:18','6:01','6:10','6:00','5:40','5:46','6:08','5:23','5:26','5:34','5:47','5:49','6:02','6:19','5:32','5:33','5:48','5:56','6:09','6:17','6:20','5:24','5:35','5:44','6:06','6:07','6:15','5:25','5:27','5:50','5:45','6:11','6:14','5:21','5:28','5:39','6:23','6:28','5:22','5:51','5:53','6:03','6:12','6:16','5:36','5:38','5:52','5:57','6:13','6:18']
url = r'https://192.168.4.216:8080/'
driver_path = r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe'

driver = webdriver.Chrome(driver_path)
driver.get(url)

driver.find_element_by_id('username').send_keys('admin')

driver.find_element_by_id('password').send_keys('gsfy211!')

driver.find_element_by_id('login-submit').click()

# 获取flow名称
list_job_name = []
for i in os.listdir(r'C:\Users\CBH\Desktop\azkaban\正式环境job\sql'):
    print(i.replace('.job', ''))
    list_job_name.append(i.replace('.job', ''))

list_time_10 = list_time * 2
for g_result in list_job_name:
    print(g_result)
    print(list_time_10[list_job_name.index(g_result)])


list_job_name = ['pg_d_121',
'pg_d_122',
'pg_d_123',
'pg_d_124',
'pg_d_125',
'pg_d_126',
'pg_d_127',
'pg_d_128',
'pg_d_129',
'pg_d_130',
'pg_d_131',
'pg_d_132',
'pg_d_133',
'pg_d_134',
'pg_d_135',
'pg_d_136',
'pg_d_137',
'pg_d_138',
'pg_d_139',
'pg_d_140',
'pg_d_141',
'pg_d_142',
'pg_d_143',
'pg_d_144',
'pg_d_145',
'pg_d_146',
'pg_d_148',
'pg_d_149',
'pg_d_150',
'pg_d_151',
'pg_d_152',
'pg_d_153',
'pg_d_154',
'pg_d_155',
'pg_d_156',
'pg_d_157',
'pg_d_158',
'pg_d_159',
'pg_d_160',
'pg_d_161',
'pg_d_162',
'pg_d_163',
'pg_d_164',
'pg_d_165',
'pg_d_166',
'pg_d_167',
'pg_d_168',
'pg_d_169',
'pg_d_170',
'pg_d_171',
'pg_d_172',
'pg_d_174',
'pg_d_175',
'pg_d_176',
'pg_d_177',
'pg_d_178',
'pg_d_179',
'pg_d_180',
'pg_d_195',
'pg_d_181',
'pg_d_182',
'pg_d_183',
'pg_d_184',
'pg_d_185',
'pg_d_186',
'pg_d_187',
'pg_d_188',
'pg_d_189',
'pg_d_190',
'pg_d_191',
'pg_d_192',
'pg_d_193',
'pg_d_194',
'pg_d_196',
'pg_d_197',
'pg_d_198',
'pg_d_199',]

# 自动提交调度时间
for i in list_job_name:
    try:
        time.sleep(5)
        # 点击history
        driver.find_element_by_xpath("//*[@id='project-list']/li[4]/div/h4/a").click()
        # 点击Dwd_Job
        # driver.find_element_by_xpath("//*[@id='project-list']/li[2]/div/h4/a").click()
        # 这里需要等待5秒左右
        time.sleep(3)
        # 点击executor按钮
        location = "//*[@flow='{}']/div/div/button".format(i)
        driver.find_element_by_xpath(location).click()
        time.sleep(3)
        # 点击调度按钮
        driver.find_element_by_xpath("//*[@id='schedule-btn']").click()
        time.sleep(3)
        # 获取时间文本输入框
        driver.find_element_by_xpath("//*[@id='timepicker']").send_keys(str(list_time[list_job_name.index(i)]) + ' AM')
        time.sleep(3)
        # 点击提交调度
        driver.find_element_by_xpath("//*[@id='schedule-button']").click()
        time.sleep(4)
        # 点击确定
        driver.find_element_by_xpath("//*[@id='azkaban-message-dialog']/div/div/div[3]/button").click()
        time.sleep(5)
        # 返回项目
        driver.find_element_by_xpath("//*[@class='navbar-collapse collapse']/ul/li[1]/a").click()
        time.sleep(1)
        print("执行任务名称：{name},执行调度时间：{time}".format(name=i, time=str(list_time[list_job_name.index(i)]) + ' AM'))
    except:
        driver.find_element_by_xpath("//*[@class='navbar-collapse collapse']/ul/li[1]/a").click()
        print("执行出错，任务名：{name},调度时间:{time}".format(name=i, time=str(list_time[list_job_name.index(i)]) + ' AM'))
        continue

# 自动重跑当天失败job
