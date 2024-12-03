# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.common.by import By
# import time
#
#
# chrome_driver = "C:/chromedriver_CC/chromedriver-win64/chromedriver.exe"
# coccoc = "C:/Program Files/CocCoc/Browser/Application/browser.exe"
# obj =ChromeService(chrome_driver)
# option = ChromeOptions()
# option.binary_location=coccoc
# driver = webdriver.Chrome(service=obj,options=option)
# driver.get("https://coccoc.com/search")
# search_box = driver.find_element("name", "query")
# search_box.send_keys("chu vit")
# search_icon = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/button[2]')
# search_icon.click()
# time.sleep(30)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# import time
#
#
# chrome_driver = "C:/chromedriver_CC/chromedriver-win64/chromedriver.exe"
# coccoc = "C:/Program Files/CocCoc/Browser/Application/browser.exe"
# obj =ChromeService(chrome_driver)
# option = ChromeOptions()
# option.binary_location=coccoc
# driver = webdriver.Chrome(service=obj,options=option)
# driver.get("https://google.com")
# search_box = driver.find_element("name","q")
# search_box.send_keys("dong ho")
# search_box.submit()
# time.sleep(30)
# driver.quit()