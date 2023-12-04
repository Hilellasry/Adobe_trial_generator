import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
from selenium.webdriver.common.keys import Keys
import time
import pyperclip





#start webdriver
os.startfile("chromedriver_win32\\chromedriver.exe")


driver = webdriver.Chrome()
#driver.maximize_window()
driver.execute_script("window.open('about:blank', 'adobetab');")
driver._switch_to.window("adobetab")
#driver.get("https://commerce.adobe.com/business-trial/sign-up?items%5B0%5D%5Bid%5D=D88531E5A20E1D8D87D1E1308E6F4ADE&cli=adobe_com_cct&lang=en&co=US&promoid=RBS7NL39&mv=other%2Caffiliate&mv2=red&sid=78654bee-de13-463f-89bb-a900cc257fe2")
print(driver.title)
driver.execute_script("window.open('about:blank', 'tempmailtab');")
driver._switch_to.window("tempmailtab")
driver.get("https://temp-mail.org/en/")
driver._switch_to.window("tempmailtab")
wait = WebDriverWait(driver, timeout=20)
wait.until(EC.text_to_be_present_in_element(By.ID,"mail"), "@")
mail = driver.find_element(By.ID,"mail").text
#print(temp_mail)
#mail = pyperclip.paste()
print(mail)

#if(driver.title != "Business Trial Sign Up"):
   # print("ERROR: the adobe webstie been enable to load" + " your website is:" + driver.title)

driver.find_element(By.NAME, "lastName").send_keys("hihihi")

time.sleep(10)