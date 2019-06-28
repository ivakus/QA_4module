from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login"
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_page()
    #page.go_to_login_page()
