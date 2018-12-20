import logging
from base_page import BasePage

class GooglePage(BasePage):

    def __init__(self, driver):
        super(GooglePage, self).__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    #Web elements:

    def __get_search_box(self):
        return self.driver.find_element_by_css_selector("input[title='Search'")

    def __get_search_button(self):
        return self.driver.find_element_by_css_selector("input[name='btnK'")
    
    #Page actions:

    def get_search_box_text(self):
        self.logger.info('getting value of search box text')
        return self.__get_search_box().get_attribute('value')

    def set_search_box_text(self, text_to_search):
        self.logger.info('typing {} in search box'.format(text_to_search))
        self.__get_search_box().send_keys(text_to_search)

    def click_search(self):
        self.logger.info('clicking search button')
        self.__get_search_box().click()

    #Page conditions:

    #TODO: is_element_present_and_clickable