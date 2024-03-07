import time

import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promocode', range(10))
def test_guest_can_add_product_to_basket(browser, promocode):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promocode}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, link)
    product_page.add_to_basket()
    page.solve_quiz_and_get_code()
    product_page.should_be_product_in_the_basket()

