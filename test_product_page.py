from pages.product_page import ProductPage
import time
import pytest

def custom_format_link_string(param):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{}"
    return link.format(param)

@pytest.mark.parametrize('link', 
    [
        custom_format_link_string(x) if x != 7 else pytest.param(custom_format_link_string(x),
            marks=pytest.mark.xfail) for x in range(10)
    ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_to_basket(promo=True)
    page.compare_values_book_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_to_basket()
    page.is_not_show_message_success()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.is_not_show_message_success()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_to_basket()
    page.is_disappeared_message_success()