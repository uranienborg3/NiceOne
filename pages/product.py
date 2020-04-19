from pages.base import BasePage
from pages.base import InvalidPageException
from pages.locators import ProductPageLocators
from pages.locators import CartSummaryLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        """checks if huge main product picture is present"""
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        except NoSuchElementException:
            raise InvalidPageException('Product page not found')

    def product_title_should_be_correct(self, expected_name):
        """checks if name of product matches with expected provided as argument"""
        assert expected_name == self.product_name, "Titles do not match"

    def open_product_picture(self):
        """clicks main product picture"""
        picture = self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        picture.click()

    def close_product_picture(self):
        """clicks 'x' on open main product picture"""
        cross = self.browser.find_element(*ProductPageLocators.CLOSE_PICTURE)
        cross.click()

    def add_to_cart(self):
        """finds and clicks add to cart link and returns CartSummary instance"""
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        return CartSummary(self.browser)

    @property
    def product_name(self):
        """returns product name"""
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return title


class CartSummary(ProductPage):
    _product_summary_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # get success message that appears after adding product to the cart in short summary
        self.success_message = WebDriverWait(self.browser, 10).until(
            ec.visibility_of_element_located((CartSummaryLocators.SUCCESS_MESSAGE))).text
        # get the product name that appears in short summary
        self.name = self.browser.find_element(*CartSummaryLocators.PRODUCT_TITLE_CART_LAYER).text
        # counter displays number of product added to cart
        counter = self.browser.find_element(*CartSummaryLocators.CART_SUMMARY_COUNTER_HEADER).text
        counter_list = counter.split()
        self._product_summary_count = int(counter_list[2])  # extract the number from the counter string

    def product_is_added_to_cart(self, product_name, expected_count):
        """check if product added to cart is in short summary"""
        assert "Product successfully added to your shopping cart" == self.success_message, \
            "Product added success message is not correct"
        name = self.browser.find_element(*CartSummaryLocators.PRODUCT_TITLE_CART_LAYER).text
        assert product_name == name, "Product names do not match in cart summary"
        assert expected_count == self._product_summary_count, "Count in cart is not correct"

    def close_cart_summary(self):
        """closes short summary"""
        cross = self.browser.find_element(*CartSummaryLocators.CART_SUMMARY_CROSS)
        cross.click()

    def go_to_checkout(self):
        """finds and clicks go to checkout button in th short cart summary"""
        button = self.browser.find_element(*CartSummaryLocators.PROCEED_TO_CHECKOUT_BUTTON)
        button.click()

    def _validate_page(self):
        """checks if product counter is in the short summary"""
        try:
            self.browser.find_element(*CartSummaryLocators.CART_SUMMARY_COUNTER_HEADER)
        except NoSuchElementException:
            raise InvalidPageException('Product Summary not found')
