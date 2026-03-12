import pytest
from pages.base_page import BasePage

def test_guest_should_see_login_link(browser):
    link = "http://example.com"
    page = BasePage(browser, link)
    page.open()
    assert page.is_element_present(*page.locators.LOGIN_LINK), "Login link is not present"