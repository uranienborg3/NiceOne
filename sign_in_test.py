import pytest
from pages.home_page import HomePage
from pages.sign_in import SignIn
from pages.account import AccountPage


class TestSignIn:
    def test_guest_can_go_to_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.should_be_authentication_header()
        sign_in_page.authentication_should_be_in_breadcrumbs()

    @pytest.mark.register
    @pytest.mark.skip(reason="It will register a new user and we can not delete from data base")
    def test_guest_can_register(self, browser, register):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.enter_email(register.get("email"))
        sign_in_page.fill_in_info(register.get("name"),
                                  register.get("surname"),
                                  register.get("password"),
                                  register.get("company"),
                                  register.get("address_1"),
                                  register.get("address_2"),
                                  register.get("city"),
                                  register.get("postcode"),
                                  register.get("add_info"),
                                  register.get("home_phone"),
                                  register.get("mobile"))
        sign_in_page.register_account()

    @pytest.mark.sign_in
    def test_user_can_sign_in(self, browser, get_credentials):
        home_page = HomePage(browser)
        home_page.go_to_sign_in()
        sign_in_page = SignIn(browser)
        sign_in_page.sign_in(*get_credentials)
        account_page = AccountPage(browser)
        account_page.return_home_with_logo()
        home_page = HomePage(browser)
        home_page.guest_should_be_logged_in()
