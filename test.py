from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

# driver = webdriver.Chrome('chromedriver.exe')

# ------- 신규
chrome_driver = os.path.join('chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')               # headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


# driver.implicitly_wait(1)
# driver = webdriver.Chrome(options=options)

url = 'https://imjingakcamping.co.kr/resv/res_01.html?checkdate=2022-04-26'
driver.get(url)

from bs4 import BeautifulSoup
import time
import telegram
from selenium.webdriver.chrome.options import Options



# html = driver.find_element(BY.ID, 'tableRemainTbody').get_attribute('innerHTML') # 전체 구조도
html = driver.find_element_by_css_selector('#tableRemainTbody').get_attribute('innerHTML') # 전체 구조도

soup = BeautifulSoup(html, 'html.parser')
data = [] # 원하는 자리 담기

while True:
    for ele in soup.find_all('span',limit=2):
        a = ele.get_text()
        num = int(a)
        print(num)
    # 원하는 자리 났을 경우, 리스트에 자리와 색 넣기
        if num >= 1 :
            data.append(num)

    if data:
        print("자리 났음!! 종료")

        bot = telegram.Bot(token='5379588207:AAFanpXE3ts0mVstRUCOdUL8tHIdsrEVv5w')
        chat_id = 5354867788
        bot.sendMessage(chat_id=chat_id, text="자리 났음!! 종료") 

        driver.quit() # 드라이버 완전히 종료. 창 하나만 닫으려면 .close()
        break

    # 10초마다 새로고침하여 반복

    time.sleep(10)
    driver.refresh()



