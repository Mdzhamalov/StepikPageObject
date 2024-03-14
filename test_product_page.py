import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('promocode', ["0", "1", "2", "3", "4", "5", "6",
                                       pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promocode):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promocode}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_be_product_in_the_basket()


@pytest.mark.skip
def test_gest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.should_not_be_success_message()


@pytest.mark.skip
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

