from .base import BasePage
from .base import InvalidPageException
from .locators import ShoppingCartLocators
from .locators import HomePageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ShoppingCartRegion:
    def __init__(self, browser):
        self.browser = browser
        self.shopping_cart = self.browser.find_element(*HomePageLocators.SHOPPING_CART)

    def open(self):
        return

    def open_empty(self):
        self.shopping_cart.click()
        return ShoppingCartEmpty(self.browser)


class ShoppingCartBase(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        WebDriverWait(self.browser, 10).until(ec.title_contains, 'Order')
        if 'Order' not in self.browser.title:
            raise InvalidPageException('Shopping cart not loaded')


class ShoppingCart(ShoppingCartBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ShoppingCartEmpty(ShoppingCartBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def no_products_should_be_in_shopping_cart(self):
        alert_message = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_EMPTY_MESSAGE).text
        assert 'Your shopping cart is empty.' == alert_message, 'Shopping cart is not empty'
