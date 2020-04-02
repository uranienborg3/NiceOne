from .locators import BasePageLocators
from .locators import SearchResultsLocators
from .base_page import BasePage
from .base_page import InvalidPageException
# from selenium.common.exceptions import NoSuchElementException
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
        results = WebDriverWait(self.browser, 10, 3).until(ec.visibility_of_all_elements_located
                                                          (SearchResultsLocators.PRODUCT_LIST), 'Results not found')
        count = 0
        for product in results:
            name = product.find_element(*SearchResultsLocators.PRODUCT_NAME).text.strip()
            print(name)
            if name not in self._products.keys():
                self._products[name] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            else:
                self._products[name + ' ' + str(count)] = product.find_element(*SearchResultsLocators.PRODUCT_LINK)
            self._product_count += 1
            count += 1
        print(len(self._products))
        print(self._product_count)
        print(self._products.keys())

    def _validate_page(self):
        WebDriverWait(self.browser, 10). until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded")

    @property
    def product_count(self):
        return self._product_count
