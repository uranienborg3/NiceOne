from selenium.webdriver.common.by import By


class HomePageLocators:
    """locators for home page ui"""
    BANNER = (By.ID, "homeslider")
    SEARCH_FIELD = (By.ID, "search_query_top")
    SHOPPING_CART = (By.CSS_SELECTOR, 'div.shopping_cart a')
    SHOPPING_CART_EMPTY = (By.CSS_SELECTOR, 'div.shopping_cart span.ajax_cart_no_product')
    LOGO = (By.CSS_SELECTOR, 'img.logo.img-responsive')


class ShoppingCartLocators:
    SHOPPING_CART_EMPTY_MESSAGE = (By.CLASS_NAME, 'alert')
    SHOPPING_CART_HEADING = (By.ID, 'cart_title')


class BreadcrumbsLocators:
    BREADCRUMBS = (By.CLASS_NAME, 'breadcrumb')
    SHOPPING_CART_BREADCRUMB = (By.XPATH, "//div[contains(@class, 'breadcrumb')]/span[contains(text(), 'cart')]bla")
    HOME_BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb a.home')
    SEARCH_BREADCRUMB = (By.XPATH, "//div[contains(@class, 'breadcrumb')]/span[text()='Search']")


class SearchResultsLocators:
    """locators connected to search"""
    PRODUCT_LIST = (By.CSS_SELECTOR, "ul.product_list > li")
    PRODUCT_LINK_LIST = (By.CSS_SELECTOR, "ul.product_list > li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h5 a.product-name")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.product_img_link")
    SEARCH_ERROR_MESSAGE = (By.CSS_SELECTOR, 'p.alert.alert-warning')
    HEADING_COUNTER = (By.CSS_SELECTOR, 'span.heading-counter')


class ProductPageLocators:
    PRODUCT_PICTURE = (By.ID, "bigpic")
    PRODUCT_TITLE = (By.XPATH, "//h1[@itemprop='name']")