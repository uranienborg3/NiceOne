from pages.home_page import HomePage


class TestShoppingCartHomePage:
    def test_shopping_cart_should_be_empty(self, browser):
        home_page = HomePage(browser)
        shopping_cart = home_page.shopping_cart.open_empty()
        shopping_cart.no_products_should_be_in_shopping_cart()
