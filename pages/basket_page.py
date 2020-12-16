from pages.base_page import BasePage
from pages.locators import BacketPageLocators


class BasketPage(BasePage):

    def shopping_cart_is_empty(self):
        assert self.is_not_element_present(*BacketPageLocators.BASKET_IS_NOT_EMPTY), "basket is not empty"

    def text_that_the_shopping_cart_is_empty(self):
        assert self.browser.find_element(*BacketPageLocators.MESSAGE), "Success message is not displayed, but should"
