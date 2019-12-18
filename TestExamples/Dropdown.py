
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path= "C:Users\VICOMA\Python27\Scripts\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)
#drp.select_by_visible_text("Morning") #by text Morning, Afternoon or Evening
#drp.select_by_index(2) #By idex 0, 1 , 2 , 3
drp.select_by_value("Radio-2") # value of the items

#Count number of options on dropdown#

print (len(drp.options))

# Capture all the options available on dropdown and print them #
all_options = drp.options
for option in all_options:
    print (option.text)
