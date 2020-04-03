from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """
    Model of the main page
    """

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
