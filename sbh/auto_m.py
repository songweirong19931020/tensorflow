# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    auto_m
   Description :
   Author :       CBH
   date：         2020/6/4 15: 27
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/6/4 15: 27:
-------------------------------------------------
"""
from pywinauto import application
from pywinauto.keyboard import send_keys
from pywinauto import mouse
import time
from datetime import datetime, date, timedelta
import datetime
import requests
import win32gui

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)



import requests
while True:
    try:
        now_time = (datetime.datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        response = requests.get('http://192.168.4.215:9090/')
        print('执行时间:{},网络连接正常，无需重连！'.format(now_time))
        time.sleep(60)
    except:
        # 方式一：创建应用程序时可以，指定应用程序的合适的backend，start方法中指定启动的应用程序
        app = application.Application(backend='uia').start('C:\Program Files (x86)\Gateway\SSLVPN\gwclient.exe')
        # app = application.Application().start('C:\Program Files (x86)\Gateway\SSLVPN\gwclient.exe')
        wind_1 = app.actions
        time.sleep(3)
        send_keys("{VK_RETURN}")
        time.sleep(15)
        mouse.press(button='left', coords=(940, 450)) #账号
        send_keys("J0009")
        time.sleep(5)
        mouse.press(button='left', coords=(940, 500)) #密码
        send_keys("12345678")
        time.sleep(2)
        send_keys("{VK_RETURN}")