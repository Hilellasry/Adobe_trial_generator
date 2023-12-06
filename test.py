import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException
import urllib.request
from selenium.webdriver.common.keys import Keys
import time
import random
import string
import pyperclip





#start webdriver
os.startfile("chromedriver_win32\\chromedriver.exe")


driver = webdriver.Chrome()
mail = "mepine6551@mcenb.com"
driver.get("https://commerce.adobe.com/business-trial/sign-up?items%5B0%5D%5Bid%5D=D88531E5A20E1D8D87D1E1308E6F4ADE&cli=adobe_com_cct&lang=en&co=US&promoid=RBS7NL39&mv=other%2Caffiliate&mv2=red&sid=78654bee-de13-463f-89bb-a900cc257fe2")
#input
#mail
driver.find_element(By.NAME, "email").send_keys(mail)

#firsname
driver.find_element(By.NAME, "firstName").send_keys( ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3, 7))))

#lastname
driver.find_element(By.NAME, "lastName").send_keys( ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3, 7))))

#companyName
driver.find_element(By.NAME, "companyName").send_keys( ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3, 7))))

#companySizeField
driver.find_element(By.ID, "companySizeField").click()
driver.find_element(By.CSS_SELECTOR, ".spectrum-Menu-item:nth-child(1) > .spectrum-Menu-itemLabel").click()

#countryField
driver.find_element(By.ID, "countryField").click()
driver.find_element(By.CSS_SELECTOR, ".spectrum-Menu-item:nth-child(37) > .spectrum-Menu-itemLabel").click()

#Phone
driver.find_element(By.NAME, "businessPhone").send_keys(random.sample(range(0, 9), 7))


