import pytest
from pages.home_page import HomePage
from pages.sign_in import SignIn
from pages.account import AccountPage


class TestSignIn:
    """Tests to sign in the user"""

    @pytest.mark.sign_in
    def test_guest_can_go_to_sign_in(self, browser):
        """go to sign in page"""
        home_page = HomePage(browser)  # open home page
        home_page.go_to_sign_in()  # click sign in button
        sign_in_page = SignIn(browser)
        sign_in_page.should_be_authentication_header()  # check if the page is sign in page
        sign_in_page.authentication_should_be_in_breadcrumbs()  # check if the page is followed in breadcrumbs

    @pytest.mark.register
    @pytest.mark.skip(reason="It will register a new user and we can not delete from data base")
    def test_guest_can_register(self, browser, register):
        """register
        test uses browser and register fixtures
        register fixture creates fake credentials before running the test
        and stores them in the json file"""
        home_page = HomePage(browser)  # open home page
        home_page.go_to_sign_in()  # click sign in button
        sign_in_page = SignIn(browser)
        sign_in_page.enter_email(register.get("email"))  # enter email into register field
        sign_in_page.fill_in_info(register.get("name"),  # enter user's credentials
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
        sign_in_page.register_account()  # submit the form

    @pytest.mark.sign_in
    def test_user_can_sign_in(self, browser, get_credentials):
        """sign in
        test uses get_credentials fixture
        it gets credentials from a json file"""
        home_page = HomePage(browser)  # open the home page
        home_page.go_to_sign_in()  # open sign in page
        sign_in_page = SignIn(browser)
        sign_in_page.sign_in(*get_credentials)  # enter credentials into sign in form and submit
        account_page = AccountPage(browser)
        account_page.return_home_with_logo()  # get to home page by clicking logo link
        home_page = HomePage(browser)
        home_page.guest_should_be_logged_in()  # check if user is signed in
