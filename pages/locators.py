from selenium.webdriver.common.by import By


class HomePageLocators:
    """locators for home page ui"""
    BANNER = (By.ID, "homeslider")
    SEARCH_FIELD = (By.ID, "search_query_top")
    SHOPPING_CART = (By.CSS_SELECTOR, 'div.shopping_cart a')
    SHOPPING_CART_STATUS = (By.CSS_SELECTOR, ".shopping_cart span.ajax_cart_quantity")
    LOGO = (By.CSS_SELECTOR, 'img.logo.img-responsive')
    POPULAR_TAB = (By.CSS_SELECTOR, "#home-page-tabs a.homefeatured")
    BEST_SELLERS_TAB = (By.CSS_SELECTOR, "#home-page-tabs a.blockbestsellers")
    PRODUCT_LIST = (By.CSS_SELECTOR, ".product_list.active li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "a.product-name")
    PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, "a.button.ajax_add_to_cart_button")
    SIGN_IN_LINK = (By.CLASS_NAME, "login")
    ACCOUNT_LINK = (By.CLASS_NAME, "account")
    SIGN_OUT_LINK = (By.CLASS_NAME, "logout")


class ShoppingCartLocators:
    """Locators connected to shopping cart"""
    SHOPPING_CART_EMPTY_MESSAGE = (By.CLASS_NAME, 'alert')
    SHOPPING_CART_HEADING = (By.ID, 'cart_title')
    SHOPPING_CART_STEPS = (By.ID, "order_step")
    FIRST_STEP_CURRENT = (By.CSS_SELECTOR, "ul.step li.step_current.first span")
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.cart_description p.product-name a")
    PROCEED_BUTTON = (By.XPATH, "//p[contains(@class, 'cart_navigation')]/a[@title='Proceed to checkout']")


class BreadcrumbsLocators:
    """Breadcrumbs locators"""
    BREADCRUMBS = (By.CLASS_NAME, 'breadcrumb')
    SHOPPING_CART_BREADCRUMB = (By.XPATH, "//div[contains(@class, 'breadcrumb')]/span[contains(text(), 'cart')]")
    HOME_BREADCRUMB = (By.CSS_SELECTOR, '.breadcrumb a.home')
    SEARCH_BREADCRUMB = (By.XPATH, "//div[contains(@class, 'breadcrumb')]/span[text()='Search']")
    AUTHENTICATION_BREADCRUMB = (By.XPATH,
                                 "//div[contains(@class, 'breadcrumb')]/span[contains(text(), 'Authentication')]")


class SearchResultsLocators:
    """locators connected to search"""
    PRODUCT_LIST = (By.CSS_SELECTOR, "ul.product_list > li")
    PRODUCT_LINK_LIST = (By.CSS_SELECTOR, "ul.product_list > li")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h5 a.product-name")
    PRODUCT_LINK = (By.CSS_SELECTOR, "a.product_img_link")
    SEARCH_ERROR_MESSAGE = (By.CSS_SELECTOR, 'p.alert.alert-warning')
    HEADING_COUNTER = (By.CSS_SELECTOR, 'span.heading-counter')


class ProductPageLocators:
    """Product page Locators"""
    PRODUCT_PICTURE = (By.ID, "bigpic")
    PRODUCT_TITLE = (By.XPATH, "//h1[@itemprop='name']")
    CLOSE_PICTURE = (By.XPATH, "//a[@title='Close']")
    ADD_TO_CART = (By.CSS_SELECTOR, "#add_to_cart button")


class CartSummaryLocators:
    """Cart summary locators"""
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.layer_cart_product > h2")
    PRODUCT_TITLE_CART_LAYER = (By.ID, "layer_cart_product_title")
    CART_SUMMARY_COUNTER_HEADER = (By.CSS_SELECTOR, "div.layer_cart_cart > h2 > span.ajax_cart_product_txt")
    CART_SUMMARY_CROSS = (By.XPATH, '//span[@class="cross" and @title="Close window"]')
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[@title='Proceed to checkout']")


class SignInLocators:
    """Sign in page locators"""
    CREATE_ACCOUNT_FORM = (By.ID, "create-account_form")
    LOG_IN_FORM = (By.ID, "login_form")
    AUTHENTICATION_HEADER = (By.CSS_SELECTOR, "h1.page-heading")
    EMAIL_FIELD = (By.ID, "email_create")
    FIRST_NAME_FIELD = (By.ID, "customer_firstname")
    SECOND_NAME_FIELD = (By.ID, "customer_lastname")
    GENDER_CHECKBOXES = (By.XPATH, "//input[@name='id_gender']")
    PASSWORD_FIELD = (By.ID, "passwd")
    BIRTH_DAY = (By.ID, "days")
    BIRTH_YEAR = (By.ID, "years")
    BIRTH_MONTH = (By.ID, "months")
    COMPANY_FIELD = (By.ID, "company")
    FIRST_ADDRESS_FIELD = (By.ID, "address1")
    SECOND_ADDRESS_FIELD = (By.ID, "address2")
    CITY_FIELD = (By.ID, "city")
    STATE_LIST = (By.ID, "id_state")
    POSTCODE_FIELD = (By.ID, "postcode")
    ADDITIONAL_INFO_FIELD = (By.ID, "other")
    MOBILE_FIELD = (By.ID, "phone_mobile")
    HOME_PHONE_FIELD = (By.ID, "phone")
    SUBMIT_BUTTON = (By.ID, "submitAccount")
    SIGN_IN_EMAIL_FIELD = (By.ID, "email")
    SIGN_IN_PASSWORD_FIELD = (By.ID, "passwd")
    SIGN_IN_BUTTON = (By.ID, "SubmitLogin")


class AccountLocators:
    """My account page locators"""
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[@title='Orders']")
    CREDIT_SLIPS_LINK = (By.XPATH, "//a[@title='Credit slips']")
    ADDRESSES_LINK = (By.XPATH, "//a[@title='Addresses']")
    INFORMATION_LINK = (By.XPATH, "//a[@title='Information']")
    WISHLISTS_LINK = (By.XPATH, "//a[@title='My wishlists']")
    WISHLIST = (By.ID, "block-history")
    WISHLIST_NAME_FIELD = (By.ID, "name")
    WISHLIST_SAVE_BUTTON = (By.ID, "submitWishlist")
    WISHLIST_NAME = (By.XPATH, "//tr[contains(@id, 'wishlist')]/td[1]/a")
    WISHLIST_DELETE_BUTTON = (By.XPATH, "//td[@class='wishlist_delete']/a")
