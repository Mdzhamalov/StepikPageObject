from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_of_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Your basket is not empty."

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty, but should be"
