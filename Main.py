import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, ElementNotInteractableException
import urllib.request
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import random
import string
import pyperclip


password = "1234Abcd"


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
driver.get("https://maildrop.cc/")
driver._switch_to.window("tempmailtab")

time.sleep(0.5)
driver.find_element(By.XPATH,"//*[@id='gatsby-focus-wrapper']/div/section[1]/div/div[2]/div[2]/div/div[2]/div[2]/button").click()

mail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='gatsby-focus-wrapper']/div/main/div/div[1]/div/div/div[1]/div[2]/a"))).get_attribute("href").split(":")[1]

#print(temp_mail)
#mail = pyperclip.paste()
print(mail)


driver._switch_to.window("adobetab")
driver.get("https://commerce.adobe.com/business-trial/sign-up?items%5B0%5D%5Bid%5D=D88531E5A20E1D8D87D1E1308E6F4ADE&cli=adobe_com_cct&lang=en&co=US&promoid=RBS7NL39&mv=other%2Caffiliate&mv2=red&sid=78654bee-de13-463f-89bb-a900cc257fe2")
#input---------------------------------------------------

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
time.sleep(0.1)
#Phone
driver.find_element(By.NAME, "businessPhone").send_keys(str(random.sample(range(0, 9), 7)))

#continue 
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID, "TrialsForm__continueButton__3RMjG"))

driver.find_element(By.ID, "TrialsForm__continueButton__3RMjG").click()
#ActionChains(driver).move_to_element(continue_button).click()


#wait for page to load
try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#password
driver.find_element(By.NAME, "password").send_keys(password)
time.sleep(2)
driver.find_element(By.NAME, "submit").click()

#wait for page to load
try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

#month
driver.find_element(By.ID, "Signup-DateOfBirthChooser-Month-value").click()


#YEAR
driver.find_element(By.CSS_SELECTOR, ".spectrum-Menu-item:nth-child(4) > .spectrum-Menu-itemLabel").click()
driver.find_element(By.NAME, "bday-year").send_keys(random.randint(1990, 2004))
driver.find_element(By.NAME, "submit").click()

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.spectrum-Textfield.CodeInput-Digit[data-id='CodeInput-0']")))

driver._switch_to.window("tempmailtab")


#refresh mailbox
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".order-2").click()

#get verifiction code
driver.switch_to.frame(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'iframe'))))

verification_code = ''.join(filter(str.isdigit, driver.find_element(By.CSS_SELECTOR, "strong").text))
print(verification_code)
driver.switch_to.default_content()


time.sleep(0.1)
driver._switch_to.window("adobetab")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.spectrum-Textfield.CodeInput-Digit[data-id='CodeInput-0']")))
for i in range(6):
    print(i)
    driver.find_element(By.CSS_SELECTOR, str(f"input.spectrum-Textfield.CodeInput-Digit[data-id='CodeInput-{str(i)}']")).send_keys(str(verification_code)[i])


try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
print(driver.find_element(By.XPATH, "/html/body").text)
