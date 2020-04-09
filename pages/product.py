from .base import BasePage
from .base import InvalidPageException
from .locators import ProductPageLocators
from .locators import CartSummaryLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        except NoSuchElementException:
            raise InvalidPageException('Product page not found')

    def product_title_should_be_correct(self, expected_name):
        assert expected_name == self.product_name, "Titles do not match"

    def open_product_picture(self):
        picture = self.browser.find_element(*ProductPageLocators.PRODUCT_PICTURE)
        picture.click()

    def close_product_picture(self):
        cross = self.browser.find_element(*ProductPageLocators.CLOSE_PICTURE)
        cross.click()

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        return CartSummary(self.browser)

    @property
    def product_name(self):
        title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        return title


class CartSummary(ProductPage):
    _product_summary_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success_message = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located
                                                                     ((CartSummaryLocators.SUCCESS_MESSAGE))).text
        self.name = self.browser.find_element(*CartSummaryLocators.PRODUCT_TITLE_CART_LAYER).text
        counter = self.browser.find_element(*CartSummaryLocators.CART_SUMMARY_COUNTER_HEADER).text
        counter_list = counter.split(' ')
        self._product_summary_count = int(counter_list[2])

    def product_is_added_to_cart(self, product_name, expected_count):
        assert "Product successfully added to your shopping cart" == self.success_message, \
            "Product added success message is not correct"
        name = self.browser.find_element(*CartSummaryLocators.PRODUCT_TITLE_CART_LAYER).text
        assert product_name == name, "Product names do not match in cart summary"
        assert expected_count == self._product_summary_count, "Count in cart is not correct"

    def close_cart_summary(self):
        cross = self.browser.find_element(*CartSummaryLocators.CART_SUMMARY_CROSS)
        cross.click()

