from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
        add_btn.click()

    def should_be_add_to_cart_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BTN), "No 'Add to cart' button"

    def should_be_alert_contains_bookname(self):
        text = self.browser.find_element(*ProductPageLocators.BOOKNAME_ALERT).text
        bookname = self.get_bookname()
        assert bookname == text, f"No such bookname in alert. Except '{bookname}' in '{text}'"

    def should_be_alert_contain_price(self):
        text = self.browser.find_element(*ProductPageLocators.PRICE_ALERT).text
        price = self.get_price()
        assert price == text, f"No such price in alert. Ecxept '{price}' in '{text}'"

    def get_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return price

    def get_bookname(self):
        bookname = self.browser.find_element(*ProductPageLocators.BOOKNAME).text
        return bookname

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared_succes_message(self):
        assert self.is_dissappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Succes message doesn't disappeared"