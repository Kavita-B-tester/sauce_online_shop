from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class OrderConfirmation(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.chekout_path=(By.ID,"checkout")
        self.firstname_input=(By.ID,"first-name")
        self.lastname_input=(By.ID,"last-name")
        self.postcode_input=(By.ID,"postal-code")
        self.continue_input=(By.ID,"continue")
        self.finish_button=(By.ID,"finish")


    def Checkout(self):
        self.driver.find_element(*self.chekout_path).click()


    def Order_address(self,first_name,last_name,postcode):
        self.driver.find_element(*self.firstname_input).send_keys(first_name)
        self.driver.find_element(*self.lastname_input).send_keys(last_name)
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.continue_input).click()



    def Order_confirmation(self):
        self.driver.find_element(*self.finish_button).click()
        order_success_message=self.driver.find_element(By.ID,"checkout_complete_container").text
        assert "Thank you for your order!" in order_success_message