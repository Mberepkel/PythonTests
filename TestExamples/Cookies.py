from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.co.uk/")
cookies = driver.get_cookies()
print (len(cookies))
print (cookies)

##adding new cookies to the browser
Cookie = {"name":"my_cookie", "value": "12345"}
driver.add_cookie(Cookie)

cookies = driver.get_cookies()
print (len(cookies))
print (cookies)

#deleting cookies
driver.delete_cookie("my_cookie")
cookies = driver.get_cookies()
print (len(cookies))

driver.delete_all_cookies()
cookies = driver.get_cookies()
print (len(cookies))

driver.close()

