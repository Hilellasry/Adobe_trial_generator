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
driver.get("https://temp-mail.org/en/")
#input

#WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "col-box"))).click()
try:
    # Use explicit wait to wait for the presence of the element
    elements = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "viewLink"))
    )

    # Scroll to and click on each element directly
    for element in elements:
        # Scroll to the element
        ActionChains(driver).move_to_element(element).perform()

        # Click on the element
        element.click()

except Exception as e:
    print(f"An error occurred: {str(e)}")
    # Add additional logging or error handling as needed
time.sleep(10)