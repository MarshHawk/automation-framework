import logging
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)

    def is_on_page(self):
        return False

    def is_page_loaded(self):
        return False

    def is_displayed(self, get_web_element):
        is_displayed = False
        try:
            is_displayed = get_web_element().is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            self.logger.info('Web element was not displayed')
        return is_displayed

    def is_on_hover_displayed(self, get_web_element):
        is_displayed = False
        try:
            is_displayed = get_web_element().is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            self.logger.info('Web element was not displayed')
        return is_displayed

    def does_element_exist(self, get_web_element):
        does_exist = False
        try:
            does_exist = get_web_element()
        except NoSuchElementException:
            self.logger.info('Web element was not displayed')
        return does_exist
