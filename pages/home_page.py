from pages.base import BasePage
from pages.base import InvalidPageException
from pages.locators import HomePageLocators
from pages.locators import BreadcrumbsLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    """inherits everything from BasePage"""
    _product_add_buttons = {}  # key is number of product and value is add to cart link element
    _product_names = {}  # key is number of product and value is product name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.products = self.browser.find_elements(
            *HomePageLocators.PRODUCT_LIST)  # find all product blocks on home page
        count = 0
        for product in self.products:
            count += 1
            name = product.find_element(*HomePageLocators.PRODUCT_NAME).text  # find name for each product
            self._product_names[count] = name
            button = product.find_element(*HomePageLocators.PRODUCT_ADD_BUTTON)  # find link for each product
            self._product_add_buttons[count] = button

    def unchangeable_elements_should_be_present(self):
        """checks if logo, search, and shopping cart are on home page"""
        self._search_field_present()
        self._shopping_cart_present()
        self._logo_present()

    def _search_field_present(self):
        """checks if search field is present"""
        assert self.is_element_present(*HomePageLocators.SEARCH_FIELD), "Search field not found"

    def _shopping_cart_present(self):
        """checks if shopping cart is present"""
        assert self.is_element_present(*HomePageLocators.SHOPPING_CART), "Shopping cart not found"

    def _logo_present(self):
        """checks if logo is present"""
        assert self.is_element_present(*HomePageLocators.LOGO), "Logo is not found"

    def shopping_cart_should_be_empty(self):
        """gets number of products in shopping cart without opening it
        and checks if nothing is in there"""
        status = self.shopping_cart_status()
        assert status == 0, 'Shopping cart is not empty'

    def breadcrumbs_should_disappear(self):
        """checks if breadcrumbs are not on home page"""
        self.is_not_element_present(*BreadcrumbsLocators.BREADCRUMBS)

    def change_to_best_sellers_tab(self):
        """changes b;lock of products to best sellers"""
        current_product_list = self.browser.find_elements(
            *HomePageLocators.PRODUCT_LIST)  # create a list of current items on home page
        self._change_tab(*HomePageLocators.BEST_SELLERS_TAB)  # click another tab
        new_product_list = self.browser.find_elements(*HomePageLocators.PRODUCT_LIST)  # create a new product list
        # compare the lists to make sure tabs have changed
        assert new_product_list != current_product_list, "Tabs did not change, product list is the same"

    def change_to_popular_tab(self):
        current_product_list = self.browser.find_elements(
            *HomePageLocators.PRODUCT_LIST)  # create a list of current items on home page
        self._change_tab(*HomePageLocators.POPULAR_TAB)  # click another tab
        new_product_list = self.browser.find_elements(*HomePageLocators.PRODUCT_LIST)  # create a new product list
        # compare the lists to make sure tabs have changed
        assert new_product_list != current_product_list, "Tabs did not change"

    def _change_tab(self, how, what):
        """finds a tab and clicks it"""
        tab = self.browser.find_element(how, what)
        tab.click()

    def get_product_name(self, number):
        """gets name of the product number of which is provided as argument"""
        name = self._product_names.get(number)
        return name

    def add_product_to_cart(self, number):
        """hovers over the product which number is provided as argument and adds it to cart"""
        product_to_hover_over = self.products[number - 1]  # get product block from the list
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", product_to_hover_over)
        # button = self._product_add_buttons.get(number)
        hover = ActionChains(self.browser).move_to_element(product_to_hover_over)  # create hover action
        hover.perform()
        button = self._product_add_buttons.get(number)  # get the add button from the list
        button.click()

    def _validate_page(self):
        """checks if promo banner is present on the gage"""
        try:
            self.browser.find_element(*HomePageLocators.BANNER)
        except NoSuchElementException:
            raise InvalidPageException('Home page not found')
