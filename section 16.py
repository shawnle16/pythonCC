# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# chrome_drive = 'C:/chromedriver_CC/chromedriver-win64/chromedriver.exe'
# coccoc = 'C:/Program Files/CocCoc/Browser/Application/browser.exe'
# obj = ChromeService(chrome_drive)
# option = ChromeOptions()
# option.binary_location = coccoc
# driver = webdriver.Chrome  (service=obj, options=option)
# # # option.add_argument("headless")
# # # option.add_argument("--ignore-certificate-errors")
#
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# products= driver.find_element(By.XPATH,"//div[@class='card h-100']")
# for product in products:
#     productName = product.find_element(By.XPATH,"div/h4/a").text
#     if productName == "Blackberry":
#         product.find_element(By.XPATH,"div/button").click()
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR,"a[class='btn-primary']").click()
# driver.find_element(By.XPATH,"//button[normalize-space()='Checkout']")
# driver.find_element(By.XPATH,"//input[@id='country']").send_keys("In")
# wait=WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,'India')))
# driver.find_element(By.LINK_TEXT,"India").click()
# driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
# driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
# successmessage=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text()
# assert "Success!" in successmessage
# time.sleep(10)
