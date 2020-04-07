from .base import BasePage
from .base import InvalidPageException
from .locators import ShoppingCartLocators
from .locators import BreadcrumbsLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseShoppingCart(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        WebDriverWait(self.browser, 10).until(ec.title_contains, 'Order')
        if 'Order' not in self.browser.title:
            raise InvalidPageException('Shopping cart not loaded')

    def should_be_header(self):
        header = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_HEADING).text
        assert 'SHOPPING-CART SUMMARY' == header, "Something wrong with header"

    def shopping_cart_should_be_in_breadcrumbs(self):
        self.is_element_present(*BreadcrumbsLocators.SHOPPING_CART_BREADCRUMB)


class ShoppingCart(BaseShoppingCart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EmptyShoppingCart(BaseShoppingCart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def no_products_should_be_in_shopping_cart(self):
        alert_message = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_EMPTY_MESSAGE).text
        assert 'Your shopping cart is empty.' == alert_message, 'Shopping cart is not empty'
