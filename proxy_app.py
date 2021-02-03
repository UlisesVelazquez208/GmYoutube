from pywinauto.application import Application
from pywinauto import keyboard
from bs4 import BeautifulSoup
from faker import Faker
import names
import base64
fake = Faker('en_US')
import os
import sys
import platform
from time import sleep
from datetime import datetime
import time
import json
import csv
from random import *
import string
import random
from pywinauto import *
from pyautogui import *
import requests

import datetime
from anticaptchaofficial.recaptchav2proxyless import *
from random import randint ,choice

import imaplib
import pprint
import email
from email.header import decode_header
import webbrowser
import wmi 

def change_vpn_ip():
# # wifi_netflix = 'Livebox-3DB6'
# # change_wifi(wifi_netflix)
# # sleep(3)
# # input('wifi chagned')
# # proxy = 'p.appcloud.digital:9999'   
# # options.add_argument('--proxy-server=socks5://' + proxy)
  sleep(2)
  sleep(2)
  try:
    os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
    app = Application().start('C:\\3.26\\Client.exe')
    sleep(2)
    w = app.top_window()
    w.set_focus()
    sleep(2)
    sleep(1)
    w.set_focus()
    sleep(0.5)
    user_id = 'olorus'
    password = 'gP2{^}5yY4htLS'
    w.set_focus()
    sleep(0.3)
    for i in range(15):
      sleep(0.1)
      keyboard.send_keys('{DELETE}')
    sleep(2)
    w.set_focus()
    sleep(0.3)
    keyboard.send_keys(user_id)
    sleep(1)
    w.set_focus()
    sleep(0.3)
    keyboard.send_keys('{TAB 1}')
    sleep(1)
    for i in range(15):
      sleep(0.1)
      keyboard.send_keys('{DELETE}')
    sleep(1)
    w.set_focus()
    sleep(0.3)
    keyboard.send_keys(password)
    sleep(1)
    w.set_focus()
    sleep(0.2)
    keyboard.send_keys('{TAB 1}')
    keyboard.send_keys('{TAB 1}')
    sleep(1)
    w.set_focus()
    sleep(0.2)
    keyboard.send_keys('{ENTER 2}')
    sleep(1)
    sleep(2)
    sleep(1)
    try:
      app_b = Application().connect(path='annoucement.exe')
      w_b = app_b.top_window()
      w_b.close()
      sleep(1)
    except:
      pass
    sleep(2)
    sleep(1)
  except:
    pass
  sleep(2)
  # os.popen('"C:/Users/olorus/Downloads/3.26/ProxyTool/AutoProxyTool.exe" -changeproxy/PT')
  sleep(3)
  sleep(2)
  app1 = Application().connect(path='Client.exe')
  w1 = app1.top_window()
  w1.set_focus()
  sleep(2)
  w1.set_focus()
  os.popen('"C:/3.26/ProxyTool/AutoProxyTool.exe" -changeproxy/CH')
  print('done proxy ip change')
  sleep(3)
  # os.popen('"C:/3.26/ProxyTool/AutoProxyTool.exe" -changeproxy/PT')
  # sleep(3)
  sleep(2)
  sleep(1)
# change_vpn_ip()