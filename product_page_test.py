from pages.home_page import HomePage
from pages.search import SearchResults
from pages.product import ProductPage


class TestProductPage:
    def test_guest_can_view_product(self, browser):
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")
        search = SearchResults(browser)
        product_title = search.get_product_title(1)
        search.open_product_page(1)
        product_page = ProductPage(browser)
        product_page.product_title_should_be_correct(product_title)

    def test_guest_can_open_product_picture(self, browser):
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")
        search = SearchResults(browser)
        product_title = search.get_product_title(1)
        search.open_product_page(1)
        product_page = ProductPage(browser)
        product_page.product_title_should_be_correct(product_title)
        product_page.open_product_picture()
        product_page.close_product_picture()

    def test_guest_can_add_product_to_cart(self, browser):
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")
        search = SearchResults(browser)
        search.open_product_page(1)
        product_page = ProductPage(browser)
        product_name = product_page.product_name
        summary = product_page.add_to_cart()
        summary.product_is_added_to_cart(product_name, 1)
        summary.close_cart_summary()
        product_page = ProductPage(browser)
        product_page.number_of_products_in_cart_should_be_as_expected(1)
