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
        home_page = results.return_to_home_page(browser)
        home_page.should_unchangeable_elements_be_present()

    def test_empty_search_returns_correct_message(self, browser):
        home_page = HomePage(browser)
        no_result_search = home_page.search.submit_empty_search_field()
        no_result_search.empty_search_text_should_be_correct()
        home_page = no_result_search.return_to_home_page(browser)
        home_page.should_unchangeable_elements_be_present()
