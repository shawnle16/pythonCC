# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# driver.get("https://www.google.com/")
# search_box = driver.find_element("name", "q")
# search_box.send_keys("phim hay")
# search_box.submit()
# time.sleep(30)
# driver.quit()

# from selenium import webdriver
# import time
#
# driver = webdriver.Edge()
# driver.get("https://www.youtube.com/")
# print(driver.title)
# print(driver.current_url)
# time.sleep(30)

# from selenium import webdriver
# import time
#
# from selenium.webdriver.chrome.service import Service
#
# chrome_driver = 'C:/chrom/chromedriver-win64/chromedriver.exe'
# service_obj = Service(chrome_driver)
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.youtube.com/")
# print(driver.title)
# print(driver.current_url)
# time.sleep(30)

# from selenium import webdriver
# import time
# from selenium.webdriver.firefox.options import Options
#
#
# firefox=("C:/Program Files/Mozilla Firefox/firefox.exe")
# options = Options()
# options.binary_location = firefox
#
# driver = webdriver.Firefox(options=options)
# driver.get("https://www.youtube.com/")
# time.sleep(30)

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# import time
# from selenium.webdriver.firefox.options import Options
#
# gecko_driver =("C:/geckodriver/geckodriver.exe")
# firefox =("C:/Program Files/Mozilla Firefox/firefox.exe")
# service_driver= Service(gecko_driver)
# option = Options()
# option.binary_location = firefox
# driver = webdriver.Firefox(service=service_driver, options=option)
# driver.get("https://www.youtube.com/")
# time.sleep(30)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# import time
# from selenium.webdriver.firefox.options import Options
#
# gecko_driver =("C:/geckodriver/geckodriver.exe")
# service_driver= Service(gecko_driver)
# option = Options()
# driver = webdriver.Firefox(service=service_driver, options=option)
# driver.get("https://www.google.com/")
# search_box = driver.find_element("name", "q")
# search_box.send_keys("phim hay")
# search_box.submit()
# time.sleep(30)
# driver.quit()






