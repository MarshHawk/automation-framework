import logging
from selenium import webdriver
from google_page import GooglePage
 
logging.basicConfig(level=logging.INFO)
   
def test_google_search_input_not_readonly(driver):
    driver.get("https://www.google.com")
    google_page = GooglePage(driver)
    expected_search_text = "True Fit"
    google_page.set_search_box_text(expected_search_text)
    actual_search_text = google_page.get_search_box_text()
    assert actual_search_text, expected_search_text        
    driver.close()

def test_google_search_button(driver):
    driver.get("https://www.google.com")
    google_page = GooglePage(driver)
    expected_search_text = "True Fit"
    google_page.set_search_box_text(expected_search_text)
    google_page.click_search()
    #TODO: assert on page       
    driver.close()