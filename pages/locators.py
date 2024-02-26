from selenium.webdriver.common.by import By


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

