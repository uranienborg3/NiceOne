from .base import BasePage
from .base import InvalidPageException
from .locators import HomePageLocators
from .locators import ShoppingCartLocators
from selenium.common.exceptions import NoSuchElementException


class HomePage(BasePage):
    """HomePage inherits everything from BasePage"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_unchangeable_elements_be_present(self):
        self._search_field_present()
        self._shopping_cart_present()
        self._logo_present()

    def _search_field_present(self):
        assert self.is_element_present(*HomePageLocators.SEARCH_FIELD), "Search field not found"

    def _shopping_cart_present(self):
        assert self.is_element_present(*HomePageLocators.SHOPPING_CART), "Shopping cart not found"

    def _logo_present(self):
        assert self.is_element_present(*HomePageLocators.LOGO), "Logo is not found"

    def shopping_cart_should_be_empty(self):
        shopping_card_status = self.browser.find_element(*HomePageLocators.SHOPPING_CART_EMPTY).text
        assert 'empty' in shopping_card_status, 'Shopping cart is not empty'

    def _validate_page(self):
        """Implemented abstract method from BasePage to validate home page"""
        try:
            self.browser.find_element(*HomePageLocators.BANNER)
        except NoSuchElementException:
            raise InvalidPageException('Home page not found')
