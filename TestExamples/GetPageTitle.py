from selenium import webdriver

from selenium.webdriver.common.keys import  Keys
driver = webdriver.Chrome()
driver.maximize_window()
url = "http://newtours.demoaut.com/"
driver.get(url)
print ("the title of the page is %s " % (driver.title))
print (driver.current_url)

driver.close()



