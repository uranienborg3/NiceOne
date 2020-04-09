from pages.home_page import HomePage
from pages.product import CartSummary


class TestHomePage:
    """"Tests to validate ui elements on the home page"""
    def test_quest_can_see_essentials_on_home_page(self, browser):
        """"HomePage instance can be created, unchangeable elements present, search returns results"""
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.shopping_cart_should_be_empty()

    def test_guest_can_change_tabs(self, browser):
        home_page = HomePage(browser)
        home_page.change_to_best_sellers_tab()

    def test_guest_can_add_product_to_cart_from_home_page(self, browser):
        home_page = HomePage(browser)
        name = home_page.get_product_name(1)
        home_page.add_product_to_cart(1)
        summary = CartSummary(browser)
        summary.product_is_added_to_cart(name, 1)
        summary.close_cart_summary()
        home_page = HomePage(browser)
        home_page.number_of_products_in_cart_should_be_as_expected(1)
