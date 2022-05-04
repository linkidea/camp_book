import os
import random
import time
import telegram
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
chrome_driver = os.path.join('chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
driver = webdriver.Chrome(chrome_driver, options=chrome_options)
driver.implicitly_wait(3)

# 원하는 날짜 넣기
sedate = ("2022-05-05", "2022-05-14", "2022-05-28")

while True :
    for i in sedate:
        url = 'https://imjingakcamping.co.kr/resv/res_01.html?checkdate=' + i
        driver.get(url)
        time.sleep(3)
        print(url)   # -------test-----------

        # html = driver.find_element(By.CSS_SELECTOR, '#tableRemainTbody').get_attribute('innerHTML')
        html = driver.find_element_by_css_selector('#tableRemainTbody').get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        data = []

        for ele in soup.find_all('span', limit=2):
            a = ele.get_text()
            num = int(a)
            print(num)

            if num >= 1:
                data.append(num)
                print(data)   # -------test-----------

        if data:
            print(i + " " + str(data) + " 자리 났음! 종료")
            bot = telegram.Bot(token='5379588207:AAFanpXE3ts0mVstRUCOdUL8tHIdsrEVv5w')
            chat_id = 5354867788
            bot.sendMessage(chat_id=chat_id, text=i + " " + str(data) + " 자리 났음! 빨리 예약하세요!")
            driver.quit()  # 드라이버 완전히 종료. 창 하나만 닫으려면 .close()
            break

        time.sleep(random.uniform(3, 10))  # 3 ~ 10초 사이 랜덤으로 쉼
        driver.refresh()

    if data :
        break

#-----------------------------------------------------------------------------
