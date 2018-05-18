# -*- coding: utf-8 -*-
from __future__ import print_function, division
import os


if __name__ == '__main__':
    #切换到Android sdk所在路径
    os.system('cd E:\\Users\\shankai\\AppData\\Local\\Android\\sdk\\tools\\bin')
    #清空cache
    os.system('adb shell echo > proc/proc_test_root/test_hello')
    os.system('adb shell echo > /data/a.txt')
    #保存统计信息到文件
    os.system('cat proc/proc_test_root/test_hello | head - n 2 > /data/a.txt')
    # drop cache
    os.system('echo 1 > /proc/sys/vm/drop_caches')
    #重放trace
    os.system('.\sk.bat')
    # 保存统计信息到文件
    os.system('cat proc/proc_test_root/test_hello | head - n 2 > /data/a.txt')
    # drop cache
    os.system('echo 1 > /proc/sys/vm/drop_caches')
    #将统计的文本文件拉到本地
    os.system('adb pull /data/a.txt C:\\Users\\shankai\\Desktop\\')