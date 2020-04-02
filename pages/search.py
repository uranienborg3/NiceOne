from .locators import BasePageLocators
from .base_page import BasePage
from .base_page import InvalidPageException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SearchRegion(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_field = self.browser.find_element(*BasePageLocators.SEARCH_FIELD)

    def search_for(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()
        return SearchResults(self.browser)

    def _validate_page(self):
        try:
            self.is_element_present(*BasePageLocators.SEARCH_FIELD)
        except NoSuchElementException:
            raise InvalidPageException("No search field found")


class SearchResults(BasePage):
    pass
