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
    page.go_to_add_to_basket()
    time.sleep(5)
    page.compare_values_book_price()