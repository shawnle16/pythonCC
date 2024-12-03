# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# chrome_driver="C:/chrom/chromedriver-win64/chromedriver.exe"
# obj= Service(chrome_driver)
# driver=webdriver.Chrome(service=obj)
#
# driver.implicitly_wait(5)
#
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
# time.sleep(5)
#
# results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
# count=len(results)
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()
#
# driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
# driver.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
# driver.find_element(By.XPATH,"//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
# driver.find_element(By.XPATH,"//button[normalize-space()='Apply']").click()
#
# wait = WebDriverWait(driver,15).until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
# print(driver.find_element(By.XPATH,"//span[@class='promoInfo']").text)
#
#
#
#
#
#
#
#
#
