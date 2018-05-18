# -*- coding: utf-8 -*-
from __future__ import print_function, division
import os
import time
import datetime
import re
import cv2

from common.auto_adb import auto_adb

VERSION = "1.1.4"
scale = 1

# 加载QQ空间/微博/朋友圈中的那只点赞的手
template = cv2.imread('./resource/image/weibozan.png')
template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
template_size = template.shape[:2]


def pull_screenshot():
    filename = datetime.datetime.now().strftime("%H%M%S") + '.png'
    os.system('mv autojump.png {}'.format(filename))
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png ./autojump.png')

def wait(seconds):
    global f

    time.sleep(seconds)

    recordcmd = ' WAIT | {\'seconds\':%d,}' % (seconds)
    f.write(recordcmd + "\n")

def swipe(x1,y1,x2,y2):
    global f

    cmd = 'adb shell input swipe {} {} {} {}'.format(x1,y1,x2,y2)
    print(cmd)
    os.system(cmd)

    recordcmd = 'DRAG|{\'start\':(%d,%d),\'end\':(%d,%d),\'duration\':1.0,\'steps\':10,}' % (x1,y1,x2,y2)
    f.write(recordcmd + "\n")

def tap(x,y):
    global  f

    cmd = 'adb shell input tap {} {}'.format(x,y)
    print(cmd)
    os.system(cmd)

    recordcmd='TOUCH|{\'x\':%d,\'y\':%d,\'type\':\'downAndUp\',}' % (x,y)
    f.write(recordcmd+"\n")

def search(img):
    result = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 返回矩形的中心点坐标
    return  min_loc[0] + template_size[1] / 2, min_loc[1] +  template_size[0]


def update_data():
    global src_x, src_y
    global f

    f = open('./myQQ.mr', 'a')
    img = cv2.imread('./autojump.png')
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    return img

"""
获取手机屏幕大小

返回值： height,width
"""
def get_screen_size():
    adb = auto_adb()
    size_str = adb.get_screen()
    m = re.search(r'(\d+)x(\d+)', size_str)
    if m:
        return m.group(2),m.group(1)
    return 1920,1080

if __name__ == '__main__':
    n=100
    screen_height,screen_width=get_screen_size();

    for i in range(n):
        # 将屏幕截图拷贝到当前路径下
        pull_screenshot()
        img = update_data()
        x,y=search(img)
        tap(x,y)
        wait(5)
        print (screen_height)
        step= int(screen_height) * 0.66
        print(step)
        step=int(step)
        if(y-step<0):
            step=y
        swipe(x,y,x,y-step)
        wait(5)

