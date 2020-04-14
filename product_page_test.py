import pytest
from pages.home_page import HomePage
from pages.search import SearchResults
from pages.product import ProductPage


class TestProductPage:
    """tests for product page"""

    @pytest.mark.product
    def test_guest_can_view_product(self, browser):
        """search for product and open product details"""
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")  # enter search term into search field and submit
        search = SearchResults(browser)  # the search result are loaded
        product_title = search.get_product_title(1)  # get name of the first search result
        search.open_product_page(1)  # click search result No1
        product_page = ProductPage(browser)
        product_page.product_title_should_be_correct(product_title)  # compare expected title with the one on the page

    @pytest.mark.product
    def test_guest_can_open_product_picture(self, browser):
        """open product detail and maximize the picture"""
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")  # enter search term into search field and submit
        search = SearchResults(browser)  # the search result are loaded
        product_title = search.get_product_title(1)  # get name of the first search result
        search.open_product_page(1)  # click search result No1
        product_page = ProductPage(browser)
        product_page.product_title_should_be_correct(product_title)  # compare expected title with the one on the page
        product_page.open_product_picture()  # click the main picture
        product_page.close_product_picture()  # click "X" on the main picture

    @pytest.mark.product
    def test_guest_can_add_product_to_cart(self, browser):
        """search for product, open product details and add product to cart"""
        home_page = HomePage(browser)
        home_page.search_for("t-shirt")  # enter search term into search field and submit
        search = SearchResults(browser)  # the search result are loaded
        search.open_product_page(1)  # click search result No1
        product_page = ProductPage(browser)
        product_name = product_page.product_name  # get the name product on the product page
        summary = product_page.add_to_cart()  # click "Add to cart"
        # check if the names are the same, count should be as expected
        summary.product_is_added_to_cart(product_name, 1)
        summary.close_cart_summary()  # close the short cart summary
        product_page = ProductPage(browser)
        # count of products in the shopping cart should be as expected
        # without opening the shopping cart
        product_page.number_of_products_in_cart_should_be_as_expected(1)
