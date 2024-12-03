# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# chrome_driver="C:/chrom/chromedriver-win64/chromedriver.exe"
# obj= Service(chrome_driver)
# driver=webdriver.Chrome(service=obj)
# # driver.get("https://rahulshettyacademy.com/angularpractice")
# # #
# # # dropdown_value=driver.find_element(By.ID,"exampleFormControlSelect1")
# # # dropdown_list= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# # # # dropdown_list.select_by_index(1)
# # # dropdown_list.select_by_visible_text("Female")
# # # time.sleep(30)
# # # driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# # #
# # # # dropdown_value=driver.find_element(By.CSS_SELECTOR,"select[class='form-control']")
# # # dropdown_list1= Select(driver.find_element(By.CSS_SELECTOR,"select[class='form-control']"))
# # # # dropdown_list.select_by_index(1)
# # # dropdown_list1.select_by_value("teach")
# # # time.sleep(30)
# #
# # # driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# # # driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("Ind")
# # # time.sleep(10)
# # # countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
# # #
# # # for country in countries:
# # #     if country.text == "India":
# # #      country.click()
# # #     break
# # #
# # # if driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India":
# # #     print ("Right value")
# # #
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# name = driver.find_element(By.CSS_SELECTOR,"#dropdown-class-example")
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#
# # print(len(checkboxes))
#
# # for checkbox in checkboxes:
# #     if checkbox.get_attribute("value") == "option3"
# #         checkbox.click()
# #         assert checkbox.is_selected()
# #         break
#
# checkbox2 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
# if not checkbox2.is_selected():
#     checkbox2.click()
#
# checkbox3 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']")
# if not checkbox3.is_selected():
#     checkbox3.click()
#
# radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
# radiobuttons[0].click()
# assert radiobuttons[0].is_selected()
#
# textbox =  driver.find_element(By.ID,"displayed_text")
# button_hide= driver.find_element(By.ID,"hide_textbox")
# button_hide.click()
# button_show= driver.find_element(By.ID,"show_textbox")
# button_hide.click()
# #
# # if textbox_is_displayed():
# #     button_hide.click()
# # else:
# #     button_show.click()
#
# buttonAlert= driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Aaaaa")
# driver.find_element(By.ID,"alertbtn").click()
# alert=driver.switch_to.alert
# alertText=alert.text
# print(alertText)
# time.sleep(10)
# alert.dismiss()
#
#
#
#
#
#
#
#
