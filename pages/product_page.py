from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def go_to_add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        login_link.click()
        self.solve_quiz_and_get_code()

    def compare_values_book_price(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME_FORM)
        price = self.browser.find_element(*ProductPageLocators.PRICE_FORM)
        book_ = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ALERT)
        price_ = self.browser.find_element(*ProductPageLocators.PRICE_ALERT)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(ProductPageLocators.PRICE_ALERT))
        assert book.text == book_.text and price.text == price_.text, "Book's names is not ident, prices is not ident"