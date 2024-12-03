# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://bing.com/")
# search_box = driver.find_element("name", "q")
# search_box.send_keys("phim hay")
# search_box.submit()


# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import time
# from selenium.webdriver.common.by import By
#
# firefox_driver="C:/geckodriver/geckodriver.exe"
# firefox="C:/Program Files/Mozilla Firefox/firefox.exe"
# obj= Service(firefox_driver)
# option=FirefoxOptions()
# option.binary_location=firefox
# driver=webdriver.Firefox(service=obj,options=option)
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.find_element(By.NAME,"email").send_keys("alo1234@gmail.com")
# driver.find_element(By.ID,"exampleInputPassword1").send_keys("alo12323")
# driver.find_element(By.ID,"exampleInputPassword1").click()
# driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("alo123")
# driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# # Xpath -//tagname[@attribute=value]
# # CSS -tagname[attribute=value] #id .classname
# message= driver.find_element(By.CLASS_NAME,"alert").text
# print(message)
# assert "Success" in message
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("dayroi")
# time.sleep(30)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import time
#
#
# gecko_driver = "C:/geckodriver/geckodriver.exe"
# firefox= "C:/Program Files/Mozilla Firefox/firefox.exe"
# option=FirefoxOptions()
# obj = Service(gecko_driver)
# driver = webdriver.Firefox(service=obj)
# driver.get("https://www.youtube.com/")
# print(driver.title)
# time.sleep(30)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# import time
#
# gecko_driver = "C:/geckodriver/geckodriver.exe"
# firefox = "C:/Program Files/Mozilla Firefox/firefox.exe"
# obj =FirefoxService(gecko_driver)
# option = FirefoxOptions()
# option.binary_location=firefox
# driver = webdriver.Firefox(service=obj,options=option)
# driver.get("https://www.youtube.com/")
# print(driver.title)
# time.sleep(30)
# driver.quit()







