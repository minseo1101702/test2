#student1

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://www.musinsa.com/app/?NaPm=ct%3Dl3yedcow%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3De1ef83b897edf0a12e4c97045473642126a4fdb5"
driver.get(url)

time.sleep(3)

serch = driver.find_element_by_xpath(
    '//*[@id="search_query"]')
serch.click()
driver.find_element_by_xpath(
    '//*[@id="search_query"]').send_keys('남성 상의')
serch.send_keys(Keys.ENTER)

res = []

time.sleep(2)
for j in range(1, 11):
    try:
        brand_name = driver.find_element_by_xpath(
            f'//*[@id="searchList"]/li[{j}]/div[4]/div[2]/p[1]/a').text
        print(f'---{brand_name}---')
    except:
        name = "NAN"
        pass
        
        res.append(brand_name)
print(res)
driver.quit()

#student2

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = "https://www.musinsa.com/app/?NaPm=ct%3Dl3yedcow%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3De1ef83b897edf0a12e4c97045473642126a4fdb5"
driver.get(url)

time.sleep(3)

serch = driver.find_element_by_xpath(
    '//*[@id="search_query"]')
serch.click()
driver.find_element_by_xpath(
    '//*[@id="search_query"]').send_keys('여성 상의')
serch.send_keys(Keys.ENTER)

res = []

time.sleep(2)
for j in range(1, 11):
    try:
        brand_name_w = driver.find_element_by_xpath(
            f'//*[@id="searchList"]/li[{j}]/div[4]/div[2]/p[1]/a').text
        print(f'---{brand_name_w}---')
    except:
        name = "NAN"
        pass
        
        res.append(brand_name_w)
print(res)
driver.quit()
