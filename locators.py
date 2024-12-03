# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# chrome_driver="C:/chrom/chromedriver-win64/chromedriver.exe"
# obj= Service(chrome_driver)
# driver=webdriver.Chrome(service=obj)
# driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("alo1")
# driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("alo1")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# # driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
#
#
# time.sleep(30)