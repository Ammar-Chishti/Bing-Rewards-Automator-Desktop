from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string
import random

def create_URLs() -> list:  # Creates 25 URLs to search on bing.com to earn rewards points
    list_of_URLs = []

    for i in range(25):
        root = "bing.com/search?q="

        letters = string.ascii_letters
        suffix = "".join(random.choice(letters) for i in range(10))
        list_of_URLs.append(root + suffix)

    return list_of_URLs


browser = webdriver.Chrome("/usr/local/bin/chromedriver")

browser.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1563130781&rver=6.7.6631.0&wp=MBI_SSL&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d1B39D6E50827401881165767AF42E1D4%2526wlexpsignin%253d1%26sig%3d0651AC2328BB60D32AD5A1BA293361CF&lc=1033&id=264960&CSRFToken=b34a6229-88ed-47e6-83f3-dd676bd5591b&aadredir=1")

email = browser.find_element_by_id("i0116")
email.send_keys("your_email")

submit_button = browser.find_element_by_id("idSIButton9")
submit_button.click()
time.sleep(1)   # Everytime you open a new webpage, you must wait a little bit for the webpage to load

password = browser.find_element_by_id("i0118")
password.send_keys("your_password")

submit_button = browser.find_element_by_id("idSIButton9")
submit_button.click()



