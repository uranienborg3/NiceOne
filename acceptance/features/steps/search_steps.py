from behave import *
from selenium.webdriver.support.wait import WebDriverWait


@given("I am on the home page")
def step_i_am_on_home_page(context):
    context.browser.get(context.url)


@when("I enter {term} into search field")
def step_i_enter_search_term(context, term):
    search_field = context.browser.find_element_by_id("search_query_top")
    search_field.send_keys(term)


@when("I click search button")
def step_i_click_search(context):
    button = context.browser.find_element_by_css_selector("button.button-search")
    button.click()


@then("I can see {number} search results")
def step_i_can_see_results(context, number):
    WebDriverWait(context.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
    products = context.browser.find_elements_by_css_selector("ul.product_list > li")
    assert int(number) == len(products)
