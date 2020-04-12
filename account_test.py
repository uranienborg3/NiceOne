import pytest
from pages.home_page import HomePage
from pages.account import AccountPage


class TestAccount:
    @pytest.mark.account
    def test_guest_can_go_to_wishlist(self, browser, sign_in):
        account = AccountPage(browser)
        account.go_to_wishlist()
        account.return_home_with_logo()
        home_page = HomePage(browser)
        home_page.guest_should_be_logged_in()
