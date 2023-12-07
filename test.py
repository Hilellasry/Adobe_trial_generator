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
driver.get("https://auth.services.adobe.com/en_IL/deeplink.html?deeplink=signup&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2Fcommerce_apps_amsterdam_client%2FAdobeID%2Fcode%3Fredirect_uri%3Dhttps%253A%252F%252Fcommerce.adobe.com%252Fbusiness-trial%252Fsign-up%252Fconfirmation%253Fappims%253D1%2526ppc%253D1%26state%3D%257B%2522ac%2522%253A%2522commerce.adobe.com%2522%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=commerce_apps_amsterdam_client&scope=AdobeID%2Copenid%2Cadditional_info.roles%2Cread_organizations&state=%7B%22ac%22%3A%22commerce.adobe.com%22%7D&relay=a3b2591b-ee03-414c-9f39-d9026944f56f&locale=en_IL&flow_type=code&puser=boroxo8235%40getmola.com&fnuser=ipdpg&lnuser=rduq&pcountry=IL&eu=true&enforce_country=true&ctx_id=cc-business-trials-2020&dctx_id=v%3A2%2Ch%2Cf%2C971043b0-954d-11ee-b99e-6b2a1bcce575&idp_flow_type=create_account&dl=true&s_p=google%2Cfacebook%2Capple&response_type=code&code_challenge_method=plain&redirect_uri=https%3A%2F%2Fcommerce.adobe.com%2Fbusiness-trial%2Fsign-up%2Fconfirmation%3Fappims%3D1%26ppc%3D1&use_ms_for_expiry=true#/signup/2")
#input


driver.find_element(By.NAME, "password").send_keys(password)
time.sleep(0.8)
driver.find_element(By.NAME, "submit").click()
try:
    myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
driver.find_element(By.ID, "Signup-DateOfBirthChooser-Month-value").click()
driver.find_element(By.CSS_SELECTOR, ".spectrum-Menu-item:nth-child(4) > .spectrum-Menu-itemLabel").click()
driver.find_element(By.ID, "react-spectrum-112").send_keys(random.randint(1990, 2001))


time.sleep(10)