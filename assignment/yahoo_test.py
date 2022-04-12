import FinanceDataReader as fdr
import pandas as pd
import time
import json
import csv
import urllib.request
import requests
from selenium.webdriver.common.keys import Keys # 스크롤
from urllib.request import urlopen
from distutils.log import info
from types import new_class
from pydoc import describe
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager #크롬 드라이버 자동 업데이트
from datetime import datetime #날짜

url = 'https://finance.yahoo.com/' #야후 파이낸스 (크롤러 대상) URL

#브라우저 꺼짐 방지
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless') #빽그라운드에서 진행
chrome_options.add_argument("disable-gpu") #gpu사용 최소
chrome_options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
service = Service(executable_path=ChromeDriverManager().install())

#크롬 창 드라이버
driver = webdriver.Chrome(service=service, options=chrome_options)

#파이썬 fdr라이브러리에서 나스닥 불러오기
stock = fdr.StockListing(market = 'NASDAQ')            #나스닥 전체 불러오기
stock = stock.head(151)#총 150개

#데이터 프레임 형태로 만들어서 티커(주식 문자)만 꺼내오기
stock = pd.DataFrame(stock, columns=['Symbol'])
stock = stock.values.tolist()
#stock = stock[95:152]

def listToString(str_list):                             #리스트를 문자열로 변환
    result = ""
    for s in str_list:
        result += s + " "
    return result.strip()

for count in stock:
    key_word = count
    keyword = listToString(key_word)
    #time.sleep(2) #3

    driver.get(url)
    driver.maximize_window()
    time.sleep(2) #3#5

    #검색창 활성
    driver.find_element(By.CSS_SELECTOR, '#yfin-usr-qry').click() 
    driver.find_element(By.CSS_SELECTOR, '#yfin-usr-qry').send_keys(f'{keyword}' + '\n')
    time.sleep(2) #3#5

    #스크롤 내리기 (야후 파이낸스의 경우 무한 스크롤 형태 이므로)
    for c in range(0,9):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(2) #2#3
        
    req = driver.page_source

    soup = BeautifulSoup(req, 'html.parser')
    data_rows = soup.find_all('h3', attrs={'class':'Mb(5px)'})
    print(len(data_rows))
    time.sleep(2) #2#3

    searchNews = []
    #제목 추출
    for data_row in data_rows:
        temp = []
        temp.append(data_row.find('a').get_text()) #뉴스
        temp.append("https://finance.yahoo.com/quote/" + data_row.find('a')['href']) #링크
        searchNews.append(temp) #리스트로 한 묶음으로 넣는다.

    #파일 저장 경로
    #csv파일이 있으면 이어서 저장, 없으면 새로운 csv파일을 만든다.
    file = open(f"C:/Users/tjtjd/Desktop/crawling_with_python/yahoo/0411/{keyword}.csv","w",encoding="UTF-8",newline="")  #csv파일에 저장
    file.write("News_title,Link,"+str(datetime.today().strftime("%Y-%m-%d"))+"\n")
    csvWriter = csv.writer(file)

    for i in searchNews: #csv파일에 입력
        csvWriter.writerow(i)
    file.close()