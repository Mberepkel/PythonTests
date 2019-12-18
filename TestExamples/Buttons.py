import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path= "C:/Users/VICOMA/Python27/Scripts/chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index?1537702596407")

Male_status = driver.find_element_by_css_selector("label[for=RESULT_RadioButton-7_0]").is_selected()
print (Male_status)
if Male_status == False:
    driver.find_element_by_css_selector("label[for=RESULT_RadioButton-7_0]").click()

else:
   print ("Test is Failed")
sunday= driver.find_element_by_css_selector("label[for=RESULT_CheckBox-8_0]").click()
Saturday= driver.find_element_by_css_selector("label[for=RESULT_CheckBox-8_6]").click()
driver.close()
