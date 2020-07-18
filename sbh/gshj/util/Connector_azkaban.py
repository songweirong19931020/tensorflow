# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Connector_azkaban
   Description :
   Author :       CBH
   date：         2020/6/22 17: 11
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/22 17: 11:
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
import traceback


class AzkabanConnector:
    def __init__(self, url=r'https://192.168.4.216:8080/',
                 driver_path=r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe',
                 list_job_name=[], list_job_path=None, list_time=[]):
        '''
        :param url: 网址
        :param driver_path: chromeexe地址
        :param list_job_name: 文件名称--输入项
        :param list_job_path: 文件存放路径
        :param list_time:调度配置时间列表
        '''
        self.url = url
        self.driver_path = driver_path
        self.list_job_name = list_job_name
        self.list_job_path = list_job_path
        self.list_time = list_time

    def Loginweb(self, url, driver_path):
        driver = webdriver.Chrome(driver_path)
        driver.get(url)
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('password').send_keys('gsfy211')
        driver.find_element_by_id('login-submit').click()
        return driver

    def Get_list_name(self, list_job_name=[], list_job_path=None):
        '''
        :param list_job_path: 脚本存放路径
        :return: list_job_name: 脚本名称
        '''
        for i in os.listdir(list_job_path):
            list_job_name.append(i.replace('.job', ''))
        return list_job_name

    def Click_web_Executor(self, driver, list_time=[], list_job_name=None):
        '''
        自动配置调度时间核心代码块
        :param driver:
        :param list_time: 执行时间
        :param list_job_name: 脚本名称
        :return:None
        '''
        for i in list_job_name:
            time.sleep(2)
            # 点击history
            # driver.find_element_by_xpath("//*[@id='project-list']/li[3]/div/h4/a").click()
            # 点击Dwd_Job
            driver.find_element_by_xpath("//*[@id='project-list']/li[1]/div/h4/a").click()
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
            driver.find_element_by_xpath("//*[@id='timepicker']").send_keys(
                str(list_time[list_job_name.index(i)]) + ' AM')
            time.sleep(3)
            # 点击提交调度
            driver.find_element_by_xpath("//*[@id='schedule-button']").click()
            time.sleep(3)
            # 点击确定
            driver.find_element_by_xpath("//*[@id='azkaban-message-dialog']/div/div/div[3]/button").click()
            time.sleep(3)
            # 返回项目
            driver.find_element_by_xpath("//*[@class='navbar-collapse collapse']/ul/li[1]/a").click()
            time.sleep(5)


if __name__ == '__main__':
    a = AzkabanConnector()
    a.Loginweb(url=r'https://192.168.4.216:8080/',
               driver_path=r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe')
    a.Get_list_name(list_job_path=r'C:\Users\CBH\Desktop\azkaban\正式环境job\500name')
    list_dd = a.Get_list_name(list_job_name=[], list_job_path=r'C:\Users\CBH\Desktop\azkaban\正式环境job\500name')
    a.Click_web_Executor()
