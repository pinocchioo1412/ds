import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
driver = webdriver.Chrome()


url = "https://banggia.vndirect.com.vn/chung-khoan/hnx30"
driver.get(url)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'banggia-khop-lenh')))
except:
    print("Không thể tìm thấy phần tử bảng giá!")
    driver.quit()

sourcode = driver.page_source
data = BeautifulSoup(sourcode, 'html.parser')


items = data.select('#banggia-khop-lenh tbody tr')

stock_symbols = ["CEO", "DTD", "HUT"]

for row in items:
    row_data = {}
    stock = row.select_one('.has-symbol').text[1:-1]  
    
    if stock: 
        stock_text = stock.text.strip() 
        if stock_text in stock_symbols: 
            print(stock_text) 
    for symbol in stock_symbols:
        row_data = stock_symbols[symbol.get('id')] = symbol.text
    real_time_data = {
        'stock' : stock ,
        'date' : datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z"),
        'open' : None,
        'high' : row_data[f'{stock}ceil'],
        'low'  : row_data[f'{stock}floor'],
        'close' : None,
        'volume' : None
    }

driver.quit()
