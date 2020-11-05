import ipdb
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

driver = webdriver.Chrome(
    ChromeDriverManager().install(), chrome_options=option)


driver.get("https://d2l.arizona.edu/d2l/loginh/")
ipdb.set_trace()

driver.find_element_by_id('ualoginbutton').click()

time.sleep(1)

driver.find_element_by_id("username").send_keys("sooyoungmoon")
driver.find_element_by_id("password").send_keys("Umsy4959msy!")
driver.find_element_by_name("_eventId_proceed").click()

time.sleep(1)

driver.find_element_by_xpath(
    '//*[@id="auth_methods"]/fieldset/div[2]/button').click()

ipdb.set_trace()

driver.find_element_by_class_name("auth-button positive")

driver
