from pages.base import BasePage
from pages.base import InvalidPageException
from pages.locators import AccountLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AccountPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        """checks if 'My account is in t the page title'"""
        WebDriverWait(self.browser, 5).until(ec.title_contains("My account"))
        if "My account" not in self.browser.title:
            raise InvalidPageException("Account page not found")

    def go_to_wishlist(self):
        """finds and clicks wishlists link"""
        assert self.is_element_present(*AccountLocators.WISHLISTS_LINK), "Wishlists link not found"
        wishlist = self.browser.find_element(*AccountLocators.WISHLISTS_LINK)
        wishlist.click()

    def wishlist_should_be_empty(self):
        """checks if there are no saved wishlists"""
        assert self.is_disappeared(
            *AccountLocators.WISHLIST), "Wishlist is not empty"  # deleted wishlist disappears not straight away

    def there_should_be_wishlist(self):
        """checks if there are wishlists"""
        WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located((AccountLocators.WISHLIST)))

    def create_wishlist(self, name):
        """finds a field, sends the name provided as argument
        and clicks save"""
        name_f = self.browser.find_element(*AccountLocators.WISHLIST_NAME_FIELD)
        name_f.send_keys(name)
        button = self.browser.find_element(*AccountLocators.WISHLIST_SAVE_BUTTON)
        button.click()

    def delete_wishlist(self, name):
        """finds the wishlist with the name passed as argument and deletes it"""
        wishlists = self.browser.find_elements(*AccountLocators.WISHLIST)
        wishlist_to_de_deleted = None
        for wishlist in wishlists:
            wishlist_name = wishlist.find_element(*AccountLocators.WISHLIST_NAME).text  # find the name of wishlist
            if wishlist_name == name:
                wishlist_to_de_deleted = wishlist
        if wishlist_to_de_deleted is None:
            raise NoSuchNameException("No wishlist with such name found")  # if wishlist was not found raise exception
        button = wishlist_to_de_deleted.find_element(*AccountLocators.WISHLIST_DELETE_BUTTON)
        button.click()
        alert = self.browser.switch_to.alert  # alert must appear
        alert.accept()


class NoSuchNameException(Exception):
    pass
