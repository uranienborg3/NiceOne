from pages.home_page import HomePage


class TestHomePage:
    def test_home_page_validation(self, browser):
        """"HomePage instance can be created"""
        home_page = HomePage(browser)
