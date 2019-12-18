from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
action = ActionChains(driver)
action.context_click(button).perform()
driver.close()

#ActionChains.double_click()  ## double click on element
#ActionChains.click() ## click on an element
#ActionChains.context_click()  ## right click on element
