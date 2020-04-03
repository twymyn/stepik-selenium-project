from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Model of the product page
    """
    def should_be_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not present"

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_product_in_basket = self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_IN_BASKET).text
        assert product_name == success_product_in_basket, "Product was not added to the basket"

    def should_be_right_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        success_basket_total = self.browser.find_element(*ProductPageLocators.SUCCESS_BASKET_TOTAL).text
        assert product_price in success_basket_total, "Basket price is incorrect"
