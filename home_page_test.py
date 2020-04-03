from pages.home_page import HomePage


class TestHomePage:
    def test_home_page_validation(self, browser):
        """"HomePage instance can be created, unchangeable elements present, search returns results"""
        home_page = HomePage(browser)
        home_page.should_unchangeable_elements_be_present()


class TestSearchHomePage:
    def test_search_on_home_page_returns_correct_product_results_count(self, browser):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        results = home_page.search.search_for('dress')
        results.compare_actual_count_with_expected(7)
