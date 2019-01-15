import logging
from base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class GooglePage(BasePage):

    def __init__(self, driver):
        super(GooglePage, self).__init__(driver)
        self.logger = logging.getLogger(self.__class__.__name__)

    #Web elements:

    def __get_page_class(self):
        return self.driver.find_element_by_css_selector("#gsr.hp")

    def __get_logo_image(self):
        return self.driver.find_element_by_css_selector("#hplogo")

    def __get_search_box(self):
        return self.driver.find_element_by_css_selector("input[title='Search']")

    def __get_search_button(self):
        return self.driver.find_elements_by_css_selector("input[name='btnK']")[-1]
    
    #Page actions:

    def get_search_box_text(self):
        self.logger.info('getting value of search box text')
        return self.__get_search_box().get_attribute('value')

    def set_search_box_text(self, text_to_search):
        self.logger.info('typing {} in search box'.format(text_to_search))
        we = self.__get_search_box()
        we.send_keys(text_to_search)
        we.send_keys(Keys.TAB)

    def click_search_box(self):
        self.logger.info('clicking search box')
        self.__get_search_box().click()

    def clear_search_box(self):
        self.logger.info('clearing search box')
        self.__get_search_box().clear()
        
    def click_search(self):
        self.logger.info('clicking search button')
        ActionChains(self.driver).move_to_element(self.__get_search_button()).click().perform()

    #Page conditions:

    def is_on_page(self):
        self.logger.info('Verifying if current page is Google homepage')
        return self.does_element_exist(self.__get_page_class)

    def is_logo_image_displayed(self):
        self.logger.info('Checking if logo displayed')
        return self.is_displayed(self.__get_logo_image)

    def is_search_box_displayed(self):
        self.logger.info('Checking if search box displayed')
        return self.is_displayed(self.__get_search_box)

    def is_search_button_displayed(self):
        self.logger.info('Checking if search button displayed')
        return self.is_displayed(self.__get_search_button)