import pytest
from pages.product_page import ProductPage

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://example.com/product/1"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://example.com/product/2"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://example.com/product/3"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://example.com/product/4"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()