from pages.home_page import HomePage
from pages.shopping_cart import EmptyShoppingCart
from pages.shopping_cart import ShoppingCart
from pages.product import CartSummary


class TestShoppingCart:
    def test_guest_can_see_shopping_cart_is_empty(self, browser):
        home_page = HomePage(browser)
        home_page.open_shopping_cart()
        shopping_cart = EmptyShoppingCart(browser)
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()
        shopping_cart.no_products_should_be_in_shopping_cart()
        shopping_cart.should_be_shopping_cart_header()
        shopping_cart.shopping_cart_should_be_in_breadcrumbs()
        shopping_cart.should_be_steps()
        shopping_cart.current_step_should_be_summary()

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

    def test_can_see_product_in_shopping_cart(self, browser):
        home_page = HomePage(browser)
        name = home_page.get_product_name(2)
        home_page.add_product_to_cart(2)
        summary = CartSummary(browser)
        summary.go_to_checkout()
        shopping_cart = ShoppingCart(browser)
        shopping_cart.product_should_be_in_cart(name)

    def test_can_proceed_to_sign_in(self, browser):
        home_page = HomePage(browser)
        home_page.add_product_to_cart(3)
        summary = CartSummary(browser)
        summary.go_to_checkout()
        shopping_cart = ShoppingCart(browser)
        shopping_cart.proceed_to_sign_in()
