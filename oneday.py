# # 1. Import all library

from requests_html import HTMLSession
import datetime
import time
import xlwt 
from xlwt import Workbook 
from datetime import datetime
from datetime import datetime
datestring = datetime.strftime(datetime.now(), '%d/%m/%Y')
import xlwings as xw
from openpyxl import Workbook, load_workbook
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print(datestring)

DRIVER = 'chromedriver'
options = webdriver.ChromeOptions()
if os.name == "nt":

    options.add_argument("--start-maximized")
else:
    
    options.add_argument("--kiosk")


driver = webdriver.Chrome(DRIVER, options = options)
driver.get('https://www.idx.co.id/data-pasar/ringkasan-perdagangan/ringkasan-broker/')
time.sleep(10)
for t in range(20):
	time.sleep(0.5)
	print("sleep ", t)
#========================================================================================================================

#START-UNTUK MEMASUKAN TANGGAL
# y = "'18/09/2019'"

tanggal = "document.getElementById('dateFilter').value="+"'"+datestring+"'"
print(tanggal)
for r in range(3):
	time.sleep(0.5)
driver.execute_script(tanggal)

print('date selected')

for w in range(11):
	time.sleep(0.5)
	print("sleep ", w)



#END-UNTUK MEMASUKAN TANGGAL


#========================================================================================================================


#START - UNTUK KLIK TOMBOL SEARCH

driver.find_element_by_css_selector("button[onclick='getBrokerSummary()']").click()

print('button search has been clicked')
time.sleep(1)
#END - UNTUK KLIK TOMBOL SEARCH

#========================================================================================================================


#START - UNTUK KLIK TOMBOL UNDUH

# testing = driver.find_element_by_css_selector("td[class='dataTables_empty']").text()
bolehan = 0
try:
    content = driver.find_element_by_class_name('dataTables_empty').text
    bolehan = 1
except:
    bolehan = 3
    content = 0
    pass

# print(content)

if bolehan == 3:
    driver.find_element_by_css_selector("A[onclick='downloadSummary()']").click()
    print('button UNDUH has been clicked')
elif bolehan == 1:
	print('no documents to download')



#END - UNTUK KLIK TOMBOL UNDUH

for i in range(11):
	time.sleep(0.5)

driver.close()

# driver.close()


#acuan
# acuan --------------------> # driver.execute_script("document.getElementById('dateFilter').value = '18/09/2019'")