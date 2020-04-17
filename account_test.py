import pytest
from pages.home_page import HomePage
from pages.account import AccountPage


class TestAccount:
    """My account tests"""

    @pytest.mark.account
    def test_guest_can_go_to_wishlist(self, browser, sign_in):
        """go to wish list
        test uses browser and sign in fixtures
        sign in fixture runs the sign in scenario
        test starts in my account"""
        account = AccountPage(browser)
        account.go_to_wishlist()  # click wishlists button
        account.return_home_with_logo()  # click logo link
        home_page = HomePage(browser)
        home_page.guest_should_be_logged_in()  # check if the user is signed in

    @pytest.mark.account
    @pytest.mark.wishlist
    def test_guest_can_create_wishlist(self, browser, sign_in):
        """create a wishlist
        test uses browser and sign in fixtures"""
        account = AccountPage(browser)
        account.go_to_wishlist()  # go to wishlists
        account.wishlist_should_be_empty()  # wishlists should be empty
        account.create_wishlist('test')  # create a wishlist named 'test'
        account.there_should_be_wishlist()  # check if the wishlist is saved

    @pytest.mark.account
    @pytest.mark.wishlist
    def test_guest_can_delete_wishlist(self, browser, sign_in):
        """delete previously created list
        test uses browser and sign in fixtures"""
        account = AccountPage(browser)
        account.go_to_wishlist()  # go to wishlists
        account.delete_wishlist('test')  # find anf delete wishlist called 'test',
        # exception is raised if there is no such list
        account.wishlist_should_be_empty()  # check if there are no wishlists
