from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-lg[name='login_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn-lg[name='registration_submit']")
