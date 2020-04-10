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

    def should_be_shopping_cart_header(self):
        header = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_HEADING).text
        assert 'SHOPPING-CART SUMMARY' == header, "Something wrong with header"

    def shopping_cart_should_be_in_breadcrumbs(self):
        assert self.is_element_present(*BreadcrumbsLocators.SHOPPING_CART_BREADCRUMB), \
            "Shopping cart not in breadcrumbs"

    def should_be_steps(self):
        assert self.is_element_present(*ShoppingCartLocators.SHOPPING_CART_STEPS), "Steps not found"

    def current_step_should_be_summary(self):
        step = self.browser.find_element(*ShoppingCartLocators.FIRST_STEP_CURRENT).text
        assert "Summary" in step, "First step is not summary"


class ShoppingCart(BaseShoppingCart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def product_should_be_in_cart(self, product_name):
        name = self.product_name
        assert product_name == name, "Product is not added to cart"

    @property
    def product_name(self):
        name = self.browser.find_element(*ShoppingCartLocators.PRODUCT_NAME).text
        return name

    def proceed_to_sign_in(self):
        button = self.browser.find_element(*ShoppingCartLocators.PROCEED_BUTTON)
        button.click()


class EmptyShoppingCart(BaseShoppingCart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def no_products_should_be_in_shopping_cart(self):
        alert_message = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_EMPTY_MESSAGE).text
        assert 'Your shopping cart is empty.' == alert_message, 'Shopping cart is not empty'
