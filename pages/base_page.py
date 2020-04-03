class BasePage:
    """
    A base class for Page Object model
    Serves as a parent class for other page models
    """

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
