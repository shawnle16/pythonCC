# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options as ChromeOptions
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
# driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[contains(text(),'Free Access to InterviewQues/ResumeAssistance/Mate')]").click()
# time.sleep(5)
# windowsOpened = driver.window_handles
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[1])
# message=driver.find_element(By.XPATH,"//a[normalize-space()='mentor@rahulshettyacademy.com']")
# value_to_copy=message.text
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[0])
# input_field = driver.find_element(By.XPATH,"//input[@id='username']")
# input_field.send_keys(value_to_copy)
# time.sleep(10)
# element=driver.find_element(By.XPATH,"//i[normalize-space()='learning']")
# password_copy=element.text
# password= driver.find_element(By.XPATH,"//input[@id='password']")
# password.send_keys(password_copy)
# time.sleep(10)
# submit_button=driver.find_element(By.XPATH,"//input[@id='signInBtn']")
# submit_button.click()
# time.sleep(10)
