from pyautogui import *
from time import sleep
print('start')
_pSettingsError_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/ProxyError.png')
print(_pSettingsError_)
# _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
# while not _pSettingsMain_ == None:
#   print(_pSettingsMain_)
#   _pSettingsMain_location_ = center(_pSettingsMain_)
#   print(_pSettingsMain_)
#   _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
#   x = int(_pSettingsMain_.left) + 8
#   y = int(_pSettingsMain_.top) + 8
#   click(x,y)
#   sleep(2)
#   _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
# sleep(3)

# _pSettingsNext1_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsNext1.png')
# while not _pSettingsNext1_ == None:
#   print(_pSettingsMain_)
#   _pSettingsNext1_location_ = center(_pSettingsNext1_)
#   print(_pSettingsNext1_)
#   _pSettingsNext1_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsNext1.png')
#   click(_pSettingsNext1_location_)