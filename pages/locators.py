from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_ADDRESS_LOGIN = (By.XPATH, "//div/input[@name='login-username']")
    PASSWORD_LOGIN = (By.XPATH, "//div/input[@name='login-password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[@name='login_submit']")

    EMAIL_ADDRESS_REGISTER = (By.XPATH, "//div/input[@name='registration-email']")
    PASSWORD_REGISTER = (By.XPATH, "//div/input[@name='registration-password1']")
    CONFIRM_PASSWORD_REGISTER = (By.XPATH, "//div/input[@name='registration-password2']")
    REGISTER_SUBMIT = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.XPATH, "//button[@value = 'Add to basket']")
    PRODUCT_TITLE = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    REAL_PRODUCT_TITLE = (By.XPATH, "//div[@class = 'alertinner ']/strong")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[@class = 'price_color']")
    REAL_PRODUCT_PRICE = (By.XPATH, "//div[@class = 'alertinner ']/p/strong")

