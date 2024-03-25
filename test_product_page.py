import pytest
import time

from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


def test_gest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    product_page.should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_message_of_empty_basket()
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", "Aa123456^")
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, link)
        product_page.add_to_basket()
        # page.solve_quiz_and_get_code()
        product_page.should_be_product_in_the_basket()

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        product_page = ProductPage(browser, link)
        product_page.should_not_be_success_message()
