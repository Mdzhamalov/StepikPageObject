import time

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_product_in_the_basket(self):
        self.should_be_product_title()
        # self.basket_price_match()

    def should_be_product_title(self):
        actual_product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        expected_product_title = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_TITLE).text
        assert actual_product_title == expected_product_title, "The title of the product doesn't match"


    # def basket_price_match(self):
