import os
import json

import pytest

from PageObjects.loginpage import LoginPage
from PageObjects.orderconfirmation import OrderConfirmation
from PageObjects.shopPage import ShopPage

current_dir=os.path.dirname(__file__)
test_data_path = os.path.join(current_dir, '..', 'data', 'test_e2e1framework.json')
test_data_path = os.path.abspath(test_data_path)
with open(test_data_path) as json_file:
    test_data = json.load(json_file)
    test_list=test_data["data"]
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)

def test_loginframework(BrowserInstance, test_list_item):
    driver=BrowserInstance
    driver.get("https://www.saucedemo.com/")
    loginpage= LoginPage(driver)
    loginpage.get_title()
    loginpage.login(test_list_item["username"], test_list_item["password"])
    shoppage=ShopPage(driver)
    shoppage.get_title()
    shoppage.Add_To_Product_Card_List("Sauce Labs Bolt T-Shirt")
    shoppage.Go_to_cart()
    order_confirmation=OrderConfirmation(driver)
    order_confirmation.Checkout()
    order_confirmation.Order_address(test_list_item["firstname"], test_list_item["lastname"],test_list_item["postcode"])
    order_confirmation.Order_confirmation()