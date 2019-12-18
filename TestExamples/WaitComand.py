
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(executable_path= "C:\\Users\VICOMA\Python27\Scripts\chromedriver.exe")
"""driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(5)
print driver.title
assert "Welcome: Mercury Tours" in driver.title
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()"""

# Now open another browser to learn explicite wait
driver.get("https://www.expedia.com/")
driver.maximize_window()
print (driver.title)
#driver.find_element_by_id("tab-flight-tab-hp").click() or use below style

driver.find_element(By.ID,"tab-flight-tab-hp").click()
time.sleep(2)

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")

time.sleep(2)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
time.sleep(2)
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
time.sleep(2)
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("10/18/2019")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("10/12/2019")
time.sleep(2)

driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]"
                             "/div[2]/section[1]/form/fieldset[2]/div/div[4]/div/div/ul/li/button").click()
driver.find_element_by_xpath("/html/body/meso-native-marquee/section/div/div/div[1]/section/div/div[2]/div[2]"
                             "/section[1]/form/div[8]/label/button").click()



