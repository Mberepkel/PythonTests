from DataDrivenTest import XLUtils
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
path = "C:/Users/VICOMA/Desktop/Work/IT Training/DDTest Sheet4.xlsx"
row = XLUtils.getRowCount(path,"Sheet1")
col = XLUtils.getColumnCount(path,"Sheet1")
for r in range(2, row+1):
    username=XLUtils.ReadData(path,"Sheet1",r,1)
    password= XLUtils.ReadData(path,"Sheet1",r,2)
    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()
    if driver.title == "Find a Flight: Mercury Tours:":
        print ("test is passed")
        XLUtils.WriteData(path,"Sheet1",r,3,"test is passed")
    else:
        print("test is failed")
        XLUtils.WriteData(path, "Sheet1", r, 3,"test failed")

    driver.find_element_by_link_text("Home").click()
driver.close()


