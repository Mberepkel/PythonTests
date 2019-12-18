from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Firefox(executable_path= "C:/Users/VICOMA/Documents/Drivers/geckodriver.exe")
url = "http://demo.automationtesting.in/Windows.html"
driver.get(url)
print (driver.title)
print (driver.current_url)
driver.find_element_by_xpath ("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
time.sleep(5)
#driver.close()
driver.quit()