# -*- coding: utf-8 -*-
# @File: crawl_p.py
# @Author: leslie
# @E-mail: wrsong@cenboomh.com
# @Software: PyCharm
# @Time: 2020/9/3  16:27
import requests
from multiprocessing import Process
'''
同步阻塞
    调用函数必须等待结果，cpu没工作   input sleep  connect get
同步非阻塞
    调用函数必须等待结果，cpu工作--调用一个高计算函数strip  max  min sum avg
异步阻塞
    调用函数不需要等待结果，而是继续做其它事情，不准获取谁结果，需要等（阻塞）
异步非阻塞
    调用函数不需要等待结果，也不需要等
'''

def producer():
    ret = requests.get('https://www.douban.com/doulist/1596699/')
    print(ret.text)
    ret.status_code




a = [1,2,3,4,5,6,7,8,9]
b = [2,3,4,5,6,7,8,9,0]
def fun(a):
    return a+1
res = map(lambda x,y:x+y,a,b)
print(res)
print(list(res))
res1 = map(fun,a)
print(res1)
print(list(res1))




a = [1,2,3,4,5,6,7,8,9]
def fun(a):
    return a % 2 ==0
res = filter(lambda x:x>5,a)
print(res)
print(list(res))
res1 = filter(fun,a)
print(res1)
print(list(res1))