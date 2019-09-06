from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini span.btn-group a.btn")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOKNAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main>p.price_color")
    BOOKNAME_ALERT = (By.CSS_SELECTOR, ".alert:first-child .alertinner strong")
    PRICE_ALERT = (By.CSS_SELECTOR, ".alert:last-child .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner > p")