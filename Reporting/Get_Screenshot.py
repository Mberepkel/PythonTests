from selenium import webdriver
driver= webdriver.Edge()
driver.get("http://google.co.uk")
#driver.save_screenshot("C:/Users/VICOMA/PycharmProjects/testing/Reporting/home.png")
driver.get_screenshot_as_file("home1.png")
driver.save_screenshot("home2.png")