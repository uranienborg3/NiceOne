from .base import BasePage
from .base import InvalidPageException
from .locators import SignInLocators
from .locators import BreadcrumbsLocators
from selenium.common.exceptions import NoSuchElementException


class SignIn(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        try:
            self.browser.find_element(*SignInLocators.CREATE_ACCOUNT_FORM)
            self.browser.find_element(*SignInLocators.LOG_IN_FORM)
        except NoSuchElementException:
            raise InvalidPageException("Sign page not found")

    def should_be_authentication_header(self):
        header = self.browser.find_element(*SignInLocators.AUTHENTICATION_HEADER).text
        assert "AUTHENTICATION" == header, "Authentication header is not correct"

    def authentication_should_be_in_breadcrumbs(self):
        assert self.is_element_present(*BreadcrumbsLocators.AUTHENTICATION_BREADCRUMB),\
            "Authentication not in breadcrumb"
