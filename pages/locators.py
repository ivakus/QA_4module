from selenium.webdriver.common.by import By
class MainPageLocators(object):
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRING_FORM = (By.ID, "register_form")