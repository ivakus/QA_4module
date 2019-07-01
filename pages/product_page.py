import math
from .base_page import BasePage
from .locators import ProductPageLocator
#from .login_page import LoginPage

class ProductPage(BasePage):
    def add_product_to_cart_(self):
        self.should_be_add_to_cart_button()
        self.should_be_book_name()
        self.book_name = self.browser.find_element(*ProductPageLocator.BOOK_NAME).text
        print (self.book_name)
        link = self.browser.find_element(*ProductPageLocator.ADD_CART_BOTTUN)
        link.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocator.ADD_CART_BOTTUN), "ADD Button  is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocator.BOOK_NAME), "Book name  is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")