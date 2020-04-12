from abc import abstractmethod
from selenium.common.exceptions import NoSuchElementException
from .locators import HomePageLocators
from .locators import BreadcrumbsLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    """All objects inherit from this"""

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self._validate_page()
        self.shopping_cart = self.browser.find_element(*HomePageLocators.SHOPPING_CART)
        self.search_field = self.browser.find_element(*HomePageLocators.SEARCH_FIELD)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @abstractmethod
    def _validate_page(self):
        """Must be implemented in each child class"""
        return

    def return_home_with_logo(self):
        logo = self.browser.find_element(*HomePageLocators.LOGO)
        logo.click()

    def return_home_with_breadcrumb(self):
        home = self.browser.find_element(*BreadcrumbsLocators.HOME_BREADCRUMB)
        home.click()

    def open_shopping_cart(self):
        self.shopping_cart.click()

    def shopping_cart_status(self):
        status = self.browser.find_element(*HomePageLocators.SHOPPING_CART_STATUS)
        if status.is_displayed() is False:
            return 0
        else:
            return int(status.text)

    def number_of_products_in_cart_should_be_as_expected(self, expected_number):
        actual_number = self.shopping_cart_status()
        assert expected_number == actual_number, "Something wrong in cart"

    def search_for(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()

    def submit_empty_search_field(self):
        self.search_field.clear()
        self.search_field.submit()

    def search_for_unavailable_product(self, search_term):
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_field.submit()

    def go_to_sign_in(self):
        sign_in_link = self.browser.find_element(*HomePageLocators.SIGN_IN_LINK)
        sign_in_link.click()

    def guest_should_be_logged_in(self):
        assert self.is_element_present(*HomePageLocators.ACCOUNT_LINK), "Account link not found"
        assert self.is_element_present(*HomePageLocators.SIGN_OUT_LINK), "Sign out link not found"


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
