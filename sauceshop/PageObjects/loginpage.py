from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username_input=(By.ID,"user-name")
        self.password_input=(By.ID,"password")
        self.signin_button=(By.NAME,"login-button")


    def login(self,username,password):
       self.driver.find_element(*self.username_input).send_keys(username)
       self.driver.find_element(*self.password_input).send_keys(password)
       self.driver.find_element(*self.signin_button).click()
