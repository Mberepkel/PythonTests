from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "C:\\Users\VICOMA\Python27\Scripts\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
links = driver.find_elements(By.TAG_NAME,"a")
print ("The number of links present is %d" % len(links)) # print how many links present in a page

for link in links:
    print (link.text)

#driver.find_element(By.LINK_TEXT,"REGISTER").click() # full link
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click() # partial link