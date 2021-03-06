import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import win32clipboard

# https://www.youtube.com/watch?v=FFDDN1C1MEQ
# download drivers from https://www.seleniumhq.org/download/
# https://selenium-python.readthedocs.io/index.html
# http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
#https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html
#https://stackoverflow.com/questions/10629815/how-to-switch-to-new-window-in-selenium-for-python


# set wd
os.chdir("C:/Users/Stephen/Desktop/Python/selenium")

# start driver
driver = webdriver.Chrome("selenium_drivers/chromedriver.exe")
#driver = webdriver.Chrome("C:/users/sjdevine/Work Folders/Desktop/chromedriver.exe")
#driver = webdriver.Chrome("H:/Python/selenium/selenium_drivers/chromedriver.exe")

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

# export raw html in a df, which can then be loaded for further analysis in r
raw_html = driver.page_source
type(raw_html)
raw_html
raw_html_df = pd.DataFrame({"raw_html" : [raw_html]})
raw_html_df.shape
raw_html_df.head()
raw_html_df.to_csv("example_raw_html_df.csv", index = False)


# find element containing text 'financial times' (various options shown below)
# note that the html layout may change over time

#element_text = driver.find_element_by_class_name("ellip").text
#element_text = driver.find_element_by_xpath("//h3/div[@class = 'ellip']").text
element_text = driver.find_element_by_xpath("//h3[contains(text(), 'Financial Times')]").text
print(element_text)

# get url for financial times
element = driver.find_element_by_xpath("//h3[contains(text(), 'Financial Times')]/..")
print(element.get_attribute("href"))

# get list of all urls
list_of_urls = driver.find_elements_by_xpath("//h3/a[@href]")
len(list_of_urls)
type(list_of_urls)
print(list_of_urls[1].text)
print(list_of_urls[1].get_attribute("href"))

# loop through list_of_urls getting urls
for i in list(range(0, len(list_of_urls))):
        current_text_df = pd.DataFrame({"text" : [list_of_urls[i].text],
                                        "element_i" : [i]})
        print(current_text_df)

# copy all text on page
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, "a")
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL, "c")

# copy page text from clipboard and print
win32clipboard.OpenClipboard()
page_text = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
page_text[0:500]

# Opens a new tab
driver.execute_script("window.open()")

# can view open tabs using window_handles
print(driver.window_handles)

# Switch to the newly opened tab and navigate to website
driver.switch_to.window(driver.window_handles[1])
driver.get("https://google.com")

# switch back to original tab
driver.switch_to.window(driver.window_handles[0])
driver.get("https://imdb.com")

# switch back to google tab and close it
driver.switch_to.window(driver.window_handles[1])
driver.close()
