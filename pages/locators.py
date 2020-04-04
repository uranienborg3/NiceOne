from selenium.webdriver.common.by import By


class HomePageLocators:
    BANNER = (By.ID, "homeslider")
    SEARCH_FIELD = (By.ID, "search_query_top")
    SHOPPING_CART = (By.CLASS_NAME, 'shopping_cart')
    LOGO = (By.CSS_SELECTOR, 'img.logo.img-responsive')


class SearchResultsLocators:
    PRODUCT_LIST = (By.CSS_SELECTOR, "ul.product_list > li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h5 a.product-name")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.product_img_link")
    EMPTY_SEARCH_MESSAGE = (By.CSS_SELECTOR, 'p.alert.alert-warning')

