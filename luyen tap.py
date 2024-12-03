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
driver = webdriver.Chrome(service=obj, options=option)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

