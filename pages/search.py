from .locators import BasePageLocators
from .locators import SearchResultsLocators
from .base import BasePage
from .base import InvalidPageException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SearchRegion:
    def __init__(self, browser):
        self.browser = browser
        self.search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)

    def search_for(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()
        return SearchResults(self.browser)


class SearchResults(BasePage):

    _product_count = 0
    _products = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WebDriverWait(self.browser, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        results = self.browser.find_elements(*SearchResultsLocators.PRODUCT_LIST)
        count = 0
        for product in results:
            name = product.find_element(*SearchResultsLocators.PRODUCT_NAME).text.strip()
            print(name)
            count += 1
            name = str(count) + ' ' + name
            self._products[name] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            self._product_count += 1
        print(self._products.keys())

    def _validate_page(self):
        WebDriverWait(self.browser, 10). until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded")

    @property
    def product_count(self):
        return self._product_count

    def compare_actual_count_with_expected(self, expected_count):
        assert self._product_count == expected_count, "Actual and expected counts do not match"
