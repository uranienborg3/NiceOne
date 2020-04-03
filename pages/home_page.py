from .base import BasePage
from .base import InvalidPageException
from .locators import HomePageLocators
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """HomePage inherits everything from BasePage"""

    # _banner = 'homeslider'
    # _search_field = 'search_query_top'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        """Implemented abstract method from BasePage to validate home page"""
        try:
            self.browser.find_element(*HomePageLocators.BANNER)
        except NoSuchElementException:
            raise InvalidPageException('Home page not found')
