from .base import BasePage
from .base import InvalidPageException
from .locators import HomePageLocators
from .locators import BreadcrumbsLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    """HomePage inherits everything from BasePage"""
    _product_links = {}
    _product_names = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = self.browser.find_elements(*HomePageLocators.PRODUCT_LIST)
        count = 0
        for product in self.products:
            count += 1
            name = product.find_element(*HomePageLocators.PRODUCT_NAME).text
            self._product_names[count] = name
            button = product.find_element(*HomePageLocators.PRODUCT_ADD_BUTTON)
            self._product_links[count] = button

    def unchangeable_elements_should_be_present(self):
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
        status = self.shopping_cart_status()
        assert status == 0, 'Shopping cart is not empty'

    def breadcrumbs_should_disappear(self):
        self.is_not_element_present(*BreadcrumbsLocators.BREADCRUMBS)

    def change_to_best_sellers_tab(self):
        current_product_list = self.browser.find_elements(*HomePageLocators.PRODUCT_LIST)
        best_sellers = self.browser.find_element(*HomePageLocators.BEST_SELLERS_TAB)
        best_sellers.click()
        new_product_list = self.browser.find_elements(*HomePageLocators.PRODUCT_LIST)
        assert new_product_list != current_product_list, "Tabs did not change, list is the same"

    def get_product_name(self, number):
        name = self._product_names.get(number)
        return name

    def add_product_to_cart(self, number):
        product_to_hover_over = self.products[number - 1]
        hover = ActionChains(self.browser).move_to_element(product_to_hover_over)
        hover.perform()
        button = self._product_links.get(number)
        button.click()

    def _validate_page(self):
        """Implemented abstract method from BasePage to validate home page"""
        try:
            self.browser.find_element(*HomePageLocators.BANNER)
        except NoSuchElementException:
            raise InvalidPageException('Home page not found')
