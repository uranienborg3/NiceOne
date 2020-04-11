import time
import random
from .base import BasePage
from .base import InvalidPageException
from .locators import SignInLocators
from .locators import BreadcrumbsLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


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

    def enter_email(self, email):
        field = self._find(*SignInLocators.EMAIL_FIELD)
        field.send_keys(email)
        field.submit()

    def fill_in_info(self, name, surname, passwd, company, add_1, add_2, city, postcode, add_info, home_phone, mobile):
        gender_checkboxes = WebDriverWait(self.browser, 5).until(ec.presence_of_all_elements_located
                                                                 ((SignInLocators.GENDER_CHECKBOXES)))
        random.choice(gender_checkboxes).click()
        first_name_field = self._find(*SignInLocators.FIRST_NAME_FIELD)
        first_name_field.send_keys(name)
        second_name_field = self._find(*SignInLocators.SECOND_NAME_FIELD)
        second_name_field.send_keys(surname)
        password = self._find(*SignInLocators.PASSWORD_FIELD)
        password.send_keys(passwd)
        self._get_random_option(*SignInLocators.BIRTH_YEAR)
        self._get_random_option(*SignInLocators.BIRTH_MONTH)
        self._get_random_option(*SignInLocators.BIRTH_DAY)
        company_f = self._find(*SignInLocators.COMPANY_FIELD)
        company_f.send_keys(company)
        address_1 = self._find(*SignInLocators.FIRST_ADDRESS_FIELD)
        address_1.send_keys(add_1)
        address_2 = self._find(*SignInLocators.SECOND_ADDRESS_FIELD)
        address_2.send_keys(add_2)
        city_f = self._find(*SignInLocators.CITY_FIELD)
        city_f.send_keys(city)
        self._get_random_option(*SignInLocators.STATE_LIST)
        postcode_f = self._find(*SignInLocators.POSTCODE_FIELD)
        postcode_f.send_keys(postcode)
        add_info_f = self._find(*SignInLocators.ADDITIONAL_INFO_FIELD)
        add_info_f.send_keys(add_info)
        home_phone_f = self._find(*SignInLocators.HOME_PHONE_FIELD)
        home_phone_f.send_keys(home_phone)
        mobile_f = self._find(*SignInLocators.MOBILE_FIELD)
        mobile_f.send_keys(mobile)
        time.sleep(4)

    def register_account(self):
        button = self._find(*SignInLocators.SUBMIT_BUTTON)
        button.click()

    def sign_in(self, email, password):
        email_f = self._find(*SignInLocators.SIGN_IN_EMAIL_FIELD)
        email_f.send_keys(email)
        passwd_f = self._find(*SignInLocators.SIGN_IN_PASSWORD_FIELD)
        passwd_f.send_keys(password)
        button = self._find(*SignInLocators.SIGN_IN_BUTTON)
        button.click()

    def _get_random_option(self, how, what):
        select_element = Select(self.browser.find_element(how, what))
        options = select_element.options
        select_element.select_by_index(random.randint(1, len(options)-1))

    def _find(self, how, what):
        element = self.browser.find_element(how, what)
        return element
