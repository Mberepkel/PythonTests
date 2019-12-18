
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
admin= driver.find_element_by_xpath("/html/body/div[1]/div[2]/ul/li[1]/a/b")
user_magt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users= driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
actions=ActionChains(driver)
actions.move_to_element(admin).move_to_element(user_magt).move_to_element(users).click().perform()

rows = len(driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr")) #//*[@id="resultTable"]/tbody/tr[1]
cols = len(driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr[1]/td")) #//*[@id="resultTable"]/tbody/tr[8]/td[2]

print(rows)
print(cols)
for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        value=driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr[ "+str(r)+" ]/td[ "+str(c)+" ]").text
        print(value, end='      ')


    print()

driver.close()
