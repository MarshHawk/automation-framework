import logging
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)
        self.default_timeout_seconds = 10
        self.default_wait = WebDriverWait(driver,10)

    def is_page_loaded(self):
        self.logger.info(self.driver.execute_script("return document.readyState"))
        return True

    def is_displayed(self, get_web_element):
        is_displayed = False
        try:
            is_displayed = get_web_element().is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            self.logger.info('Web element was not displayed')
        return is_displayed

    def does_element_exist(self, get_web_element):
        does_exist = False
        try:
            self.default_wait.until(lambda d: get_web_element())
            does_exist = True
        except (NoSuchElementException, TimeoutException):
            self.logger.info('Web element was not displayed')
        return does_exist
