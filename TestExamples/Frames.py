from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path ="C:Users\VICOMA\Python27\Scripts\chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
time.sleep(3)
driver.find_element_by_link_text("WebDriver").click()
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html/body/div[1]/ul/li[5]").click()
driver.close()
