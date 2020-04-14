from .locators import SearchResultsLocators
from .locators import BreadcrumbsLocators
from .base import BasePage
from .base import InvalidPageException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseSearch(BasePage):
    """base for all kinds of search result pages"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def header_counter_should_show_no_results(self):
        """gets the number from header counter and
        checks if it is zero"""
        assert self.header_counter == 0, "Header counter does not show zero"

    def search_should_be_in_breadcrumbs(self):
        """checks if there is the search breadcrumb"""
        assert self.is_element_present(*BreadcrumbsLocators.SEARCH_BREADCRUMB), "Search not in breadcrumbs"

    def _validate_page(self):
        """checks if title of the page contain 'Search'"""
        WebDriverWait(self.browser, 5).until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded on the page")

    @property
    def header_counter(self):
        """returns the number in the header counter"""
        header_counter = self.browser.find_element(*SearchResultsLocators.HEADING_COUNTER).text
        header_counter_list = header_counter.split()
        return int(header_counter_list[0])


class SearchResults(BaseSearch):
    """search result page that contains some results"""
    _product_count = 0  # number of search results
    _product_links = {}  # a key is the number of product; a value is a link element
    _product_names = {}  # a key is the number of product; a value is a name of product

    def __init__(self, *args, **kwargs):
        """need to wait before the page is fully loaded"""
        super().__init__(*args, **kwargs)
        WebDriverWait(self.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
        results = self.browser.find_elements(*SearchResultsLocators.PRODUCT_LIST)  # find all product elements
        assert len(results) > 0, "No results found"  # check if the list is empty, it should not be
        count = 0
        for product in results:
            count += 1
            self._product_links[count] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            self._product_names[count] = product.find_element(*SearchResultsLocators.PRODUCT_NAME).text
            self._product_count += 1

    @property
    def product_count(self):
        """returns number of search results"""
        return self._product_count

    def compare_actual_count_with_expected(self, expected_count):
        """gets current number of search results and
        compares it with one passed as an argument"""
        assert self._product_count == expected_count, "Actual and expected counts of results do not match"

    def header_counter_should_show_correct_count(self):
        """compares number of search results with the number in the header counter"""
        assert self._product_count == self.header_counter, 'Header counter does not show correct result count'

    def get_product_title(self, product_number):
        """returns name of the product, number of which is passed as argument"""
        return self._product_names.get(product_number)

    def open_product_page(self, product_number):
        """opens the product, number of which is passed as argument"""
        self._product_links[product_number].click()


class EmptySearchResult(BaseSearch):
    def __init__(self, *args, **kwargs):
        super(EmptySearchResult, self).__init__(*args, **kwargs)

    def empty_search_text_should_be_correct(self):
        """checks if the empty search result message is correct"""
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "Please enter a search keyword" == message, "Empty search alert message text does not match expected"


class NoResultSearch(BaseSearch):
    def __init__(self, *args, **kwargs):
        super(NoResultSearch, self).__init__(*args, **kwargs)

    def no_result_search_text_should_be_correct(self):
        """checks if the message is correct when the search gives no results"""
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "No results were found for your search" in message, "No search results message is not correct"
