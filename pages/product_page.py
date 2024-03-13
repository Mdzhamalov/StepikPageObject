import time
from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_product_in_the_basket(self):
        self.should_be_success_message()
        self.should_be_success_price()

    def should_be_success_message(self):
        time.sleep(1)
        actual_product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        expected_product_title = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert actual_product_title == expected_product_title, "The title of the product doesn't match"

    def should_be_success_price(self):
        time.sleep(1)
        actual_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        expected_product_price = self.browser.find_element(*ProductPageLocators.REAL_PRODUCT_PRICE).text

        assert actual_product_price == expected_product_price, "The price in the cart doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message disappeared, but should not be"
