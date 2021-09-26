from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_LINK = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME_FORM = (By.CSS_SELECTOR, "div[class*=product_main] h1")
    PRICE_FORM = (By.CSS_SELECTOR, "div[class*=product_main] p[class='price_color']")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, "div[class*=alertinner] strong")
    PRICE_ALERT = (By.CSS_SELECTOR, "div[class*=alertinner] p strong")