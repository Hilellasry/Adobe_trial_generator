import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc
import time
import random
import string
import pyperclip





#start webdriver
os.startfile("chromedriver_win32\\chromedriver.exe")


driver = uc.Chrome(headless=False,use_subprocess=False)
mail = "hosev81245@getmola.com"
password = "ABCabc1234"
#driver.get("C:\\Users\\hilellasry\\Downloads\\verification code.html")
#input


#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "col-box"))).click()

#driver.get(mail_link)
#WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "inbox-data-content-intro")))
verification_code = 123456

for i in range(6):
    print(i)
    print(str(f'[data-id="CodeInput-{i}"]'))
    print(str(f":input.spectrum-Textfield.CodeInput-Digit[data-id='CodeInput-{str(i)}']"))

    print(str(verification_code)[i])
print(verification_code)
time.sleep(100)