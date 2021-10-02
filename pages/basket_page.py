from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NO_EMPTY) == True, 'The basket not empty'

    def is_present_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY) == True, 'The text of empty basket not presented'

