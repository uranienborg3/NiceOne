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
        return NoResultsSearch(self.browser)


class SearchBase(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        WebDriverWait(self.browser, 5). until(ec.title_contains, 'Search')
        if 'Search' not in self.browser.title:
            raise InvalidPageException("Search results not loaded")

    def return_to_home_page(self, browser):
        self.click_logo()
        from .home_page import HomePage
        return HomePage(browser)


class SearchResults(SearchBase):

    _product_count = 0
    _products = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WebDriverWait(self.browser, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
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
        assert self._product_count == expected_count, "Actual and expected counts do not match"


class NoResultsSearch(SearchBase):
    def __init__(self, *args, **kwargs):
        super(NoResultsSearch, self).__init__(*args, **kwargs)

    def empty_search_text_should_be_correct(self):
        message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                              (SearchResultsLocators.EMPTY_SEARCH_MESSAGE)).text
        assert "Please enter a search keyword" == message, "Something went wrong"
