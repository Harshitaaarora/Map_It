from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
elem=driver.find_element(By.NAME, "q")

if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=input("Enter the address you want to search here: ")
    
elem.send_keys(address)
time.sleep(1)
elem.send_keys(Keys.RETURN)

a=input()


# implementation-
# option 1: seedha chala do aur koi location (for eg the leela) daaldo
# option 2: open terminal, open directory by cd .\web_scraping\mapIT\  , then press enter, the type python mapit.py the leela, then press enter
