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
driver.implicitly_wait(5)

# 원하는 날짜 넣기
sedate = ("2022-04-23", "2022-04-30", "2022-05-05", "2022-05-06", "2022-05-07", "2022-05-14")

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

        time.sleep(random.uniform(10, 60))  # 10~60초 사이 랜덤으로 쉼
        driver.refresh()

    if data :
        break


# import os
# import time
# import telegram 
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options

# # ------- 신규
# options = Options()
# chrome_driver = os.path.join('chromedriver')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')               # headless
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(chrome_driver, options=chrome_options)
# options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
# driver.implicitly_wait(2)

# # 뒤에 날짜만 넣으면 됨
# url = 'https://imjingakcamping.co.kr/resv/res_01.html?checkdate=2022-04-26'
# driver.get(url)

# html = driver.find_element_by_css_selector('#tableRemainTbody').get_attribute('innerHTML') # 전체 구조도
# soup = BeautifulSoup(html, 'html.parser')
# data = [] # 원하는 자리 담기
# while True:
#     for ele in soup.find_all('span',limit=2):
#         a = ele.get_text()
#         num = int(a)
#         print(num)
    
#         if num >= 1 :
#             data.append(num)
#     if data:
#         print("자리 났음!! 종료")
#         bot = telegram.Bot(token='5379588207:AAFanpXE3ts0mVstRUCOdUL8tHIdsrEVv5w')
#         chat_id = 5354867788
#         bot.sendMessage(chat_id=chat_id, text="자리 났음!! 종료") 
#         driver.quit() # 드라이버 완전히 종료. 창 하나만 닫으려면 .close()
#         break
    
#     # 180초마다 새로고침하여 반복
#     time.sleep(180)
#     driver.refresh()










# import time
# import telegram
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# # ------- 신규
# chrome_driver = os.path.join('chromedriver')
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')               # headless
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
# driver = webdriver.Chrome(chrome_driver, options=chrome_options)
# driver.implicitly_wait(2)

# # 원하는 날짜 넣기
# sedate=("2022-04-27")

# while True :
#     for i in sedate :
#         url = 'https://imjingakcamping.co.kr/resv/res_01.html?checkdate='+i
#         driver.get(url)
#         print(url)
#         html = driver.find_element(By.CSS_SELECTOR,'#tableRemainTbody').get_attribute('innerHTML')
#         soup = BeautifulSoup(html, 'html.parser')
#         data = [] # 원하는 자리 담기
#         for ele in soup.find_all('span',limit=2):
#             a = ele.get_text()
#             num = int(a)
#             print(num)
#             if num >= 1 :
#                 data.append(num)
#         if data:
#             print("자리 났음!! 종료")
#             bot = telegram.Bot(token='5379588207:AAFanpXE3ts0mVstRUCOdUL8tHIdsrEVv5w')
#             chat_id = 5354867788
#             bot.sendMessage(chat_id=chat_id, text=i+ " 자리 났음! 빨리 예약하세요!")
#             driver.quit() # 드라이버 완전히 종료. 창 하나만 닫으려면 .close()
#             break
#         # 각 날짜별 인터벌 3초
#         time.sleep(3)
#         driver.refresh()
#     # 새로고침 10초
#     time.sleep(10)
#     driver.refresh()
 
