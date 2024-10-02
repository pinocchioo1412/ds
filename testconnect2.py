import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "https://banggia.vndirect.com.vn/chung-khoan/hnx30"
driver.get(url)
time.sleep(5)
sourcode = driver.page_source
data = BeautifulSoup(sourcode,'html.parser')
items = data.select('#banggia-khop-lend-body tr')
stock_symbols = ["CEO","DTD","HUT"]
for row in items :
    row_data = {}
    symbols = row.select('td span')
    stock = row.select_one('.has-symbol').text[1:-1]
    if not stock in stock_symbols :
        continue
    print(stock)