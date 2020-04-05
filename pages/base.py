from abc import abstractmethod
from selenium.common.exceptions import NoSuchElementException
from .locators import HomePageLocators


class BasePage:
    """All objects inherit from this"""

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

    @abstractmethod
    def _validate_page(self):
        """Must be implemented in each child class"""
        return

    @property
    def search(self):
        from .search import SearchRegion
        return SearchRegion(self.browser)

    @property
    def shopping_cart(self):
        from .shopping_cart import ShoppingCartRegion
        return ShoppingCartRegion(self.browser)

    def click_logo(self):
        logo = self.browser.find_element(*HomePageLocators.LOGO)
        logo.click()


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
