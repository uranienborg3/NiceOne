from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.url = "http://automationpractice.com/index.php"


def after_all(context):
    context.browser.quit()
