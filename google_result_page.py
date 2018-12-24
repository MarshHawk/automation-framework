import logging
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class GoogleSearchResultPage(BasePage):

    def __init__(self, driver):
        super(GoogleSearchResultPage, self).__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    #Web elements:

    def __get_page_class(self):
        return self.driver.find_element_by_css_selector("#gsr.srp")

    def __get_search_box(self):
        return self.driver.find_element_by_css_selector("input[title='Search']")

    #Page actions:

    def get_search_box_text(self):
        self.logger.info('getting value of search box text')
        return self.__get_search_box().get_attribute('value')

    #Page conditions:

    def is_on_page(self):
        self.logger.info('Verifying if current page is Google Search Results')
        return self.does_element_exist(self.__get_page_class)