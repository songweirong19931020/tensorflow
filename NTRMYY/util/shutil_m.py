# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    shutil_m
   Description :
   Author :       CBH
   date：         2020/7/20 11: 05
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/20 11: 05:
-------------------------------------------------
"""
import shutil
shutil.copy2(r'C:\Users\CBH\PycharmProjects\tensorflow\auto.log',r'C:\Users\CBH\Desktop\work_job\BI') #复制文件到指定目录
#拷贝目录
shutil.copytree(r'C:\Users\CBH\PycharmProjects\tensorflow\sbh\gshj\util',
                r'C:\Users\CBH\PycharmProjects\tensorflow\sbh\gshj\util2',
                ignore=shutil.ignore_patterns("*.pyc"))#排除指定文件
#rmtree --删除文件
shutil.move('path','target_path',copy_function=shutil.copy2)

#获取磁盘使用空间
total,use,free = shutil.disk_usage('.')
print('当前磁盘%iGB,使用%iGB,剩余%iGB'%( total / 1073741824,use / 1073741824,free / 1073741824,))


#压缩文件
shutil.make_archive('压缩文件名','zip','待压缩文件路径')