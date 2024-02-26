from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert 'login' in login_url, "There is no /login in the URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_LOGIN), \
            "There is no field 'Email address'"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER), \
            "There is no field 'Confirm password'"
