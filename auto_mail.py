# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    auto_mail
   Description :
   Author :       CBH
   date：         2020/5/16 15: 16
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/5/16 15: 16:
-------------------------------------------------
"""
import yamail
#链接邮箱服务器
yag = yamail.SMTP( user="wrsong@cenboomh.com", password="Sbh123", host='smtp.exmail.qq.com',port=465)
# 邮箱正文

contents = ['This is test_mail!']

# 发送邮件
yag.send('wrsong@cenboomh.com', 'subject', contents)
#关闭
yag.close()





