from .locators import SearchResultsLocators
from .locators import HomePageLocators
from .base import BasePage
from .base import InvalidPageException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SearchRegion:
    def __init__(self, browser):
        self.browser = browser
        self.search_field = self.browser.find_element(*HomePageLocators.SEARCH_FIELD)

    def search_for(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()
        return SearchResults(self.browser)

    def submit_empty_search_field(self):
        self.search_field.clear()
        self.search_field.submit()
        return EmptySearchResult(self.browser)

    def search_for_unavailable_product(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()
        return NoResultSearch(self.browser)


class SearchBase(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        WebDriverWait(self.browser, 5).until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded on the page")

    def return_to_home_page(self, browser):
        self.click_logo()
        from .home_page import HomePage
        return HomePage(browser)


class SearchResults(SearchBase):
    _product_count = 0
    _products = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WebDriverWait(self.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
        results = self.browser.find_elements(*SearchResultsLocators.PRODUCT_LIST)
        assert len(results) > 0, "No results found"
        count = 0
        for product in results:
            name = product.find_element(*SearchResultsLocators.PRODUCT_NAME).text.strip()
            # print(name)
            count += 1
            name = str(count) + ' ' + name
            self._products[name] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            self._product_count += 1
        # print(self._products.keys())

    @property
    def product_count(self):
        return self._product_count

    def compare_actual_count_with_expected(self, expected_count):
        assert self._product_count == expected_count, "Actual and expected counts of results do not match"

     # TODO: open product method


class EmptySearchResult(SearchBase):
    def __init__(self, *args, **kwargs):
        super(EmptySearchResult, self).__init__(*args, **kwargs)

    def empty_search_text_should_be_correct(self):
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "Please enter a search keyword" == message, "Empty search alert message text does not match expected"


class NoResultSearch(SearchBase):
    def __init__(self, *args, **kwargs):
        super(NoResultSearch, self).__init__(*args, **kwargs)

    def no_result_search_text_should_be_correct(self):
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                        (SearchResultsLocators.SEARCH_ERROR_MESSAGE)).text
        assert "No results were found for your search" in message, "No search results message is not correct"
