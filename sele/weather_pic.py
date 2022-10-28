#https://sites.google.com/chromium.org/driver/

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import wget

path = "C:/Users/MEA/天氣圖/sele/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://www.cwb.gov.tw/V8/C/W/analysis.html")
select = Select(driver.find_element(By.NAME, "sel"))

i = 0
for sel in select.options:
    strr = sel.text
    strr.replace(" ", "")
    select.select_by_index(i)
    i+=1
    sleep(1)
    img = driver.find_element(By.ID, "im")
    wget.download(img.get_attribute("src"))

driver.quit()