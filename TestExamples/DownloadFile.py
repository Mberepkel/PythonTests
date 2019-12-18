import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element_by_id("textbox").send_keys("testing this is a test")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
driver.find_element_by_id("pdfbox").send_keys("test in pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(5)

driver.close()