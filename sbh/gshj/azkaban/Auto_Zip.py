# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    Auto_Zip
   Description :
   Author :       CBH
   date：         2020/7/7 16: 37
   Ide:           PyCharm
-------------------------------------------------
   Change Activity:
                   2020/7/7 16: 37:
-------------------------------------------------
"""
import os
import zipfile
import glob

def zip_dir(dir_path, zip_path):
    '''
    压缩函数
    :param dir_path: 目标文件夹路径
    :param zip_path: 压缩后的文件夹路径
    :return:
    '''

    # os.remove(zip_path)
    if os.path.exists(zip_path):
        os.remove(zip_path)
        zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        for root, dirnames, filenames in os.walk(dir_path):
            file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
            # 循环出一个个文件名
            for filename in filenames:
                zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        zip.close()
    else:
        zip = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        for root, dirnames, filenames in os.walk(dir_path):
            file_path = root.replace(dir_path, '')  # 去掉根路径，只对目标文件夹下的文件及文件夹进行压缩
            # 循环出一个个文件名
            for filename in filenames:
                zip.write(os.path.join(root, filename), os.path.join(file_path, filename))
        zip.close()


def unzip_file(dir_path,unzip_file_path=r"C:\Users\CBH\Desktop\azkaban\正式环境job\解压文件"):
    # 解压缩后文件的存放路径
    # unzip_file_path = r"C:\Users\CBH\Desktop\azkaban\正式环境job"
    # 找到压缩文件夹
    dir_list = glob.glob(dir_path)
    if dir_list:
        # 循环zip文件夹
        for dir_zip in dir_list:
            # 以读的方式打开
            with zipfile.ZipFile(dir_zip, 'r') as f:
                for file in f.namelist():
                    f.extract(file, path=unzip_file_path)
            os.remove(dir_zip)


if __name__ == '__main__':
    zip_dir(r"C:\Users\CBH\Desktop\azkaban\正式环境job\DW", r"C:\Users\CBH\Desktop\azkaban\正式环境job\zip_path\DW" + '.zip')
    zip_dir(r"C:\Users\CBH\Desktop\azkaban\正式环境job\DWD", r"C:\Users\CBH\Desktop\azkaban\正式环境job\zip_path\DWD" + '.zip')
    zip_dir(r"C:\Users\CBH\Desktop\azkaban\正式环境job\Ods", r"C:\Users\CBH\Desktop\azkaban\正式环境job\zip_path\Ods" + '.zip')
    zip_dir(r"C:\Users\CBH\Desktop\azkaban\正式环境job\替代文件", r"C:\Users\CBH\Desktop\azkaban\正式环境job\zip_path\history" + '.zip')
    zip_dir(r"C:\Users\CBH\Desktop\azkaban\正式环境job\Dashboard", r"C:\Users\CBH\Desktop\azkaban\正式环境job\zip_path\Dashboard" + '.zip')