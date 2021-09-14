# -*- encoding: utf-8 -*-
'''
@File    :   wallpaper.py
@Time    :   2021/09/14 12:10:22
@Author  :   Rpeng 
@Version :   1.0
@Contact :   rpeng252@gmail.com
'''

import requests
import datetime
import win32api,win32con,win32gui
import os


def GetWallpaper():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    url = 'https://cn.bing.com/th'
    params = {
        'id': 'OHR.Aldeyjarfoss_ZH-CN0106567013_UHD.jpg',
        'rf': 'LaDigue_UHD.jpg',
        'w': '3840',
        'h': '2160',
        'c': '8',
        'rs': '1',
        'o': '3',
        'r': '0'
    }
    response = requests.get(url,headers=headers,params=params)

    time_now = datetime.datetime.now().strftime('%Y-%m-%d')
    path = f'Wallpaper{time_now}.bmp'

    with open(path,'wb') as file:
        file.write(response.content)
    return os.path.abspath(path)

def SetUp(path):
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")

    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path, win32con.SPIF_SENDWININICHANGE)

if __name__ == '__main__':
    path = GetWallpaper()
    SetUp(path)