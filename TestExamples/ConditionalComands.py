from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Chrome(executable_path= "C:\Users\VICOMA\Python27\Scripts\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
ele= driver.find_element_by_name("userName")

print (ele.is_displayed())
print (ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")

print (pwd_ele.is_enabled())
print (pwd_ele.is_displayed())

ele.send_keys("mercury")
pwd_ele.send_keys("mercury")
driver.find_element_by_name("login").click()

round_trip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print ("status of round trip is", round_trip_radio.is_selected())
one_trip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print ("status of one way trip is", one_trip_radio.is_selected())
driver.close()
