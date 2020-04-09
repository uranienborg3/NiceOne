from pages.home_page import HomePage
from pages.shopping_cart import EmptyShoppingCart


class TestShoppingCartHomePage:
    def test_guest_can_see_shopping_cart_is_empty(self, browser):
        home_page = HomePage(browser)
        home_page.open_shopping_cart()
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()
        shopping_cart.no_products_should_be_in_shopping_cart()
        shopping_cart.should_be_header()
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()

    def test_guest_can_return_home_from_shopping_cart_with_breadcrumb(self, browser):
        home_page = HomePage(browser)
        home_page.open_shopping_cart()
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()
        shopping_cart.return_home_with_breadcrumb()
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.breadcrumbs_should_disappear()

    def test_guest_can_return_home_from_shopping_cart_with_logo(self, browser):
        home_page = HomePage(browser)
        home_page.open_shopping_cart()
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()
        shopping_cart.return_home_with_logo()
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.breadcrumbs_should_disappear()

# TODO: add non empty shopping cart tests
