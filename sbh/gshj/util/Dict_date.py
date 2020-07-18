# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Dict_date
   Description :
   Author :       CBH
   date：         2020/7/4 21: 01
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/4 21: 01:
-------------------------------------------------
"""
import datetime
import time

today = today = datetime.date.today()


def Get_Time_All(list_time=[]):
    '''
    :param list_time:
    :return: date_list:存放日期列表，保存到20200101-当前时间
    '''
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date.today()
    for i in range(start_date.toordinal(), end_date.toordinal()):
        # print(datetime.date.fromordinal(i))
        list_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m%d")))
    date_list = list_time
    return date_list


def Get_Month_All(month_time=[]):
    '''
    :param month_time:
    :return: month_list:存放202001-T-1月份数据数据
    '''
    start_month = datetime.date(2020, 1, 1)
    first = today.replace(day=1)
    end_month = (first - datetime.timedelta(days=1))
    # b = datetime.date.today()
    # month_time=[]
    for i in range(start_month.toordinal(), end_month.toordinal()):
        # print(datetime.date.fromordinal(i))
        month_time.append(int(datetime.date.fromordinal(i).strftime("%Y%m")))
        month_list = list(set(month_time))
    return month_list
