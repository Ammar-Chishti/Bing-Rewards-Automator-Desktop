from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("/usr/local/bin/chromedriver")

browser.get("http://shorturl.at/IRS57")

email = browser.find_element_by_id("i0116")
email.send_keys("email")