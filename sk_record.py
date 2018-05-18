# -*- coding: utf-8 -*-
from __future__ import print_function, division
import os
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2

VERSION = "1.1.4"
scale = 0.75

def pull_screenshot():
    os.system('adb root')

    filename = datetime.datetime.now().strftime("%H%M%S") + '.png'
    os.system('mv autojump.png {}'.format(filename))
    os.system('adb shell su 0 screencap -p /data/autojump.png')
    os.system('adb pull /data/autojump.png ./autojump.png')

def tap(x,y):
    global  f

    x=int(x/scale)
    y=int(y/scale)

    os.system('adb root')

    cmd = 'adb shell input tap {} {}'.format(x,y)
    print(cmd)
    os.system(cmd)

    recordcmd='TOUCH|{\'x\':%d,\'y\':%d,\'type\':\'downAndUp\',}' % (x,y)
    f.write(recordcmd+"\n")

def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'shell input swipe 320 410 320 410 ' + str(press_time)
    print(cmd)
    os.system(cmd)


def update_data():
    global src_x, src_y
    global f

    f = open('./myQQ.mr', 'a')
    img = cv2.imread('./autojump.png')
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    return img

def updatefig(*args):
    global update
    global f

    if update:
        time.sleep(1)
        pull_screenshot()
        im.set_array(update_data())

        recordcmd = 'WAIT|{\'seconds\':1.0,}'
        f.write(recordcmd + "\n")

        update = False
    return im,


def on_click(event):
    global update    
    global src_x, src_y
    global f

    # 当前屏幕的点击坐标
    dst_x, dst_y = event.xdata, event.ydata
    dst_x=int(dst_x)
    dst_y=int(dst_y)

    tap(dst_x,dst_y)

    update = True

if __name__ == '__main__':
    # 准备画布
    fig = plt.figure()
    # 将屏幕截图拷贝到当前路径下
    pull_screenshot()
    img = update_data()
    im = plt.imshow(img, animated=True)
    update = True

    fig.canvas.mpl_connect('button_press_event', on_click)
    ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)
    plt.show()

