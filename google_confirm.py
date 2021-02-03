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
def get_conf_sms(sender):
  # account credentials
  username = "davi123dtran123@gmail.com"
  password = "Mur9fKfTi2nU"
  # create an IMAP4 class with SSL 
  imap = imaplib.IMAP4_SSL("imap.gmail.com")
  # authenticate
  imap.login(username, password)
  got_email=False
  while not got_email:
      sleep(10)
      status, messages = imap.select("INBOX")
      # number of top emails to fetch
      N = 100
      # total number of emails
      messages = int(messages[0])
      print('messages',messages)
      for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
          if isinstance(response, tuple):
              # parse a bytes email into a message object
              msg = email.message_from_bytes(response[1])
              # decode the email subject
              subject = decode_header(msg["Subject"])[0][0]
              if isinstance(subject, bytes):
                  # if it's a bytes, decode to str
                  subject = subject.decode()
              # decode email sender
              From, encoding = decode_header(msg.get("From"))[0]
              if isinstance(From, bytes):
                  From = From.decode(encoding)
              print("Subject:", subject)
              print("From:", From)
              # subject_sample = "Nouveau SMS à SIM №1 (Transférez les SMS vers votre PC/téléphone application)"  ---------this is for domino sms forwarder
              # from_sample = "<no-reply-smsforwarder@cofp.ru>"
              subject_sample = "Weiterleitung aus Gmail - E-Mail-Empfang"
              from_sample = "forwarding-noreply@google.com"
              
              print(subject.find(subject_sample))
              print(From.find(from_sample))
              # input('1')
              if subject.find(subject_sample)>-1:
                # input('2')
                if From.find(from_sample)>-1:
                  # input('3')
                  if subject.find(sender)>-1:
                    print(sender)
                    # with open('dd.txt','w') as dd:
                      # dd.write(str(msg))
                  sss = subject.split('(')[1]
                  sms = sss.split(')')[0].strip()
                  # sms = ss.split('est')[0].strip()
                  print("sms",sms)
                  # input(sms)
                  return sms
  imap.close()
  imap.logout()
# get_conf_sms('dfd')