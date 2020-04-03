from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    A base class for Page Object model
    Serves as a parent class for other page models
    """

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Opens a browser with url
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Searches for the element
        :param how: enum BY
        :param what: selector
        :return: true if elements was found, false otherwise
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
