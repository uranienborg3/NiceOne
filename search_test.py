from pages.home_page import HomePage


class TestSearchHomePage:
    """"tests for search function from home page"""
    def test_search_on_home_page_returns_correct_product_results_count(self, browser):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        results = home_page.search.search_for('t-shirt')
        results.compare_actual_count_with_expected(1)
        results.header_counter_should_show_correct_count()
        home_page = results.return_to_home_page(browser)
        home_page.should_unchangeable_elements_be_present()

    def test_empty_search_returns_correct_message(self, browser):
        """when empty search field is submitted there is correct warning message"""
        home_page = HomePage(browser)
        empty_search = home_page.search.submit_empty_search_field()
        empty_search.empty_search_text_should_be_correct()
        empty_search.header_counter_should_show_correct_count()
        home_page = empty_search.return_to_home_page(browser)
        home_page.should_unchangeable_elements_be_present()

    def test_no_results_search_returns_correct_message(self, browser):
        """when search gives no results there is correct alert message"""
        home_page = HomePage(browser)
        no_result_search = home_page.search.search_for_unavailable_product('glasses')
        no_result_search.no_result_search_text_should_be_correct()
        no_result_search.header_counter_should_show_correct_count()
        home_page = no_result_search.return_to_home_page(browser)
        home_page.should_unchangeable_elements_be_present()
