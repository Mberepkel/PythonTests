class Loginpage():
    text_box_user_id = "Email"
    text_box_password_id = "Password"
    text_button_login_class = "button-1 login-button"
    #text_link_logout_linkTest = "welcome"
    text_link_text_logout = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.text_box_user_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.text_box_password_id).send_keys(password)

    def setloginbutton(self, loginbutton):
        self.driver.find_element_by_class(self.text_button_login_class).click()

    def setlogout(self, logout):
        self.driver.find_element_by_linktext (self.text_link_text_logout).click()

