# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# chrome_drive = 'C:/chromedriver_CC/chromedriver-win64/chromedriver.exe'
# coccoc = 'C:/Program Files/CocCoc/Browser/Application/browser.exe'
# obj = ChromeService(chrome_drive)
# option = ChromeOptions()
# option.binary_location = coccoc
# driver = webdriver.Chrome(service=obj, options=option)
# # 5 seconds is max timeout.. 2 seconds(3 seconds save)
# driver.implicitly_wait(5)
# # driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# # driver.maximize_window()
# # time.sleep(2)
# # element_to_hover = driver.find_element(By.ID, "mousehover")
# # actions = ActionChains(driver)
# # actions.move_to_element(element_to_hover).perform()
# # time.sleep(10)
# # # actions.context_click(driver.find_element(By.XPATH,"//a[normalize-space()='Top']")).click().perform()
# # # time.sleep(10)
# # actions.context_click(driver.find_element(By.XPATH,"//a[normalize-space()='Reload']")).click().perform()
# # time.sleep(20)
#
# # driver.get("https://the-internet.herokuapp.com/windows")
# # driver.maximize_window()
# # time.sleep(2)
# # driver.find_element(By.LINK_TEXT,"Click Here").click()
# # time.sleep(5)
# # windowsOpened = driver.window_handles
# # time.sleep(5)
# # driver.switch_to.window(windowsOpened[1])
# # time.sleep(10)
# # driver.switch_to.window(windowsOpened[0])
#
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"Blog").click()
# time.sleep(5)
# driver.find_element(By.LINK_TEXT,"Join our Courses").click()
# time.sleep(5)
# windowsOpened = driver.window_handles
# time.sleep(5)
# driver.switch_to.window(windowsOpened[1])
# time.sleep(5)
# driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[@id='login-with-google']").click()
# time.sleep(5)
#
#
# # driver.find_element(By.LINK_TEXT,"Click Here").click()
# # time.sleep(5)
# # windowsOpened = driver.window_handles
# # time.sleep(5)
# # driver.switch_to.window(windowsOpened[1])
# # time.sleep(10)
# # driver.switch_to.window(windowsOpened[0])
#
#
#
#
