# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Time_Util
   Description :
   Author :       CBH
   date：         2020/6/12 07: 32
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/12 07: 32:
-------------------------------------------------
"""
from datetime import datetime, date, timedelta
import datetime
import time
today = datetime.date.today()
t_date_time = (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
def Get_Yesterday():
    '''
    :return:T-1 date
    '''
    yesterday = (today - datetime.timedelta(days=1)).strftime("%Y%m%d")
    return yesterday


def Get_Last_Day_15():
    '''
    :return: T-15 date
    '''
    day_15 = (today - datetime.timedelta(days=15)).strftime("%Y%m%d")
    return day_15

def Get_Last_Day_20():
    '''
    :return: T-25 date
    '''
    day_20 = (today - datetime.timedelta(days=20)).strftime("%Y%m%d")
    return day_20


def Get_Last_Day_30():
    '''
    :return: T-30 date
    '''
    day_30 = (today - datetime.timedelta(days=30)).strftime("%Y%m%d")
    return day_30

def Get_Day():
    '''
    :return: today date
    '''
    return today

def Get_Last_Month():
    '''
    :return: 上个月，格式为yyyymm
    '''
    first = today.replace(day=1)
    last_month = (first - datetime.timedelta(days=1)).strftime("%Y%m")
    return last_month

def Get_Last_2_Month():
    '''
    :return:上两个月，格式：yyyymm
    '''
    first_2 = today.replace(month=int(time.strftime("%m", time.localtime())) - 2)
    last_2_month = first_2.replace(day=1).strftime("%Y%m")
    return last_2_month

def Get_Begin_Month():
    '''
        :return: 本月-指定日期为月初1号
        '''
    first = today.replace(day=1)
    return first

def Get_Last_Month_id():
    '''
    :return: 上个月-指定日期为月初1号
    '''
    first = today.replace(day=1)
    last_month_id = ((first - datetime.timedelta(days=1)).replace(day=1)).strftime("%Y%m%d")
    return last_month_id

def Get_Last_2_Month_id():
    '''
        :return: 上两个月-指定日期为月初1号
     '''
    first_2 = today.replace(month=int(time.strftime("%m", time.localtime())) - 2)
    last_2_month_id = first_2.replace(day=1).strftime("%Y%m%d")
    return last_2_month_id


def Get_Time_Qj_30(list_time=[]):
    a = (today - datetime.timedelta(days=30))
    b = datetime.date.today()
    for i in range(a.toordinal(), b.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(datetime.date.fromordinal(i).strftime("%Y%m%d"))
    return list_time


first_2 = today.replace(month=int(time.strftime("%m", time.localtime())) - 2)