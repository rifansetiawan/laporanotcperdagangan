# from requests_html import HTMLSession
import os
import datetime
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook
from selenium.webdriver.common.keys import Keys


DRIVER = 'chromedriver'
options = webdriver.ChromeOptions()
if os.name == "nt":

    options.add_argument("--start-maximized")
else:
    
    options.add_argument("--kiosk")


driver = webdriver.Chrome(DRIVER, options = options)
driver.get('https://idx.co.id/data-pasar/data-obligasi-sukuk/laporan-perdagangan-otc/')
time.sleep(5)
allHTML = driver.page_source
soup = BeautifulSoup(allHTML, "html.parser")


wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1') 



select_100 = driver.find_element_by_name('ltrTableReporting_length')
select_100.send_keys(100)
time.sleep(5)
# select_100.send_keys(Keys.RETURN)
allHTML = driver.page_source
soup = BeautifulSoup(allHTML, "html.parser")



div_button_page = soup.find("div", {"class": "dataTables_paginate paging_simple_numbers"})
span_button_page = div_button_page.find('span')
semua_a = span_button_page.find_all('a') 
jumlah_button = 0   
for a in semua_a:
    text_of_button_page = a.get_text()
    print(text_of_button_page)
    jumlah_button = int(text_of_button_page)
    # jumlah_button = jumlah_button + 1
    

print('--------------')
print('ini adalah jumlah button')
print(jumlah_button)
print("----------------")
time.sleep(5)
#=================================================================================================
thead_list = soup.find('table', id='ltrTableReporting').find('thead').find_all('th')
index = 0
for th in thead_list:
    
    textOf_TH = th.get_text()
    print(th.get_text())
    print(index)
    sheet1.write(0, index, textOf_TH) 
    index= index+1
for x in range(jumlah_button):
    allHTML = driver.page_source
    soup = BeautifulSoup(allHTML, "html.parser")
    tbody_list = soup.find('table', id='ltrTableReporting').find('tbody').find_all('tr')
    
    for tr in tbody_list:
        index_column = 0
        tdList = tr.find_all('td')

        for td in tdList:
            if index_column == 0:
                textOf_TD_Pertama = int(td.get_text())
            textOf_TD = td.get_text()
            print(textOf_TD)
            print(textOf_TD_Pertama,index_column)
            sheet1.write(textOf_TD_Pertama, index_column, textOf_TD) 
            index_column = index_column + 1
        index_column = 0
        print("----------------") 
    driver.find_element_by_link_text("Next").click()
    print('ini jalan untuk yang ke : ')
    print(x+1)
    time.sleep(5) 

from datetime import datetime
datestring = datetime.strftime(datetime.now(), '%Y-%m-%d')

print(datestring)

wb.save(datestring+".xls")
