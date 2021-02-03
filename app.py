from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver=webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://stackoverflow.com/users/login')
sleep(1)
sfg=driver.find_element_by_class_name('s-btn__google')
sfg.click()
wait=WebDriverWait(driver,10)
email_box=wait.until(EC.presence_of_element_located((By.ID,'identifierId')))
email_box.send_keys('henri639760@gmail.com')
btn=driver.find_element_by_class_name('VfPpkd-Jh9lGc')
btn.click()


# s-btn__google
input('wait')

