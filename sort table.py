# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# import time
#
# from selenium.webdriver.common.by import By
#
# chrome_drive = 'C:/chromedriver_CC/chromedriver-win64/chromedriver.exe'
# coccoc = 'C:/Program Files/CocCoc/Browser/Application/browser.exe'
# obj = ChromeService(chrome_drive)
# option = ChromeOptions()
# option.binary_location = coccoc
# driver = webdriver.Chrome(service=obj, options=option)
#
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# time.sleep(30)
#
# driver.find_element(By.XPATH,"//span[normalize-space()='Veg/fruit name']").click()
# veggie=driver.find_elements(By.XPATH,"//tr/td[1]")
# browserSortedVeggies = []
# for ele in veggie:
#     browserSortedVeggies.append(ele.text)
#
# time.sleep(5)
#
# originalBrowserSortedList= browserSortedVeggies.copy()
# browserSortedVeggies.sort()
# assert originalBrowserSortedList == browserSortedVeggies
#
#
# #
# #
# #
# #
# #
# #
# #
# #
