import pytest
from selenium import webdriver


# @pytest.fixture(scope='class')
@pytest.fixture()
def browser():
    print('\nstarting Chrome..')
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://automationpractice.com/index.php')
    yield browser
    print('\nclosing Chrome..')
    browser.quit()
