import pytest
from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"]


@pytest.mark.parametrize('link', links)
def test_guest_should_see_add_product_to_basket_button(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_product_in_basket()
    page.should_be_right_basket_total()
