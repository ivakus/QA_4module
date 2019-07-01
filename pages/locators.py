from selenium.webdriver.common.by import By
class MainPageLocators(object):
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRING_FORM = (By.ID, "register_form")
class ProductPageLocator(object):
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_CART_BOTTUN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_IN_CART = (By.CSS_SELECTOR,".alertinner strong")
    SUCCSESS = (By.CSS_SELECTOR,".alert-success")