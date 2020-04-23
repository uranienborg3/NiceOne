from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


@given("I found a certain product")
def step_found_certain_product(context):
    context.execute_steps("""
   Given  I can see menu on the home page
    When  I hover over Women in menu
     And  I click T-shirts
    Then  I can see products of this category
    """)


@when("I hover over the product block")
def step_i_hover_over_product(context):
    product = context.browser.find_element_by_css_selector("ul.product_list > li")
    hover = ActionChains(context.browser).move_to_element(product)
    hover.perform()


@when("I click the More button")
def step_i_click_more(context):
    more = context.browser.find_element_by_css_selector("a.button[title = View]")
    more.click()


@then("I can see product details page")
def step_i_can_see_product_details_page(context):
    WebDriverWait(context.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
    main_pict = None
    try:
        main_pict = context.browser.find_element_by_css_selector("img#bigpic")
    except NoSuchElementException:
        pass
    assert main_pict is not None, "Product page not found"
