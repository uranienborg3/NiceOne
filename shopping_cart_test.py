import pytest
from pages.home_page import HomePage
from pages.shopping_cart import EmptyShoppingCart
from pages.shopping_cart import ShoppingCart
from pages.product import CartSummary
from pages.sign_in import SignIn


class TestShoppingCart:
    """Tests for the shopping cart page"""

    @pytest.mark.cart
    def test_guest_can_see_shopping_cart_is_empty(self, browser):
        """the shopping cart should be empty"""
        home_page = HomePage(browser)  # open home page
        home_page.open_shopping_cart()  # click shopping cart link
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()  # check if shopping cart is followed in breadcrumbs
        shopping_cart.no_products_should_be_in_shopping_cart()  # check if shopping cart is empty
        shopping_cart.should_be_shopping_cart_header()  # check if there is correct header
        shopping_cart.should_be_steps()  # check if there is steps navigation
        shopping_cart.current_step_should_be_summary()  # check if the current step is 'Summary'

    @pytest.mark.cart
    def test_guest_can_return_home_from_shopping_cart_with_breadcrumb(self, browser):
        """"return to home page with breadcrumb link"""
        home_page = HomePage(browser)  # open home page
        home_page.open_shopping_cart()  # click shopping cart link
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()  # check if shopping cart is followed in breadcrumbs
        shopping_cart.return_home_with_breadcrumb()  # click home link in breadcrumbs
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()  # check ui elements on home page
        home_page.breadcrumbs_should_disappear()  # check if breadcrumbs have disappeared

    @pytest.mark.cart
    def test_guest_can_return_home_from_shopping_cart_with_logo(self, browser):
        """click logo to return to home page"""
        home_page = HomePage(browser)  # open home page
        home_page.open_shopping_cart()  # click shopping cart link
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()  # check if shopping cart is followed in breadcrumbs
        shopping_cart.return_home_with_logo()  # click logo link to get to home page
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()  # check ui elements on home page
        home_page.breadcrumbs_should_disappear()  # check if breadcrumbs have disappeared

    @pytest.mark.cart
    def test_can_see_product_in_shopping_cart(self, browser):
        """add product to cart"""
        home_page = HomePage(browser)  # open home page
        name = home_page.get_product_name(2)  # get the name of product No2 on home page
        home_page.add_product_to_cart(2)  # add product No2 to cart by clicking add to cart
        summary = CartSummary(browser)
        summary.go_to_checkout()  # click go to checkout in cart short summary
        shopping_cart = ShoppingCart(browser)
        shopping_cart.product_should_be_in_cart(name)  # check if the name of product is the same in the cart

    @pytest.mark.cart
    def test_can_proceed_to_sign_in(self, browser):
        """proceed to sign in from shopping cart"""
        home_page = HomePage(browser)
        home_page.add_product_to_cart(3)  # add product No3 on home page to cart
        summary = CartSummary(browser)
        summary.go_to_checkout()  # click 'Go to checkout' in the short cart summary
        shopping_cart = ShoppingCart(browser)
        shopping_cart.proceed_to_sign_in()  # click 'Proceed to sign in' on the shopping cart page

    @pytest.mark.xfail(reason="This is to fail, but it passes")
    @pytest.mark.cart
    def test_can_add_product_and_then_sign_in(self, browser, get_credentials):
        """proceed to sign in from shopping cart"""
        home_page = HomePage(browser)
        home_page.add_product_to_cart(6)  # add product No3 on home page to cart
        summary = CartSummary(browser)
        summary.go_to_checkout()  # click 'Go to checkout' in the short cart summary
        shopping_cart = ShoppingCart(browser)
        shopping_cart.proceed_to_sign_in()  # click 'Proceed to sign in' on the shopping cart page
        sign_in_page = SignIn(browser)
        sign_in_page.sign_in(*get_credentials)
