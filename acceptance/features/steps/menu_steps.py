from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@given("I can see menu on the home page")
def step_i_can_see_menu_on_home_page(context):
    context.browser.get(context.url)
    WebDriverWait(context.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
    context.browser.find_element_by_css_selector("ul.menu-content")


@when("I hover over Women in menu")
def step_i_hover_over_women(context):
    women_menu = context.browser.find_element_by_css_selector("a[title=Women]")
    hover = ActionChains(context.browser).move_to_element(women_menu)
    hover.perform()


@when("I click T-shirts")
def step_i_click_t_shirts(context):
    t_shits = context.browser.find_element_by_css_selector("a[title=T-shirts]")
    t_shits.click()


@then("I can see products of this category")
def step_i_can_see_products(context):
    WebDriverWait(context.browser, 10).until(lambda b: b.execute_script("return document.readyState") == "complete")
    context.browser.find_elements_by_css_selector("ul.product_list > li")
