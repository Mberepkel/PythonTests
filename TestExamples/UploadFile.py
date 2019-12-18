from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,800)", " ")
driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C:/Users/VICOMA/Documents/dox2.jpg")

driver.close()