import pytest
import random
import json
import datetime
from faker import Faker
from pages.locators import SignInLocators
from pages.locators import HomePageLocators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='choose browser: firefox/chrome')


@pytest.fixture(scope="function")
def browser(request):
    """opens the browser at the beginning of a test
    and closes at the end of a test"""
    browser_name = request.config.getoption('browser')
    # browser = None
    if browser_name == 'firefox':
        print('\nstarting Firefox..')
        browser = webdriver.Firefox()
    else:
        print('\nstarting Chrome..')
        browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://automationpractice.com/index.php')
    yield browser
    print('\nclosing browser..')
    browser.quit()


@pytest.fixture(scope="function")
def register():
    """creates credentials for registering a user
    and saves them into a json file"""
    fake = Faker()
    data = {"email": str(random.randint(1, 100)) + fake.email(),
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "password": fake.password(length=5, special_chars=False),
            "address_1": fake.street_address(),
            "address_2": fake.secondary_address(),
            "city": fake.city(),
            "postcode": fake.postcode(),
            "company": fake.company(),
            "mobile": "+1" + str(random.random())[-10:],
            "home_phone": "+1" + str(random.random())[-10:],
            "add_info": fake.sentence(nb_words=10)}
    with open("test_data_" + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + ".json", "w") as f:
        json.dump(data, f, sort_keys=True, indent=2)
    return data


@pytest.fixture(scope="function")
def get_credentials():
    """loads credentials from json file
    returns email and password for signing in"""
    with open("test_data_20200411_212033.json") as f:
        data = json.load(f)
    email = data.get('email')
    password = data.get('password')
    return email, password


@pytest.fixture(scope="function")
def sign_in(browser, get_credentials):
    """gets credentials and signs the user in"""
    email, password = get_credentials
    browser.find_element(*HomePageLocators.SIGN_IN_LINK).click()
    email_f = WebDriverWait(browser, 5).until(ec.presence_of_element_located((SignInLocators.SIGN_IN_EMAIL_FIELD)))
    email_f.send_keys(email)
    password_f = browser.find_element(*SignInLocators.SIGN_IN_PASSWORD_FIELD)
    password_f.send_keys(password)
    button = browser.find_element(*SignInLocators.SIGN_IN_BUTTON)
    button.click()
