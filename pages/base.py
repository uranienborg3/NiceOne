from abc import abstractmethod
from selenium.common.exceptions import NoSuchElementException
from pages.locators import HomePageLocators
from pages.locators import BreadcrumbsLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


class BasePage:
    """All objects inherit from this"""

    def __init__(self, browser, timeout=10):
        """takes a WebDriver instance"""
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self._validate_page()  # method is implemented in each class that inherits from this
        self.shopping_cart = self.browser.find_element(*HomePageLocators.SHOPPING_CART)
        self.search_field = self.browser.find_element(*HomePageLocators.SEARCH_FIELD)
        self.search_button = self.browser.find_element(*HomePageLocators.SEARCH_BUTTON)

    def is_element_present(self, how, what):
        """returns True if driver can find element on page
        and with NoSuchElementException returns false"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=3):
        """checks for the period of timeout if an element is present on the page,
        after timeout returns True if the element was not detected,
        after timeout returns False if the element was detected"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=3):
        """checks if the element has disappeared from the page
        returns False if the element is still detected after the timeout
        returns True if element is no longer detected after timeout,
        ignores TimeOutException"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    @abstractmethod
    def _validate_page(self):
        """Must be implemented on each page"""
        return

    def return_home_with_logo(self):
        """finds and clicks logo link"""
        logo = self.browser.find_element(*HomePageLocators.LOGO)
        logo.click()

    def return_home_with_breadcrumb(self):
        """finds and clicks home link in the breadcrumbs"""
        home = self.browser.find_element(*BreadcrumbsLocators.HOME_BREADCRUMB)
        home.click()

    def open_shopping_cart(self):
        """finds and clicks shopping cart"""
        self.shopping_cart.click()

    def shopping_cart_status(self):
        """returns the number of items in the shopping cart:
        0 if there is no items"""
        status = self.browser.find_element(*HomePageLocators.SHOPPING_CART_STATUS)
        if status.is_displayed() is False:  # if status element is not displayed, the cart is empty
            return 0
        else:
            return int(status.text)

    def number_of_products_in_cart_should_be_as_expected(self, expected_number):
        """gets the number of items in shopping cart
        and compares it with the number passed as an argument"""
        actual_number = self.shopping_cart_status()
        assert expected_number == actual_number, "Number of items in cart does not meet expected number"

    def search_for(self, search_term):
        """finds search field, clears its content, and sends
        the string passed as an argument into the search field"""
        self.search_field.clear()
        self.search_field.send_keys(search_term)
        self.search_button.click()

    def submit_empty_search_field(self):
        """finds and submits the empty search field"""
        self.search_field.clear()
        self.search_button.click()

    def go_to_sign_in(self):
        """finds sign in link and clicks it"""
        sign_in_link = self.browser.find_element(*HomePageLocators.SIGN_IN_LINK)
        sign_in_link.click()

    def guest_should_be_logged_in(self):
        """checks if the user is signed in"""
        assert self.is_element_present(*HomePageLocators.ACCOUNT_LINK), "Account link not found"
        assert self.is_element_present(*HomePageLocators.SIGN_OUT_LINK), "Sign out link not found"


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
