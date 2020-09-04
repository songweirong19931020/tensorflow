# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    LogUitl
   Description :
   Author :       CBH
   date：         2020/6/30 15: 38
   Ide:           PyCharm
-------------------------------------------------
"""
import logging,os
class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] - [%(name)s] -  w_level:[%(levelname)s] - job_name:[%(module)s] - detail: %(message)s', '%Y-%m-%d %H:%M:%S')
        ch = logging.StreamHandler()
        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        ch.setLevel(logging.DEBUG)
        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        ch.setFormatter(fmt)
        self.logger.addHandler(ch)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        '''

        :param message:
        :return: 测试
        '''
        self.logger.debug(message)

    def info(self, message):
        '''
        输入信息
        :param message:
        :return:
        '''
        self.logger.info(message)

    def war(self, message):
        '''
        告警
        :param message:
        :return:
        '''
        self.logger.warn(message)

    def error(self, message):
        '''
        错误
        :param message:
        :return:
        '''
        self.logger.error(message)

    def cri(self, message):
        '''
        批判性
        :param message:
        :return:
        '''
        self.logger.critical(message)




