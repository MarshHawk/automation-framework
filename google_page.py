import logging
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class GooglePage(BasePage):

    def __init__(self, driver):
        super(GooglePage, self).__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    #Web elements:

    def __get_logo_image(self):
        return self.driver.find_element_by_css_selector("#hplogo")

    def __get_search_box(self):
        return self.driver.find_element_by_css_selector("input[title='Search']")

    def __get_search_button(self):
        return self.driver.find_elements_by_css_selector("input[name='btnK']")[1]

    def __get_not_existing_element(self):
        return self.driver.find_element_by_css_selector("#not_existerr")
    
    #Page actions:

    def get_search_box_text(self):
        self.logger.info('getting value of search box text')
        return self.__get_search_box().get_attribute('value')

    def set_search_box_text(self, text_to_search):
        self.logger.info('typing {} in search box'.format(text_to_search))
        self.__get_search_box().send_keys(text_to_search)

    def click_search(self):
        self.logger.info('clicking search button')
        ActionChains(self.driver).move_to_element(self.__get_search_button()).click().perform()

    #Page conditions:

    def is_logo_image_displayed(self):
        self.logger.info('Checking if logo displayed')
        return self.is_displayed(self.__get_logo_image)

    def is_search_box_displayed(self):
        self.logger.info('Checking if search box displayed')
        return self.is_displayed(self.__get_search_box)

    def is_search_button_displayed(self):
        self.logger.info('Checking if search button displayed')
        return self.is_displayed(self.__get_search_button)

    def is_non_existent_element_displayed(self):
        self.logger.info('Checking if non-existent element displayed')
        return self.is_displayed(self.__get_not_existing_element)