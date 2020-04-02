from abc import abstractmethod
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators


class BasePage:
    """All pages inherit from this"""

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self._validate_page()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_unchangeable_elements_be_present(self):
        self._search_field_present()
        self._shopping_cart_present()
        self._logo_present()

    def _search_field_present(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_FIELD), "Search field not found"

    def _shopping_cart_present(self):
        assert self.is_element_present(*BasePageLocators.SHOPPING_CART), "Shopping cart not found"

    def _logo_present(self):
        assert self.is_element_present(*BasePageLocators.LOGO), "Logo is not found"

    @abstractmethod
    def _validate_page(self):
        """Must be implemented in each child class"""
        return


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
