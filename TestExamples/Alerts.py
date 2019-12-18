from selenium import webdriver
import time
driver= webdriver.Chrome(executable_path= "C:/Users/VICOMA/Documents/Drivers/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

driver.switch_to_alert().dismiss()   # closes alert by using cancel button
#driver.switch_to_alert().accept()    # closes alert by using ok button
#driver.switch_to.alert().dismiss()
time.sleep(2)


driver.close()

