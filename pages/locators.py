from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_VIEW_LINK = (By.CSS_SELECTOR, "span[class=btn-group] a[class*=btn-default]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REG = (By.CSS_SELECTOR, "#id_registration-email")
    PASSW_REG1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSW_REG2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REG = (By.NAME, "registration_submit")

class ProductPageLocators():
    BASKET_ADD_LINK = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME_FORM = (By.CSS_SELECTOR, "div[class*=product_main] h1")
    PRICE_FORM = (By.CSS_SELECTOR, "div[class*=product_main] p[class='price_color']")
    BOOK_NAME_ALERT = (By.CSS_SELECTOR, "div[class*=alertinner] strong")
    PRICE_ALERT = (By.CSS_SELECTOR, "div[class*=alertinner] p strong")

class BasketPageLocators():
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_NO_EMPTY = (By.CLASS_NAME, "basket-title.hidden-xs")