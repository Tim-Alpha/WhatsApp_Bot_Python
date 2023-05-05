from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import sys
import os

CHROME_WHATSAPP_PROFILE = "user-data-dir=C:\\Users\\nikhi\\AppData\\Local\\Google\\Chrome\\User Data\\whatsapp"
chromedriver_autoinstaller.install()
option = webdriver.ChromeOptions()
option.add_argument(CHROME_WHATSAPP_PROFILE)
driver = webdriver.Chrome(options=option)

RESULT = True

IGNOU_URL = "https://iop.ignouonline.ac.in/announcements/0"
driver.get(IGNOU_URL)


NEW_NOTICE_INDEX = 0
with open('counter.txt','r', encoding='utf8') as f:
    NEW_NOTICE_INDEX = f.read()
    NEW_NOTICE_INDEX = int(NEW_NOTICE_INDEX)

EYE1 = f"preview{NEW_NOTICE_INDEX}"


try:
    NOTICE_EYE = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, EYE1))).click()
    os.system('cls')
except Exception as e:
    RESULT = False
    Message = f"Sorry! no new notice yet{Keys.SHIFT}{Keys.ENTER}{Keys.SHIFT}{Keys.ENTER}"

driver.close()

if RESULT:
    Message = f'''Dear friends
    One new notice recived
    Please check the website : https://iop.ignouonline.ac.in/announcements/0 
    Thanks and Regards
    Admin Bot
    {Keys.SHIFT}{Keys.ENTER}   
    {Keys.SHIFT}{Keys.ENTER}

    {Keys.SHIFT}{Keys.ENTER}
    
    '''

    with open('counter.txt','w', encoding='utf8') as f:
        NEW_NOTICE_INDEX += 1
        f.write('{}' .format(NEW_NOTICE_INDEX))


if RESULT:
    CHROME_WHATSAPP_PROFILE = "user-data-dir=C:\\Users\\nikhi\\AppData\\Local\\Google\\Chrome\\User Data\\whatsapp"
    chromedriver_autoinstaller.install()
    option = webdriver.ChromeOptions()
    option.add_argument(CHROME_WHATSAPP_PROFILE)
    driver = webdriver.Chrome(options=option)
    url = "https://web.whatsapp.com/"
    driver.get(url)
    # time.sleep(1)

    search_text = "IGNOU STUDENTS COMMUNITY"
    search_path = '//div[@contenteditable="true"][@data-tab="3"]'
    SEARCH = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_path)))
    SEARCH.send_keys(search_text)
    # time.sleep(1)
    xpath = f'//span[@title="{search_text}"]'
    OPEN = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    input_path = '//div[@contenteditable="true"][@data-tab="10"]'
    INPUT_MSG = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_path)))
    INPUT_MSG.send_keys(Message)
    # time.sleep(1)

driver.quit()