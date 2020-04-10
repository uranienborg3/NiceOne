from pages.home_page import HomePage
from pages.sign_in import SignIn


class TestSignIn:
    def test_guest_can_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.should_be_authentication_header()
        sign_in_page.authentication_should_be_in_breadcrumbs()
