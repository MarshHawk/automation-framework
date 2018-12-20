from base_page import BasePage

class GooglePage(BasePage):

    #Web elements:

    def get_search_box(self):
        return self.driver.find_element_by_css_selector("input[title='Search'")

    def get_search_button(self):
        return self.driver.find_element_by_css_selector("input[name='btnK'")
    
    #Page actions:

    def get_search_box_text(self):
        return self.get_search_box().get_attribute('value')

    def set_search_box_text(self, text_to_search):
        self.get_search_box().send_keys(text_to_search)

    def click_search(self):
        self.get_search_box().click()

    #Page conditions:

    #TODO: is_element_present_and_clickable