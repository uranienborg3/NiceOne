from .base import BasePage
from .base import InvalidPageException
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        except NoSuchElementException:
            raise InvalidPageException('Product page not found')

    def product_title_should_be_correct(self, expected_name):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert expected_name == title, "Titles do not match"
