# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    inp_flow
   Description :
   Author :       CBH
   date：         2020/5/21 16: 47
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/21 16: 47:
-------------------------------------------------
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import lxml

import pandas as pd
chrome_options= webdriver.ChromeOptions()
# chrome_options.add_argument('--headless') #配置不显示chrome
#chrome_options.add_argument('--disable-gpu')
url = r'http://192.168.4.150:8080/webroot/decision/view/report?viewlet=core/daily/inp_adt.cpt&op=write'
driver_path = r'C:\Users\CBH\AppData\Local\Google\Chrome\Application\chromedriver.exe'

driver = webdriver.Chrome(driver_path,chrome_options=chrome_options)
driver.get(url)

#js定制化输入开始日期
js1 = 'document.getElementsByClassName("fr-trigger-texteditor")[2].value="2020-05-01";'
driver.execute_script(js1)

#结束日期
js2 = 'document.getElementsByClassName("fr-trigger-texteditor")[0].value="2020-05-12";'
driver.execute_script(js2)

#查询event
driver.find_element_by_id('fr-btn-FORMSUBMIT0').click() #查询按钮

#实例化页面text
data = driver.page_source
soup = BeautifulSoup(data,'html.parser')
rows = soup.find_all('tr')
reslut = []
for row in rows:
    cell = [i.text for i in row.find_all('td')]
    print(cell)
    reslut.append(cell)
del reslut[0:10]

df = pd.DataFrame(reslut)
df = df.drop([0,1],axis=1)
df = df.drop(df.index[-3:])
df.to_csv(r'demo.csv',index=False)
df = df.fillna(0)
#df.columns=['','B','c']
########### 数据插入PG库
import psycopg2
import time
for i in range(0,29):
    conn = psycopg2.connect(host="192.168.4.205", port=5432, user="postgres", password="postgres", database="postgres")
    cur = conn.cursor()
    sql = """
    insert into his_bi.demo_py("2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29") 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    # conn.commit()
    cur.execute(sql,
                (
                    str(df[2][i]),
                    str(df[3][i]),
                    str(df[4][i]),
                    str(df[5][i]),
                    str(df[6][i]),
                    str(df[7][i]),
                    str(df[8][i]),
                    str(df[9][i]),
                    str(df[10][i]),
                    str(df[11][i]),
                    str(df[12][i]),
                    str(df[13][i]),
                    str(df[14][i]),
                    str(df[15][i]),
                    str(df[16][i]),
                    str(df[17][i]),
                    str(df[18][i]),
                    str(df[19][i]),
                    str(df[20][i]),
                    str(df[21][i]),
                    str(df[22][i]),
                    str(df[23][i]),
                    str(df[24][i]),
                    str(df[25][i]),
                    str(df[26][i]),
                    str(df[27][i]),
                    str(df[28][i]),
                    str(df[29][i])
                )
                )

    conn.commit()  # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
    cur.close()
    conn.close()


















#
# soup = BeautifulSoup(data,'html.parser')
#
#
# table_td = soup.find_all('td',class_="fh tac bw pl2 br1 brw1 brss brcb bb1 bbw1 bbss bbcb bl1 blw1 blss blcb bt0")
#
# table_tr = soup.find_all('tr')
#
#
# items = soup.find_all('td',class_="fh tac bw pl2 br1 brw1 brss brcb bb1 bbw1 bbss bbcb bl1 blw1 blss blcb bt0")
#
# for item in items:
#     try:
#         print(item)
#
#         t = item.find('div')
#         print(t.text)
#     except:
#         continue
#
# for g in soup.find_all('td',class_='fh tac bw pl2 br1 brw1 brss brcb bb1 bbw1 bbss bbcb bl1 blw1 blss blcb bt0'):
#     try:
#         # print('第'+g['row']+'行' + '第'+ g['col']+'列')
#         print(g['cv'],end=" ")
#         if (int(g['col']) % 28 == 0):
#             print('\n')
#         # num += 1
#     except:
#         continue
#
#
# soup.find('table',id="ctl00_ContentMain_SearchResultsGrid_grid")
# a = driver.find_element_by_xpath("//*[@class='pmeter-container fr-absolutelayout ui-state-enabled']/div[5]").click()
#
# driver.find_element_by_xpath("//*[@class='pmeter-container fr-absolutelayout ui-state-enabled']/div[5]").send_keys(Keys.CONTROL, 'a')
# driver.find_element_by_xpath("//*[text()='fr-trigger-text']").click()
#
# soup = BeautifulSoup(ht,'html.parser')
# a = soup.find('table',class_="x-table")
