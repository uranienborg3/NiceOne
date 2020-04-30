import pytest
from pages.home_page import HomePage
from pages.product import CartSummary


class TestHomePage:
    """"Tests to validate ui elements on the home page"""

    @pytest.mark.home
    def test_quest_can_see_essentials_on_home_page(self, browser):
        """"Logo, search, shopping cart are always visible"""
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()  # check presence og logo, search, shopping cart
        home_page.shopping_cart_should_be_empty()  # there's nothing in the cart

    @pytest.mark.home
    def test_guest_can_change_tabs(self, browser):
        """tabs can be changed on the home page"""
        home_page = HomePage(browser)
        # make a list of current products, change tab,
        # make another list and compare two lists
        home_page.change_to_best_sellers_tab()
        # make a list of current products, change tab,
        # make another list and compare two lists
        home_page.change_to_popular_tab()

    @pytest.mark.home
    def test_guest_can_add_product_to_cart_from_home_page(self, browser):
        """add a product to the cart from home page"""
        home_page = HomePage(browser)
        name = home_page.get_product_name(1)  # get product No1 name
        home_page.add_product_to_cart(1)  # hover over product area and click "add to cart"
        summary = CartSummary(browser)
        # check if names match with short cart summary and count is as expected
        # takes expected product name argument and expected count
        summary.product_is_added_to_cart(name, 1)
        summary.close_cart_summary()  # click "close" on short cart summary
        home_page = HomePage(browser)
        home_page.number_of_products_in_cart_should_be_as_expected(1)  # compare number of items in cart with expected

    @pytest.mark.xfail(raises=IndexError)
    @pytest.mark.home
    def test_guest_can_change_tabs_and_add_product_to_cart_from_home_page(self, browser):
        """add a product to the cart from home page"""
        home_page = HomePage(browser)
        # make a list of current products, change tab,
        # make another list and compare two lists
        home_page.change_to_best_sellers_tab()
        name = home_page.get_product_name(10)  # get product No1 name
        home_page.add_product_to_cart(10)  # hover over product area and click "add to cart"
        summary = CartSummary(browser)
        # check if names match with short cart summary and count is as expected
        # takes expected product name argument and expected count
        summary.product_is_added_to_cart(name, 1)
        summary.close_cart_summary()  # click "close" on short cart summary
        home_page = HomePage(browser)
        home_page.number_of_products_in_cart_should_be_as_expected(1)  # compare number of items in cart with expected
