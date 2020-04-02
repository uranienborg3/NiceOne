from pages.home_page import HomePage


class TestHomePage:
    def test_home_page_validation(self, browser):
        """"HomePage instance can be created, unchangeable elements present, search returns results"""
        home_page = HomePage(browser)
        home_page.should_unchangeable_elements_be_present()
        home_page.search.search_for('dress')
