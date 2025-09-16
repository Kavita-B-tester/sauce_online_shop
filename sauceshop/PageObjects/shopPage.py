
from selenium.webdriver.common.by import By
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.product_cards=(By.CLASS_NAME,"inventory_item")
        self.go_tocart=(By.CLASS_NAME,"shopping_cart_container")



    def Add_To_Product_Card_List(self,product_name):
        products=self.driver.find_elements(*self.product_cards)
        for product in products:
            name_element = product.find_element(By.CLASS_NAME, "inventory_item_name")
            name = name_element.text.strip()
            if name == product_name:
                add_button = product.find_element(By.NAME,"add-to-cart-sauce-labs-bolt-t-shirt")
                add_button.click()
                return True  # Product found and added
        return False



    def Go_to_cart(self):
        self.driver.find_element(*self.go_tocart).click()


