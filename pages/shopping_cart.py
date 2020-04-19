from pages.base import BasePage
from pages.base import InvalidPageException
from pages.locators import ShoppingCartLocators
from pages.locators import BreadcrumbsLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseShoppingCart(BasePage):
    """base for any shopping cart"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        """checks if the title of the page contains 'Order'"""
        WebDriverWait(self.browser, 10).until(ec.title_contains, 'Order')
        if 'Order' not in self.browser.title:
            raise InvalidPageException('Shopping cart not loaded')

    def should_be_shopping_cart_header(self):
        """checks if there is a 'Shopping cart' header"""
        header = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_HEADING).text
        assert 'SHOPPING-CART SUMMARY' == header, "Shopping cart header is not correct"

    def shopping_cart_should_be_in_breadcrumbs(self):
        """checks if the shopping cart is followed in breadcrumbs"""
        assert self.is_element_present(*BreadcrumbsLocators.SHOPPING_CART_BREADCRUMB), \
            "Shopping cart not in breadcrumbs"

    def should_be_steps(self):
        """checks if there is steps navigation"""
        assert self.is_element_present(*ShoppingCartLocators.SHOPPING_CART_STEPS), "Steps not found"

    def current_step_should_be_summary(self):
        """checks if 'Summary' is the first step"""
        step = self.browser.find_element(*ShoppingCartLocators.FIRST_STEP_CURRENT).text
        assert "Summary" in step, "First step is not summary"


class ShoppingCart(BaseShoppingCart):
    """shopping cart with items"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def product_should_be_in_cart(self, product_name):
        """checks if name passed as argument is in the shopping cart"""
        name = self.product_name
        assert product_name == name, "Product is not added to cart"

    @property
    def product_name(self):
        """returns product name in the shopping cart"""
        name = self.browser.find_element(*ShoppingCartLocators.PRODUCT_NAME).text
        return name

    def proceed_to_sign_in(self):
        """finds and clicks 'Proceed to sign in'"""
        button = self.browser.find_element(*ShoppingCartLocators.PROCEED_BUTTON)
        button.click()


class EmptyShoppingCart(BaseShoppingCart):
    """empty shopping cart"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def no_products_should_be_in_shopping_cart(self):
        """checks if there is correct alert message"""
        alert_message = self.browser.find_element(*ShoppingCartLocators.SHOPPING_CART_EMPTY_MESSAGE).text
        assert 'Your shopping cart is empty.' == alert_message, 'Shopping cart is not empty'
