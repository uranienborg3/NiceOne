from pages.home_page import HomePage


class TestHomePage:
    """"Tests to validate ui elements on the home page"""
    def test_quest_can_see_essentials_on_home_page(self, browser):
        """"HomePage instance can be created, unchangeable elements present, search returns results"""
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.shopping_cart_should_be_empty()
