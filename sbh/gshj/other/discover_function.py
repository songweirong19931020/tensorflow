# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    discover_function
   Description :
   Author :       CBH
   date：         2020/7/24 11: 29
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/24 11: 29:
-------------------------------------------------
"""

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def func_menu(menu):
    flag = True
    while flag:
        for name in menu:
            print(name)
        key  = input('>>>').strip()
        if menu.get(key):
            dic = menu[key]
            func_menu(dic)
        elif key.upper()=='B':
            return True
        elif key.upper()=='Q':
            return False

func_menu(menu)



'''
装饰器--不改变原函数代码和调用方式
*args,**kwargs
'''
import time
def index():
    '''many code'''
    time.sleep(2)
    print('weclome my house!')

def timeer(f):
    def inner():
        start_time = time.time()
        f()
        end_time = time.time()
        print(f'测试运时间{end_time-start_time}')
    return inner

index = timeer(index)
index()


'''标准装饰器语法'''
def wrapper(f):
    def inner(*args,**kwargs):
        '''添加额外的功能，执行被装饰函数之前的操作'''
        ret = f(*args,**kwargs)
        '''添加额外的功能，执行被装饰函数之后的操作'''
        return ret
    return inner