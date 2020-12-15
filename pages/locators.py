from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_PRODUCT = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    SMS = (By.CSS_SELECTOR,'.alertinner strong')
    CARD_PRICE = (By.CSS_SELECTOR,".alert-info strong")