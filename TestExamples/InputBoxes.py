from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
driver = webdriver.Chrome(executable_path= "C:\\Users\VICOMA\Python27\Scripts\chromedriver.exe")
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index?1537702596407")
input_boxes= driver.find_elements_by_class_name("text_field")
print (len(input_boxes))
driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Law")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("Mbere")
driver.find_element(By.NAME,"RESULT_TextField-3").send_keys("07433455")

