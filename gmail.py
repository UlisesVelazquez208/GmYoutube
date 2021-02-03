from pyautogui import *
from time import sleep
import requests
from random import randint ,choice
from clipboard import copy,paste
import string
import csv
import base64
import imaplib
import string
import email
from email.header import decode_header
from time import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json
import win32clipboard
from csv import reader
# from time import sleep
from anticaptchaofficial.recaptchav2proxyless import *
from random import randint ,choice
from datetime import date
from google_confirm import *
from proxy_app import *
chrome_options = Options()

# import requests
from bs4 import BeautifulSoup
api_key='3296ab32h9b3rvb4bkxjiuub8eqv3mpl73trerjwurjwtbw7fkus0yq5thjh'
# get_numbers='https://en.sms-online.pro/api/orders/create/444?api_token={}'.format(api_key)
# get_avl='https://sms-online.pro/api/countriesbyservice?service=444&api_token={}'.format(api_key)
get_avl_2='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=getNumbersStatus&country={}'.format(api_key,78)
# ordr1='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=getNumber&service=go&&country=78'.format(api_key)
# get_status='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=getStatus&id={}'.format(api_key,80679501)
countries={}
cntf=open('countries.csv','r')
cnts=csv.DictReader(cntf)

for cnt in cnts:
  if cnt['status'].strip()=='1':
    countries[cnt['country_code']]=cnt['country_name']

b=int(input('number of gmails:-'))
# b = 2

chrome_options = Options()  
# chrome_options.add_argument("--headless")  

def remove_tv_screens():

  _tv_screen_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_9.png')
  while not _tv_screen_ == None:
    print(_tv_screen_)
    _tv_location_ = center(_tv_screen_)
    print(_tv_location_)
    _ok_button_=locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_10.png')
    while not _ok_button_ == None:
      _location_ok = center(_ok_button_)
      print(_ok_button_)
      print(_location_ok)
      sleep(1)
      click(_location_ok)
      _tv_screen_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_9.png')
      _ok_button_=locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_10.png')
  print('removed all tv screens!!')

def remove_intell_screens():

  _combo_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_8.png')
  while not _combo_ == None:
    sleep(1)
    print(_combo_)
    _combo_location_ = center(_combo_)
    print(_combo_location_)
    sleep(1)
    x = _combo_.left + 15
    y = _combo_.top + 15
    click(x,y)
    sleep(2)
    _combo_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_8.png')
  print('removed combo screen')

def remove_next_b_screens():

  _Next_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next_button.png')
  while not _Next_button_ == None:
    sleep(1)
    print(_Next_button_)
    __Next_button__location_ = center(_Next_button_)
    print(__Next_button__location_)
    sleep(1)
    click(__Next_button__location_)
    sleep(2)
    _Next_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next_button.png')
  print('removed Next_button screen')

def remove_next_2_screens():

  _Next2_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/next_2.png')
  while not _Next2_button_ == None:
    sleep(1)
    print(_Next2_button_)
    __Next2_button__location_ = center(_Next2_button_)
    print(__Next2_button__location_)
    sleep(1)
    click(__Next2_button__location_)
    sleep(2)
    _Next2_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/next_2.png')
  print('removed Next_button screen')

def click_reload():

  _reload_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/reload.png')
  while not _reload_button_ == None:
    sleep(1)
    print(_reload_button_)
    _reload_button__location_ = center(_reload_button_)
    print(_reload_button__location_)
    sleep(1)
    click(_reload_button__location_)
    sleep(3)
    click(1000,500)
    _reload_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/reload.png')
  print('removed Next_button screen')

def connect(name, SSID):
    if platform.system() == "Windows":
        command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
    elif platform.system() == "Linux":
        command = "nmcli con up "+SSID
    print(os.system(command))
    print('Changed to ',name)

def check_wifi():
  
  import subprocess
  output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode('utf8', errors ='ignore')
  
  for line in output.split('\n'):
    if line.lower().strip().startswith('ssid'):
      return line.split(':')[1].strip()

def change_wifi(target):
  moveTo(x=1761,y=1060,duration=1)
  sleep(1)
  click(x=1761,y=1060)
  sleep(0.5)
  click(x=1761,y=1060)
  sleep(1)
  wifi = ['Domino-Free','Livebox-3DB6']
  current_wifi = check_wifi()
  # pass_domino = '22759976'
  # pass_livebox = 'szW3GmK6sUr4juWDks'
  # ssid_domino = 'Domino-Free'
  # ssid_livebox = 'Lenovo-3D86'
  sleep(1)
  if current_wifi == target:
    print('Current wifi is : {}'.format(target))
    # connect('Livebox-3DB6','Livebox-3DB6')
    return True
  else:
    wifi.remove(target)
    print('Current wifi is :'+wifi[0])
    while True:
      connect(target,target)
      connect(target,target)
      sleep(2)
      if check_wifi() == target:
        break
    return True
def get_captcha():
  print('\n>>> Getting Captcha Start\n')
  start=time.time()
  while True:
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("9f9bac30e4b573982c4161238d5cf010")
    solver.set_website_url("https://web.onoff.app/login")
    solver.set_website_key("6LcdKygUAAAAAGyosR7wOJr0y1StdqrHdndXVWWG")

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
      print('\n>>> Getting Captcha End\t{} seconds\n '.format(time.time()-start))
      return g_response
    else:
      continue
def get_phone_list():
  phone_list = []
  with open('accounts.csv', 'r') as read_obj:
      # pass the file object to reader() to get the reader object
      csv_reader = reader(read_obj)
      # Iterate over each row in the csv using reader object
      for row in csv_reader:
          # row variable is a list that represents a row in csv
          try:
            if(row[3]==date.today()):
              print(row[3],date.today())
              phone_list.append(row[4])
          except:
            pass
  return phone_list
def get_a_new_number():
  global countries
  cl=list(countries.keys())
  default_country='78'
  default_country=choice(cl)
  while True:
    print('\n>>> Choosing country:- \t {}'.format(countries[str(default_country)]))
    ordr1='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=getNumber&service=go&&country={}'.format(api_key,default_country)
    r=requests.get(get_avl_2)
    # print(r.text)
    # input('proceed')
    r=requests.get(ordr1)
    print("r.text",r.text)
    if 'NO_NUMBER' in r.text:
      print('No new numbers on sms-online')
      default_country=choice(cl)

      continue

    return r.text.split(':')
def get_otp(id):
  get_status='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=getStatus&id={}'.format(api_key,id)
  max_retry=10
  retry=0
  while retry < max_retry:
    retry+=1
    r=requests.get(get_status)
    print(r.text)
    if 'STATUS_CANCEL' in r.text:
      return False
    if 'STATUS_OK' in r.text:
      return r.text.split(':')[-1]
    if retry==7:
      set_status='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=setStatus&status={}&id={}'.format(api_key,8,id)
      r=requests.get(set_status)
      sleep(1)
      print('order is cancelled in def_func')
      return False
    sleep(6)
  return False
def get_latest_otp(last_otp=''):
  global driver_onff
  driver_onff.get('https://web.onoff.app/messages')
  sleep(5)
  max_retry=8
  retry=0
  while retry < max_retry:
    msgs=driver_onff.find_elements_by_class_name('ThreadItem_excerpt__2iqRc')
    retry+=1
    for msg in msgs:
      if "G-" in msg.text.strip()[:3]:
        latest_otp = msg.text.strip().split("G-")[1].split(" ")[0]
        if latest_otp==last_otp:
          
          print('No new otp checking after 5 seconds')
          break
        return latest_otp
  return False

def on_off_login(email,password):
  global driver_onff
  driver_onff.get('https://web.onoff.app/login')
  sleep(10)
  email_box=driver_onff.find_element_by_name('email')
  password_box=driver_onff.find_element_by_name('password')
  email_box.send_keys(email)
  password_box.send_keys(password)
  token=get_captcha()
  script2='''document.getElementById("g-recaptcha-response").style.display = "block"; document.getElementById("g-recaptcha-response").innerHTML="{}";'''.format(token.strip())
  driver_onff.execute_script(script2)
  # script='''$('button[type="submit"]').click();'''
  # script='''document.getElementByTagName('button').click();'''
  # driver_onff.execute_script(script)
  driver_onff.find_element_by_css_selector("form>button").click()
  sleep(2)
  print('>>>\tLogged in OnOff')
  last_otp=get_latest_otp()
  return last_otp


def get_all_numbers():
  global driver_onff
  numbersl=[]
  soup=BeautifulSoup(driver_onff.page_source,'lxml')
  numbers=soup.find_all('div',{'class':'PhoneCard_category-number__2Qf0S'})
  for number in numbers[1:]:
    print(number.text.strip().replace(' ',''))
    numbersl.append(number.text.strip().replace(' ',''))
  return numbersl


def gen_pass(length):
    letters = string.ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(length))
    return result_str

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def generate_french_name():
  api_url='https://api.namefake.com/french-france/'
  r=requests.get(api_url)
  data=r.json()
  print(data)
  # input('wait')
  return data

def execute_js(js):
  hotkey('ctrl','l')
  sleep(0.3)
  hotkey('ctrl','a')
  sleep(0.3)
  typewrite('javascript')
  sleep(0.3)
  copy(js)
  sleep(0.3)
  hotkey('ctrl','v')
  sleep(0.3)
  typewrite('\n')
  sleep(2)

def create_gmail(pno):
  global last_otp
  # x=get_a_new_number()
  # print(x)
  hotkey('win','r')
  sleep(1)
  hotkey('ctrl','a')
  sleep(1.5)
  write('chrome --profile-directory=profile{}'.format(pno))
  press('enter')
  sleep(5)
  hotkey('win','up')
  clear_url = 'chrome://settings/clearBrowserData'
  copy(clear_url)
  sleep(0.3)
  hotkey('ctrl','l')
  sleep(1)
  hotkey('ctrl','v')
  sleep(0.5)
  typewrite('\n')
  sleep(2)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('tab')
  sleep(0.3)
  press('enter')
  sleep(0.5)
  is_back = 'yes'
  while is_back == 'yes':
    french_id=generate_french_name()
    print(french_id)
    sleep(1)
    # net_error = True
    # while net_error:
    sleep(2)
    hotkey('ctrl','l')
    keyDown('ctrlleft');  typewrite('a'); keyUp('ctrlleft')
    typewrite('accounts.google.com/SignUp')
    sleep(1.2)
    typewrite('\n')
    sleep(20)
    #   _pSettingsError_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/ProxyError.png')
    #   if not _pSettingsError_ == None:
    #     net_error = False
    #   if _pSettingsError_ == None:
    #     change_vpn_ip()
    # # input('wait')
    typewrite(french_id['name'].split(' ')[0])
    sleep(1)
    press('tab')
    typewrite(french_id['name'].split(' ')[-1])
    sleep(1)
    press('tab')
    rno=random_with_N_digits(4)
    typewrite('{}{}'.format(french_id['username'],rno))
    print('email is','{}{}'.format(french_id['username'],rno))
    sleep(2)
    with open('accounts.txt','a') as f:
      f.write('{}{}\n'.format(french_id['username'],rno))
    press('tab')
    sleep(1)
    press('tab')
    password=gen_pass(10)
    typewrite(password)
    print('password is',password)
    sleep(1)
    press('tab')
    typewrite(password)
    sleep(1)
    typewrite('\n')
    sleep(5)
    print('entered to checking part-0')
    sleep(1)
    is_f_screen=''':var dummy1 = document.createElement("input");document.body.appendChild(dummy1);
  y=document.getElementById('username');if(y){dummy1.value ='yes';}else{dummy1.value ='no';}dummy1.select();document.execCommand("copy");setTimeout(()=>{console.log('World!');},2000);document.body.removeChild(dummy1);'''
    hotkey('ctrl','l')
    hotkey('ctrl','a')
    sleep(2)
    typewrite('javascript')
    copy(is_f_screen)
    sleep(0.3)
    hotkey('ctrl','v')
    sleep(0.5)
    typewrite('\n')
    sleep(3)
    is_back = paste()
    sleep(2)
    if is_back == 'yes':
      print('back')
      continue
    # num_d=get_a_new_number()
    # all_numbers=get_all_numbers()
    res='Error'
    use_local_sms = 'True'
    old_id = ''
    while res == 'Error':
      u_time = 'Error'
    
      num_d = get_a_new_number()
      print('num_d',num_d)
      use_local_sms = 'False'
      phone_number = '+{}'.format(num_d[-1].strip())
      sleep(0.5)
      hotkey('win','up')
      sleep(1)
      click(x=1795,y=377,duration=0.5)
      sleep(1)
      click(x=1795,y=377,duration=0.5)
      sleep(1)
      sleep(2)
      hotkey('ctrl','l')
      sleep(0.5)
      press('tab')
      sleep(0.3)
      press('tab')
      sleep(0.5)
      hotkey('ctrl','a')
      sleep(0.4)
      typewrite(phone_number)
      sleep(1)
      typewrite('\n')
      sleep(4)
      sleep(2)
      is_error=''':var dummy = document.createElement("textarea");document.body.appendChild(dummy);
  x=document.getElementsByClassName('o6cuMc');if(x[0]){dummy.value ='Error';}else{dummy.value ='True';}dummy.select();document.execCommand("copy");'''
      hotkey('ctrl','l')
      sleep(1)
      hotkey('ctrl','a')
      sleep(0.5)
      typewrite('javascript')
      copy(is_error)
      hotkey('ctrl','v')
      sleep(0.3)
      typewrite('\n')
      sleep(3)
      res = paste()
      print("res",res)
      if not res == 'True':
        if use_local_sms == 'False':
          set_status='https://sms-online.pro/stubs/handler_api.php?api_key={}&action=setStatus&status={}&id={}'.format(api_key,8,num_d[-2])
          r=requests.get(set_status)
          print('r',r.text) 
        res = 'Error'
        press('tab')
        sleep(1)
        press('tab')
        sleep(1)
        press('tab')
        sleep(1)
        press('tab')
        sleep(1)
        # hotkey('ctrl','a')
      if res == 'True':
        #=======================================================check if first screen==================================
        print('entered to checking part')
        sleep(1)
        is_f_screen=''':var dummy1 = document.createElement("input");document.body.appendChild(dummy1);
    y=document.getElementById('username');if(y){dummy1.value ='yes';}else{dummy1.value ='no';}dummy1.select();document.execCommand("copy");'''
        hotkey('ctrl','l')
        hotkey('ctrl','a')
        sleep(0.5)
        typewrite('javascript')
        copy(is_f_screen)
        sleep(0.3)
        hotkey('ctrl','v')
        sleep(0.3)
        typewrite('\n')
        sleep(3)
        is_back = paste()
        sleep(2)
        if is_back == 'yes':
          print('back')
          break
        #==============================================================================================================
        if use_local_sms == 'True':
          latest_otp=get_latest_otp(last_otp)
        if use_local_sms == 'False':
          print(num_d , "num_d")
          print(num_d[-2],"num_d[-2]")
          latest_otp=get_otp(num_d[-2])
        print(latest_otp)
        if not latest_otp:
          res = 'Error'
          sleep(2)
          c_js=''':document.getElementsByTagName('button')[0].click();'''
          execute_js(c_js)
          sleep(3)
  sleep(5)
  hotkey('ctrl','l')
  sleep(0.5)
  press('tab')
  sleep(0.5)
  typewrite(latest_otp)
  sleep(1)
  typewrite('\n')
  sleep(5)
  last_otp=latest_otp
  with open('last_profile.txt','w') as w:
    w.write('{}'.format(pno))
  sleep(5)
  hotkey('ctrl','a')
  sleep(2)
  press('backspace')
  sleep(2)
  press('tab')
  recoveryemail='franktrace0@gmail.com'
  copy(recoveryemail)
  sleep(0.4)
  day=str(randint(1,28))
  year=str(randint(1990,2000))
  # typewrite(recoveryemail)
  hotkey('ctrl','v')
  sleep(1)
  press('tab')
  sleep(0.1)
  typewrite(day)
  sleep(1)
  sleep(2)
  press('tab')
  sleep(0.1)
  month=randint(1,12)
  for i in range(month):
    press('down')
    sleep(0.1)
  sleep(2)
  press('tab')
  sleep(0.1)
  typewrite(year)
  sleep(2)
  press('tab')
  sleep(0.1)
  gender_d={'male':2,'female':1,'other':3}
  gender=choice(list(gender_d.keys()))
  for i in range(gender_d[gender]):
    press('down')
    sleep(2)
  press('tab')
  sleep(2)
  press('tab')
  sleep(0.3)
  typewrite('\n')
  sleep(1)
  sleep(6)
  
  input_33 = True
  # termsofserviceNext
  #-----------------------check personal settings----------
  sleep(10)
  hotkey('ctrl','l')
  sleep(1)

  js=''':document.getElementsByTagName('input')[33].click();'''
  execute_js(js)
  sleep(3)
  js=''':document.getElementsByTagName('input')[35].click();'''
  execute_js(js)
  sleep(1)

  js=''':document.getElementById('termsofserviceNext').click();'''
  execute_js(js)
  sleep(3)
  # termsofserviceNext,document.getElementById('termsofserviceNext').click();
  js=''':document.getElementById('confirmdialog-confirm').click();'''
  execute_js(js)
  sleep(1)
  sleep(2)
  # input('s')
  _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
  while not _pSettingsMain_ == None:
    print(_pSettingsMain_)
    _pSettingsMain_location_ = center(_pSettingsMain_)
    print(_pSettingsMain_)
    _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
    x = int(_pSettingsMain_.left) + 8
    y = int(_pSettingsMain_.top) + 8
    click(x,y)
    sleep(2)
    _pSettingsMain_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsMain.png')
  sleep(3)

  _pSettingsNext1_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsNext1.png')
  while not _pSettingsNext1_ == None:
    print(_pSettingsMain_)
    _pSettingsNext1_location_ = center(_pSettingsNext1_)
    print(_pSettingsNext1_)
    _pSettingsNext1_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/pSettingsNext1.png')
    input_33 = False
    click(_pSettingsNext1_location_)

  sleep(3)
  hotkey('ctrl','l')
  sleep(1)
  js = ''':document.getElementsByTagName("div")[73].click();'''
  execute_js(js)
  sleep(1)
  sleep(5)

  
  # if not input_33:
    
  # input('s')
  sleep(15)
  #------------------------check popup dialog---------------
  # remove_tv_screens()
  # sleep(2)
  # remove_intell_screens()
  # sleep(1)
  # remove_next_b_screens()
  # sleep(1)
  # remove_next_2_screens()
  # sleep(1)
  # click_reload()

  with open('accounts.csv','a') as f:
    f.write('{},{}{}@gmail.com,{},{},{}\n'.format(pno,french_id['username'],rno,password,date.today(),phone_number))
  sleep(1)
  print('saved as{},{}{}@gmail.com,{},{},{}\n'.format(pno,french_id['username'],rno,password,date.today(),phone_number))
  sleep(25)
  sleep(5)
  hotkey('ctrl','l')
  keyDown('ctrlleft');  typewrite('a'); keyUp('ctrlleft')
  typewrite('mail.google.com/mail/u/0/#inbox')
  sleep(1.2)
  typewrite('\n')
  sleep(5)
  sleep(4)
  sleep(20)

  _inboxError_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/inboxError.png')
  while not _inboxError_ == None:
    sleep(1)
    print(_inboxError_)
    _inboxError_location_ = center(_inboxError_)
    print(_inboxError_location_)
    sleep(5)
    hotkey('ctrl','l')
    sleep(1)
    hotkey('ctrl','a')
    sleep(1)
    copy('mail.google.com/mail/u/0/#inbox')
    sleep(1.2)
    hotkey('ctrl','v')
    sleep(2)
    press('enter')
    sleep(5)
    sleep(14)
    _inboxError_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/inboxError.png')
  print('removed Next_button screen')

  _combo_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_8.png')
  while not _combo_ == None:
    sleep(1)
    print(_combo_)
    _combo_location_ = center(_combo_)
    print(_combo_location_)
    sleep(1)
    x = _combo_.left + 10
    y = _combo_.top + 10
    print(x)
    print(y)
    click(x,y)
    sleep(2)
    _combo_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_8.png')
  print('removed combo screen')
  sleep(3)
  _Next_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next_button.png')
  while not _Next_button_ == None:
    sleep(1)
    print(_Next_button_)
    __Next_button__location_ = center(_Next_button_)
    print(__Next_button__location_)
    sleep(1)
    click(__Next_button__location_)
    sleep(2)
    _Next_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next_button.png')
  print('removed Next_button screen')
  sleep(3)
  _bNext2_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/bNext2.png')
  while not _bNext2_ == None:
    sleep(1)
    print(_bNext2_)
    _bNext2_location_ = center(_bNext2_)
    print(_bNext2_)
    sleep(1)
    click(_bNext2_.left+10,_bNext2_.top+10)
    sleep(2)
    _bNext2_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/bNext2.png')
  print('removed bNext2 screen')
  sleep(3)
  _Next2_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next2.png')
  while not _Next2_button_ == None:
    sleep(1)
    print(_Next2_button_)
    __Next2_button__location_ = center(_Next2_button_)
    print(__Next2_button__location_)
    sleep(1)
    click(__Next2_button__location_)
    sleep(2)
    _Next2_button_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Next2.png')
  print('removed Next2_button screen')
  sleep(3)
  hotkey('ctrl','l')
  sleep(0.3)
  moveTo(535,589)
  sleep(0.5)
  click(535,589)
  sleep(0.5)
  click(535,589)
  sleep(1)
  click(535,615)
  sleep(1)
  click(535,615)
  sleep(10)

  hotkey('ctrl','l')
  sleep(1)
  hotkey('ctrl','a')
  sleep(1)
  copy('mail.google.com/mail/u/0/#settings/fwdandpop')
  sleep(1.2)
  hotkey('ctrl','v')
  sleep(2)
  press('enter')
  sleep(5)
  sleep(24)

  sleep(1)
  hotkey('ctrl','l')
  sleep(0.3)
  moveTo(534,609)
  sleep(0.5)
  click(534,609)
  sleep(0.5)
  click(534,609)
  sleep(1)
  hotkey('ctrl','l')
  sleep(0.3)
  js=''':document.getElementsByTagName('input')[12].click();'''
  execute_js(js)
  sleep(1)
  sleep(1)
  sleep(1)
  sleep(2)
  sleep(5)
  # input('a')
  # js=''':document.getElementById(":3w").value="davi123dtran123@gmail.com";'''
  # execute_js(js)
  copy('davi123dtran123@gmail.com')
  sleep(1)
  hotkey('ctrl','v')
  sleep(2)
  sleep(1)

  js=''':document.getElementsByTagName('button')[6].click();'''
  execute_js(js)
  sleep(2)
  sleep(1)
  sleep(2)
  sleep(5)
  
  _Screenshot_6_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_6.png')
  while not _Screenshot_6_ == None:
    sleep(1)
    print(_Screenshot_6_)
    _Screenshot_6_location_ = center(_Screenshot_6_)
    print(_Screenshot_6_location_)
    sleep(1)
    click(_Screenshot_6_location_)
    sleep(2)
    _Screenshot_6_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/Screenshot_6.png')
  print('removed Next2_button screen')
  sleep(10)
  # hotkey('ctrl','l')
  # sleep(0.3)
  # moveTo(103,162)
  # sleep(0.5)
  # click(103,162)
  # sleep(0.5)
  # click(103,162)
  # sleep(2)
  # sleep(3)
  sleep(5)
  # input('a')
  js=''':document.getElementsByName('ok')[0].click();'''
  execute_js(js)
  sleep(2)
  sleep(2)
  sleep(5)
  # input('a')
  js=''':document.getElementsByTagName('button')[7].click();'''
  execute_js(js)
  sleep(5)
  # (1178,458)
  #----------------------------------get_confirmation code-------------------------------
  # '{},{}{}@gmail.com,{},{},{}\n'.format(pno,french_id['username'],rno,password,date.today(),phone_number)
  otpa = get_conf_sms('ddd')
  print("otpa",otpa)
  sleep(1)
  otp = get_conf_sms('{}{}'.format(french_id['username'],rno))
  sleep(1)
  print('this is otp',otp)
  sleep(2)
  moveTo(930,320)
  sleep(1)
  click(930,320)
  sleep(1)
  click(930,320)
  sleep(7)
  
  _last_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/last.png')
  while not _last_ == None:
    sleep(1)
    print(_last_)
    _last_location_ = center(_last_)
    print(_last_location_)
    sleep(1)
    click(_last_location_)
    sleep(2)
    _last_ = locateOnScreen('C:/Users/PC 6/Desktop/gmail_bot/last.png')
  print('removed Next2_button screen')
  sleep(10)

  # sleep(2)
  sleep(3)
  copy(otp)
  sleep(1)
  hotkey('ctrl','v')
  sleep(1)
  # js=''':var sms=document.execCommand("paste");setTimeout(()=>{document.getElementById(':6d').value=sms;},1000);'''
  # execute_js(js)
  # (895,345)

  sleep(5)
  
  js=''':document.getElementsByName('verify')[0].click();'''
  execute_js(js)
  sleep(1.5)
  sleep(1)
  sleep(5)
  # input('s')
  js=''':document.getElementsByTagName('input')[11].click();'''
  execute_js(js)
  sleep(3)
  
  js=''':document.getElementsByTagName('button')[4].click();'''
  execute_js(js)
  sleep(5)

  hotkey('ctrl','l')
  sleep(1)
  hotkey('ctrl','a')
  sleep(1)
  copy('mail.google.com/mail/u/0/#settings/fwdandpop')
  sleep(1.2)
  hotkey('ctrl','v')
  sleep(2)
  press('enter')
  sleep(5)
  # input('s')
  with open('accounts_forward.csv','a') as f:
    f.write('{},{}{}@gmail.com,{},{},{}\n'.format(pno,french_id['username'],rno,password,date.today(),phone_number))
  sleep(1)
  return True


if __name__ =='__main__':
  # sleep(1)
  # change_wifi('Livebox-3DB6')
  # sleep(1)
  # change_wifi('Domino-Free')
  print('*'*100)
  password='Ana25lol'
  email='tatthan963@gmail.com'
  sleep(2)
  win32clipboard.OpenClipboard()
  win32clipboard.EmptyClipboard()
  win32clipboard.SetClipboardText('testing 123')
  win32clipboard.CloseClipboard()

  # get clipboard data
  win32clipboard.OpenClipboard()
  data = win32clipboard.GetClipboardData()
  win32clipboard.CloseClipboard()
  # last_otp = on_off_login(email,password)
  last_profile_file=open('last_profile.txt','r')
  last_profile=int(last_profile_file.read().strip())+1

  # b=int(input('number of gmails:-'))
  for i in range(last_profile,last_profile+b):
    success=False
    while not success:
      change_vpn_ip()
      success=create_gmail(i)
      # hotkey('alt','f4')
    with open('last_profile.txt','w') as w:
      w.write('{}'.format(i))
    print('Gmail-{} is created successfully!!'.format(i-last_profile+1))

  # driver_onff.quit()
  # javascript:document.getElementsByClassName('VfPpkd-LgbsSe')[1].click();