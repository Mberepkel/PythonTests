from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
city = driver.find_element_by_xpath("//*[@id='box6']")
country = driver.find_element_by_xpath("//*[@id='box106']")
action = ActionChains(driver)
action.drag_and_drop(city,country).perform()
