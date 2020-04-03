from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Model of the basket page
    """
    def should_be_basket_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket doesnt have items"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is filled, but should be empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not present"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is presented, but should not be "
