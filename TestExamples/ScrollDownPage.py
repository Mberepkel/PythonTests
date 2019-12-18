from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0,1000)", " ")
#flag= driver.find_element_by_css_selector("#content > div.container > div:nth-child(2) > table:nth-child(1) > tbody > tr:nth-child(86) > td:nth-child(1) > img")
#driver.execute_script("arguments[0].scrollIntoView();", flag)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep (3)
driver.close()