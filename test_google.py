import logging
import pytest
from google_page import GooglePage
from google_result_page import GoogleSearchResultPage

#TODO move logging to command-line-option 
logging.basicConfig(level=logging.INFO)

class TestGoogle(object):

    def test_google_page_display_is_correct(self, google_page):
        assert google_page.is_logo_image_displayed() == True
        assert google_page.is_search_box_displayed() == True
        assert google_page.is_search_button_displayed() == True
        assert google_page.is_non_existent_element_displayed() == False
   
    def test_google_search_input_not_readonly(self, google_page):
        expected_search_text = "True Fit"
        google_page.set_search_box_text(expected_search_text)
        actual_search_text = google_page.get_search_box_text()
        assert actual_search_text, expected_search_text
        google_page.clear_search_box()
        actual_search_text = google_page.get_search_box_text()
        assert actual_search_text == ''

    def test_google_search_button(self, google_page, google_results_page):
        google_page.click_search()
        assert google_page.is_on_page() == True
        assert google_results_page.is_on_page() == False
        expected_search_text = "True Fit"
        google_page.set_search_box_text(expected_search_text)
        google_page.click_search_box()
        google_page.click_search()
        assert google_results_page.is_on_page() == True

    @pytest.fixture(scope="class")
    def google_page(self, driver_bootstrapper):
        base_url = "https://www.google.com"
        driver_bootstrapper.get(base_url)
        yield GooglePage(driver_bootstrapper)
        driver_bootstrapper.close()
    
    @pytest.fixture("function")
    def google_results_page(self, driver_bootstrapper):
        return GoogleSearchResultPage(driver_bootstrapper)