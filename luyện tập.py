from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

from selenium.webdriver.common.by import By

chrome_drive = 'C:/chromedriver_CC/chromedriver-win64/chromedriver.exe'
coccoc = 'C:/Program Files/CocCoc/Browser/Application/browser.exe'
obj = ChromeService(chrome_drive)
option = ChromeOptions()
option.binary_location = coccoc
driver = webdriver.Chrome  (service=obj, options=option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(10)

# driver.execute_script("window.scrollBy(0, 1400);")
# driver.execute_script("window.scrollTo(0, 1000);")

# driver.execute_script("window.scrollBy(0,-500);")
# time.sleep(5)
# element = driver.find_element(By.XPATH,"//div[@class='totalAmount']")
# driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight,);")
time.sleep(5)
