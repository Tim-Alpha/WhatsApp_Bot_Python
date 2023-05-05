import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
import time
import sys
import os

RESULT = True

url = 'https://iop.ignouonline.ac.in/announcements/0'

R = requests.get(url)
htmlContent = R.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)

# -------------------------------------------
        # Checking for new data
# -------------------------------------------
table = soup.find('table')
# print(table.get_text())
tableBody = table.find('tbody')
newNotification = tableBody.find('tr')

NEW_NOTICE_INDEX = 0
with open('counter.txt','r', encoding='utf8') as f:
    NEW_NOTICE_INDEX = f.read()
    NEW_NOTICE_INDEX = int(NEW_NOTICE_INDEX)
# print(NEW_NOTICE_INDEX)

notice = f"notice{NEW_NOTICE_INDEX}"
NOTICE_INDEX = newNotification.find('div', id= notice)

# print(NOTICE_INDEX)

if NOTICE_INDEX == None:
    RESULT = False
    print('Sorry!!')
    os.system('exit')
else:
    RESULT = True

# -------------------------------------------
        # Checking end
# -------------------------------------------
if RESULT:
    notification = newNotification.get_text()
    # print(newNotification.get_text().strip())
    link = newNotification.find('a')
    newLink = link['href']

    Message = f'''
        Hey Everyone,

        {notification}

        Click here : {newLink}

        Thanks and Regards
        Admin Bot
        \n


    '''
    # print(Message)
if RESULT:
# -----------------------------------------------
#       Increasing index by + 1
# -----------------------------------------------
    with open('counter.txt','w', encoding='utf8') as f:
        NEW_NOTICE_INDEX += 1
        f.write('{}' .format(NEW_NOTICE_INDEX))

# -----------------------------------------------
#       Sending message to WhatsApp Community
# -----------------------------------------------

    CHROME_WHATSAPP_PROFILE = "user-data-dir=C:\\Users\\nikhi\\AppData\\Local\\Google\\Chrome\\User Data\\whatsapp"
    chromedriver_autoinstaller.install()
    option = webdriver.ChromeOptions()
    option.add_argument(CHROME_WHATSAPP_PROFILE)
    driver = webdriver.Chrome(options=option)
    url = "https://web.whatsapp.com/"
    driver.get(url)
    time.sleep(5)

    search_text = "IGNOU STUDENTS COMMUNITY"
    search_path = '//div[@contenteditable="true"][@data-tab="3"]'
    SEARCH = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_path)))
    SEARCH.send_keys(search_text)
    time.sleep(5)
    xpath = f'//span[@title="{search_text}"]'
    OPEN = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    input_path = '//div[@contenteditable="true"][@data-tab="10"]'
    INPUT_MSG = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_path)))
    INPUT_MSG.send_keys(Message)
    time.sleep(5)
    driver.quit()

os.system('exit')