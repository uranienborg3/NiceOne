from pages.home_page import HomePage
from pages.search import SearchResults
from pages.search import NoResultSearch
from pages.search import EmptySearchResult


class TestSearchHomePage:
    """"tests for search function from home page"""
    def test_guest_can_search_for_product(self, browser):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        home_page.search_for('dress')
        results = SearchResults(browser)
        results.compare_actual_count_with_expected(7)
        results.header_counter_should_show_correct_count()
        results.search_should_be_in_breadcrumbs()

    def test_guest_can_see_message_search_is_empty(self, browser):
        """when empty search field is submitted there is correct warning message"""
        home_page = HomePage(browser)
        home_page.submit_empty_search_field()
        search = EmptySearchResult(browser)
        search.empty_search_text_should_be_correct()
        search.header_counter_should_show_correct_count()
        search.search_should_be_in_breadcrumbs()
        search.return_home_with_breadcrumb()

    def test_guest_can_see_message_search_gives_no_results(self, browser):
        """when search gives no results there is correct alert message"""
        home_page = HomePage(browser)
        home_page.search_for_unavailable_product('glasses')
        search = NoResultSearch(browser)
        search.no_result_search_text_should_be_correct()
        search.header_counter_should_show_correct_count()
        search.search_should_be_in_breadcrumbs()

    def test_guest_can_return_to_home_with_logo(self, browser):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        home_page.search_for('t-shirt')
        results = SearchResults(browser)
        results.search_should_be_in_breadcrumbs()
        results.return_home_with_logo()
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.breadcrumbs_should_disappear()

    def test_guest_can_return_to_home_with_breadcrumb(self, browser):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        home_page.search_for('t-shirt')
        results = SearchResults(browser)
        results.search_should_be_in_breadcrumbs()
        results.return_home_with_breadcrumb()
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()
        home_page.breadcrumbs_should_disappear()