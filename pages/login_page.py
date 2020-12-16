import time

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "login is missing from url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "No logging form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is missing"

    def register_new_user(self, email, password):
        link = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        link.send_keys(email)
        link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        link.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_DOUBLE)
        link.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        link.click()

