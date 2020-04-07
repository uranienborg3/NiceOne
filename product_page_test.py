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
