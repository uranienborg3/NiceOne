import pytest
from pages.home_page import HomePage
from pages.search import SearchResults
from pages.search import NoResultSearch
from pages.search import EmptySearchResult


class TestSearch:
    """"tests for search function from home page"""

    @pytest.mark.search
    @pytest.mark.parametrize('term, count', [('t-shirt', 1), ('dress', 7), ('summer dress', 4)],
                             ids=[f'search_{str(i)}' for i in range(1, 4)])
    def test_guest_can_search_for_product_param(self, browser, term, count):
        """search should return correct number of products"""
        home_page = HomePage(browser)
        home_page.search_for(term)  # enter search term into search field and submit
        results = SearchResults(browser)
        results.compare_actual_count_with_expected(count)  # get number of search results and compare with expected
        results.header_counter_should_show_correct_count()  # number in the counter in header should be as expected
        results.search_should_be_in_breadcrumbs()  # search page should be followed in breadcrumbs

    @pytest.mark.search
    def test_guest_can_see_message_search_is_empty(self, browser):
        """when empty search field is submitted there is correct warning message"""
        home_page = HomePage(browser)
        home_page.submit_empty_search_field()  # submit empty search field
        search = EmptySearchResult(browser)
        search.empty_search_text_should_be_correct()  # empty search message should appear
        search.header_counter_should_show_no_results()  # header counter shows zero

    @pytest.mark.search
    def test_guest_can_see_message_search_gives_no_results(self, browser):
        """when search gives no results there is correct alert message"""
        home_page = HomePage(browser)
        home_page.search_for('glasses')  # enter product not presented in the store
        search = NoResultSearch(browser)
        search.no_result_search_text_should_be_correct()  # no results found message should appear
        search.header_counter_should_show_no_results()  # header counter should show zero

    @pytest.mark.search
    def test_guest_can_return_to_home_with_logo(self, browser):
        """return to home page clicking logo"""
        home_page = HomePage(browser)
        home_page.search_for('t-shirt')  # enter search term into search field and submit
        results = SearchResults(browser)
        results.return_home_with_logo()  # click logo link
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()  # search field, logo and shopping cart should be present
        home_page.breadcrumbs_should_disappear()  # breadcrumbs should disappear

    @pytest.mark.search
    def test_guest_can_return_to_home_with_breadcrumb(self, browser):
        """go home clicking home link in breadcrumbs"""
        home_page = HomePage(browser)
        home_page.search_for('t-shirt')  # enter search term into search field and submit
        results = SearchResults(browser)
        results.return_home_with_breadcrumb()  # click home link in breadcrumbs
        home_page = HomePage(browser)
        home_page.unchangeable_elements_should_be_present()  # search field, logo and shopping cart should be present
        home_page.breadcrumbs_should_disappear()  # breadcrumbs should disappear
