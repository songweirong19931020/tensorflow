# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    download
   Description :
   Author :       CBH
   date：         2020/4/30 16: 05
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/4/30 16: 05:
-------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

def save(url, path):
    response = requests.get(url)
    with open(path, 'wb') as img:
        img.write(response.content)
        img.close()

option = webdriver.ChromeOptions()
option.add_argument("--headless")

browser = webdriver.Chrome()
browser.get('https://pan.baidu.com/share/init?surl=fSNoWBhNhTe7bQ5JLlJSnA')

input = browser.find_element_by_css_selector("input.QKKaIE")
button_1 = browser.find_element_by_css_selector("span.text")

input.send_keys("xxxx")
for i in range(4):
    button_1.click()
    time.sleep(0.1)

button_2 = browser.find_element_by_css_selector("a.change-code")
img = browser.find_element_by_css_selector("img#zveq8bO")
path = r"C:\Users\CBH\PycharmProjects\tensorflow\temp"
for i in range(500):
    time.sleep(0.05)
    save(img.get_attribute("src"), path + "_" + str(i) + ".jpg")
    button_2.click()

browser.close()