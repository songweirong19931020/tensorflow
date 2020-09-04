# -*- coding: utf-8 -*-
# @File: study_all.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/9/2  16:43

'''
守护进程---在start之前写p.deamon=True(等待主进程代码结束后立即结束)
Lock----进程之间数据的安全问题
队列
进程之间数据隔离
进程之间通信 inter process communication-----简称IPC
    1；基于文件  ：同一台机器上的多个进程间通信
        基于socket文件级别通信来传递数据
    2；基于网络  ：同一台机器或者多台机器上的多进程通信
        第三方工具（消息中间件）
        memcache
        redis
        kafka
        rabbitmg

队列 Queue   put  与  get
生产者消费者模型
分布式框架celery-------本质：让生产和消费数据达到平衡的最大效率

有几个消费者放几个None
'''
# from multiprocessing import Lock
# lock = Lock()
# lock.acquire() #拿锁
# lock.release() #还钥匙

import random
import time
from multiprocessing import Queue,Process
def consumer(q,name): #消费者:取到数据之后还要对数据进行操作
    while True:
        food = q.get()
        if food:
            print('%s吃了%s'%(name,food))
        else: break

def producer(q,name,food):  #生产者 ： 放数据之前通过代码获取数据
    for i in range(10):
        foodi = '%s%s'%(food,i)
        print('%s生产了%s'%(name,foodi))
        q.put(foodi)


if __name__ == '__main__':
    q = Queue()
    c1 = Process(target=consumer,args=(q,'wxd'))
    p1 = Process(target=producer,args=(q,'lz','潲水'))
    p2 = Process(target=producer,args=(q,'hz','香蕉'))
    c1.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)