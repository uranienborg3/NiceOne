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


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
