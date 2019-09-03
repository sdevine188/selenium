import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import win32clipboard

# https://www.youtube.com/watch?v=FFDDN1C1MEQ
# download drivers from https://www.seleniumhq.org/download/
# https://selenium-python.readthedocs.io/index.html
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
#https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html


# set wd
#os.chdir("C:/Users/Stephen/Desktop/Python/selenium")

# start driver
driver = webdriver.Chrome("C:/Users/Stephen/Desktop/Python/selenium/selenium_drivers/chromedriver.exe")

# set page load timeout
driver.set_page_load_timeout(10)

# navigate to google home page
driver.get("http://google.com")

# enter 'financial times' into google search bar
driver.find_element_by_name("q").send_keys("financial times")

# wait momentarily
time.sleep(1)

# press button to execute search 
driver.find_element_by_name("btnK").click()

# find element containing text 'financial times' (various options shown below)
#element_text = driver.find_element_by_class_name("ellip").text
#element_text = driver.find_element_by_xpath("//h3/div[@class = 'ellip']").text
element_text = driver.find_element_by_xpath("//h3/div[contains(text(), 'Financial Times')]").text
print(element_text)

# get url for financial times
element = driver.find_element_by_xpath("//h3/div[contains(text(), 'Financial Times')]/../..")
print(element.get_attribute("href"))

# get list of all urls
list_of_urls = driver.find_elements_by_xpath("//h3/a[@href]")
print(list_of_urls[1].text)
print(list_of_urls[1].get_attribute("href"))

# copy all text on page
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, "a")
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, "c")

# copy page text from clipboard and print
win32clipboard.OpenClipboard()
page_text = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
page_text[0:500]







