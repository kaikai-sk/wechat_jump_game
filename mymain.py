import sys
from PIL import Image

from common import screenshot
from common.auto_adb import auto_adb
import aircv as ac
import cv2

if __name__ == '__main__':
    adb = auto_adb()
    adb.test_device()

    contact=ac.imread('C:\\Users\\shankai\\Desktop\\contact.png')
    myfriends=ac.imread('C:\\Users\\shankai\\Desktop\\myfriends.png')

    screenshot.check_screenshot()
    im = screenshot.aircv_pull_screenshot()

    # ‘联系人’按键的位置
    position = ac.find_template(im, contact, 0.1)
    if position!=None:
        x, y = position['result']
        adb.run("shell input tap {} {}".format(x,y))
    # ‘我的好友’按键的位置
    position = ac.find_template(im, myfriends, 0.1)
    if position != None:
        x, y = position['result']
        adb.run("shell input tap {} {}".format(x, y))

    adb.run("shell input tap {} {}".format(x-100, y+150))

    # ‘发消息’按键的位置
    screenshot.check_screenshot()
    im = screenshot.aircv_pull_screenshot()
    sendmessage = ac.imread('C:\\Users\\shankai\\Desktop\\sendmessage.png')
    position = ac.find_template(im, sendmessage, 0.9)
    if position != None:
        x, y = position['result']
        adb.run("shell input tap {} {}".format(x, y))

    # "消息输入框" 按键的位置
    screenshot.check_screenshot()
    im = screenshot.aircv_pull_screenshot()
    text = ac.imread('C:\\Users\\shankai\\Desktop\\text.png')
    position = ac.find_template(im, text, 0.9)
    if position != None:
        x, y = position['result']
        adb.run("shell input tap {} {}".format(x, y))
    adb.run("shell input hello")






