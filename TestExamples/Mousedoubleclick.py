from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element= driver.find_element_by_css_selector("#HTML10 > div:nth-child(2) > button:nth-child(6)")
action=ActionChains(driver)
action.double_click(element).perform()
driver.close()