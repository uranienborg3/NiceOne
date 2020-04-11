from .base import BasePage
from .base import InvalidPageException
# from .locators import AccountLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccountPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        WebDriverWait(self.browser, 5).until(ec.title_contains("My account"))
        if "My account" not in self.browser.title:
            raise InvalidPageException("Account page not found")
