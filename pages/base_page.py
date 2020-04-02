from abc import abstractmethod


class BasePage:
    """All pages inherit from this"""

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self._validate_page()

    @abstractmethod
    def _validate_page(self):
        """Must be implemented in each child class"""
        return


class InvalidPageException(Exception):
    """This exception is thrown when the page is not found"""
    pass
