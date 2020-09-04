# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    call_azmitor
   Description :
   Author :       CBH
   date：         2020/7/20 16: 30
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/20 16: 30:
-------------------------------------------------
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
from sbh.gshj.util.LogUitl import *
from sbh.gshj.azkaban.azkaban_mionitor import az_miontor
log = Logger('AZKABAN.log', logging.ERROR, logging.DEBUG)
scheduler = BlockingScheduler()
scheduler.add_job(az_miontor, 'interval', hours=24, start_date='2020-07-21 07:40:00', end_date='2020-12-15 11:00:00')
log.info("程序开始执行")
scheduler.start()
log.info("程序执行结束！")