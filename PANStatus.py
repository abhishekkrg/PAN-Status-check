#Open URL AND AUTOMATE


import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys






user = "abhishxxxx@xxxx.com"
pwd = ""
chromedriver = "C:\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)



driver.get("https://tin.tin.nsdl.com/pantan/StatusTrack.html")
assert "Status" in driver.title
elem = driver.find_element_by_name("ST_SEARCH_TYPE")
elem.send_keys("P")
elem = driver.find_element_by_name("ST_SEARCH_OPTION")
elem.send_keys("A")
elem = driver.find_element_by_name("ST_ACK_NUM")
elem.send_keys("xxx5xx000xxx")

elem = driver.find_element_by_name("submit")



elem.send_keys(Keys.RETURN)

#driver.fin
#driver.close()

#driver.quit()