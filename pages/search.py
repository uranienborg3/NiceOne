from .locators import SearchResultsLocators
from .locators import BreadcrumbsLocators
from .base import BasePage
from .base import InvalidPageException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseSearch(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def header_counter_should_show_correct_count(self):
        assert self.header_counter == 0, "Header counter shows something weird"

    def search_should_be_in_breadcrumbs(self):
        self.is_element_present(*BreadcrumbsLocators.SEARCH_BREADCRUMB)

    def _validate_page(self):
        WebDriverWait(self.browser, 5).until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded on the page")

    @property
    def header_counter(self):
        header_counter = self.browser.find_element(*SearchResultsLocators.HEADING_COUNTER).text
        header_counter_list = header_counter.split(' ')
        return int(header_counter_list[0])


class SearchResults(BaseSearch):
    _product_count = 0
    _products = {}
    _product_names = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WebDriverWait(self.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
        results = self.browser.find_elements(*SearchResultsLocators.PRODUCT_LIST)
        assert len(results) > 0, "No results found"
        count = 0
        for product in results:
            count += 1
            self._products[count] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            self._product_names[count] = product.find_element(*SearchResultsLocators.PRODUCT_NAME).text
            self._product_count += 1

    @property
    def product_count(self):
        return self._product_count

    def compare_actual_count_with_expected(self, expected_count):
        assert self._product_count == expected_count, "Actual and expected counts of results do not match"

    def header_counter_should_show_correct_count(self):
        assert self._product_count == self.header_counter, 'Header counter does not show correct result count'

    def get_product_title(self, product_number):
        return self._product_names.get(product_number)

    def open_product_page(self, product_number):
        self._products[product_number].click()


class EmptySearchResult(BaseSearch):
    def __init__(self, *args, **kwargs):
        super(EmptySearchResult, self).__init__(*args, **kwargs)

    def empty_search_text_should_be_correct(self):
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "Please enter a search keyword" == message, "Empty search alert message text does not match expected"


class NoResultSearch(BaseSearch):
    def __init__(self, *args, **kwargs):
        super(NoResultSearch, self).__init__(*args, **kwargs)

    def no_result_search_text_should_be_correct(self):
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "No results were found for your search" in message, "No search results message is not correct"
