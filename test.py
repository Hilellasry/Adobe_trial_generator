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
import time
import random
import string
import pyperclip





#start webdriver
os.startfile("chromedriver_win32\\chromedriver.exe")


driver = webdriver.Chrome()
mail = "hosev81245@getmola.com"
password = "ABCabc1234"
#driver.get("C:\\Users\\hilellasry\\Downloads\\verification code.html")
#input


#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "col-box"))).click()

#driver.get(mail_link)
#WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, "inbox-data-content-intro")))


driver.get("https://maildrop.cc/inbox/?mailbox=encouraging.dunlin556")
time.sleep(0.5)
#driver.find_element(By.XPATH,"//*[@id='gatsby-focus-wrapper']/div/section[1]/div/div[2]/div[2]/div/div[2]/div[2]/button").click()

#wait for page to load

#mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/main/div/div[1]/div/div/div[1]/div[2]/a"))).get_attribute("href").split(":")[1]


#print(temp_mail)
#mail = pyperclip.paste()
print(mail)

#refresh mailbox
#driver.find_element(By.CSS_SELECTOR, ".order-2").click()

#WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "inbox-data-content-intro")))

#get verifiction code
driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe'))))

verification_code = ''.join(filter(str.isdigit, driver.find_element(By.CSS_SELECTOR, "strong").text))
print(verification_code)
driver.switch_to.default_content()
print(driver.find_element(By.XPATH, "/html/body").text)

#driver.find_element(By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/main/div/div[1]/div/div/div[1]/div[2]/button")