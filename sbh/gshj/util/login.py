# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    login
   Description :
   Author :       CBH
   date：         2020/7/20 10: 25
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/20 10: 25:
-------------------------------------------------
"""
import logging
import time
# fh = logging.FileHandler(filename='tmp.log',encoding='utf-8') #解决乱码问题
# sh = logging.StreamHandler()
#
# logging.basicConfig(
#     format='[%(asctime)s] - [%(name)s] -  w_level:[%(levelname)s]- error_lineno:[%(lineno)d] - job_name:[%(module)s]  - detail: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     level=10,
#     handlers=[fh,sh],
#
#
# )
#
# logging.warning('错误告警！！！！！')

from logging import handlers
#日志的切分
sh = logging.StreamHandler()
rh = handlers.RotatingFileHandler('myapp.log',maxBytes=1024,backupCount=5,encoding='utf-8')
fh = handlers.TimedRotatingFileHandler(filename='x2.log',when='s',interval=6,encoding='utf-8')
logging.basicConfig(
    format='[%(asctime)s] - [%(name)s] -  w_level:[%(levelname)s]- error_lineno:[%(lineno)d] - job_name:[%(module)s]  - detail: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=10,
    handlers=[fh,sh,rh],


)
for  i in range(22):
    time.sleep(1)
    logging.error('错误！ %s'%str(i))