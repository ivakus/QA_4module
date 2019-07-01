
from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def add_product_to_cart_(self):
        self.book_name = self.get_book_name()


        self.should_be_add_to_cart_button()
        link = self.browser.find_element(*ProductPageLocator.ADD_CART_BOTTUN)
        link.click()
        self.solve_quiz_and_get_code()
        self.get_in_cart_book_name()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocator.ADD_CART_BOTTUN), "ADD Button  is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocator.BOOK_NAME), "Book name  is not presented"

    def get_book_name (self):
        self.should_be_book_name()
        return self.browser.find_element(*ProductPageLocator.BOOK_NAME).text

    def get_in_cart_book_name(self):
        assert  self.book_name == self.browser.find_element(*ProductPageLocator.BOOK_NAME_IN_CART).text, "Book name in cart not equal  book name in add page  {}".format(self.book_name)