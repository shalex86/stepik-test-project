from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        if self.is_element_present(*LoginPageLocators.REG_FORM):
            input_email = self.browser.find_element(*LoginPageLocators.EMAIL_REG)
            input_email.send_keys(email)
            input_passw_1 = self.browser.find_element(*LoginPageLocators.PASSW_REG1)
            input_passw_1.send_keys(password)
            input_passw_2 = self.browser.find_element(*LoginPageLocators.PASSW_REG2)
            input_passw_2.send_keys(password)
            button = self.browser.find_element(*LoginPageLocators.BTN_REG)
            button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "URL does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def is_user_registered(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON) == True