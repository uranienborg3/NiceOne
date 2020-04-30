import random
from pages.base import BasePage
from pages.base import InvalidPageException
from pages.locators import SignInLocators
from pages.locators import BreadcrumbsLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SignIn(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_page(self):
        """checks if there is create account and log in forms"""
        try:
            self.browser.find_element(*SignInLocators.CREATE_ACCOUNT_FORM)
            self.browser.find_element(*SignInLocators.LOG_IN_FORM)
        except NoSuchElementException:
            raise InvalidPageException("Sign page not found")

    def should_be_authentication_header(self):
        """checks if page has authentication header"""
        header = self.browser.find_element(*SignInLocators.AUTHENTICATION_HEADER).text
        assert "AUTHENTICATION" == header, "Authentication header is not correct"

    def authentication_should_be_in_breadcrumbs(self):
        """checks if authentication is followed in breadcrumbs"""
        assert self.is_element_present(*BreadcrumbsLocators.AUTHENTICATION_BREADCRUMB), \
            "Authentication not in breadcrumb"

    def enter_email(self, email):
        """find email fields and sends email into it provided as argument"""
        field = self._find(*SignInLocators.EMAIL_FIELD)
        field.send_keys(email)
        field.submit()

    def fill_in_info(self, **kwargs):
        """takes credentials as arguments and submits all of them
        into corresponding fields"""
        gender_checkboxes = WebDriverWait(self.browser, 5).until(
            ec.presence_of_all_elements_located((SignInLocators.GENDER_CHECKBOXES)))
        random.choice(gender_checkboxes).click()
        # make a list of all necessary fields in correct order
        field_locators = [SignInLocators.FIRST_NAME_FIELD,
                          SignInLocators.SECOND_NAME_FIELD,
                          SignInLocators.PASSWORD_FIELD,
                          SignInLocators.COMPANY_FIELD,
                          SignInLocators.FIRST_ADDRESS_FIELD,
                          SignInLocators.SECOND_ADDRESS_FIELD,
                          SignInLocators.CITY_FIELD,
                          SignInLocators.POSTCODE_FIELD,
                          SignInLocators.ADDITIONAL_INFO_FIELD,
                          SignInLocators.HOME_PHONE_FIELD,
                          SignInLocators.MOBILE_FIELD]
        # make a list of credentials
        values = [value for value in kwargs.values()]
        # delete the first. because it is email and it was sent in previous step
        del values[0]
        # run a loop through 2 lists
        for (field_locator, value) in zip(field_locators, values):
            # find a field with a provided locator
            field = self._find(*field_locator)
            # send provided value into the field
            field.send_keys(value)
        # run a loop through a list of select lists locators
        for locator in [SignInLocators.BIRTH_YEAR, SignInLocators.BIRTH_MONTH, SignInLocators.BIRTH_DAY,
                        SignInLocators.STATE_LIST]:
            # choose any option in select list
            self._get_random_option(*locator)

    def register_account(self):
        """submits credentials and creates account"""
        button = self._find(*SignInLocators.SUBMIT_BUTTON)
        button.click()

    def sign_in(self, email, password):
        """takes registered email and password and submits"""
        email_f = self.browser.find_element(*SignInLocators.SIGN_IN_EMAIL_FIELD)
        email_f.send_keys(email)
        password_f = self.browser.find_element(*SignInLocators.SIGN_IN_PASSWORD_FIELD)
        password_f.send_keys(password)
        button = self.browser.find_element(*SignInLocators.SIGN_IN_BUTTON)
        button.click()

    def _get_random_option(self, how, what):
        """chooses random option from the list of options of a select element"""
        select_element = Select(self.browser.find_element(how, what))
        options = select_element.options
        select_element.select_by_index(random.randint(1, len(options) - 1))

    def _find(self, how, what):
        """takes a method and a locator and returns the element"""
        element = WebDriverWait(self.browser, 3).until(ec.element_to_be_clickable((how, what)))
        return element
