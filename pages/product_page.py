from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def adding_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT)
        link.click()

    def check_message(self):
        message = self.browser.find_element(*ProductPageLocators.SMS).text
        name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert name == message, 'name is not correct'
        print('name is correct')

    def cart_value(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_cart = self.browser.find_element(*ProductPageLocators.CARD_PRICE).text
        assert price == price_cart, 'price is not correct'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SMS), "Success message is presented, but should not be"

    def there_should_be_success_messages(self):
        assert self.is_disappeared(*ProductPageLocators.SMS), "Success message is not displayed, but should"
