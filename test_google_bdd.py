import pytest
from pytest_bdd import scenario, given, when, then
from google_page import GooglePage
from google_result_page import GoogleSearchResultPage

TRUE_FIT = 'True Fit'

@scenario('google.feature', 'Simple Google Search homepage smoke test')
def test_publish(google_page):
    pass
    
@given("I go to Google")
def given_init(google_page):
    pass

@when('I reach the page')
def page_init(google_page):
    assert google_page.is_on_page() == True

@then('the Google logo image will be displayed')
def log_is_displayed(google_page):
    assert google_page.is_logo_image_displayed() == True

@then('the search box will be displayed')
def search_box_is_displayed(google_page):
    assert google_page.is_search_box_displayed() == True

@then('the Google Search button will be displayed')
def search_button_is_displayed(google_page):
    assert google_page.is_search_button_displayed() == True

@then('I click the search button')
def click_search_button(google_page):
    google_page.click_search()

@then('nothing happens, I stay on the Google home page')
def verify_on_google_home_page(google_page, google_results_page):
    assert google_page.is_on_page() == True
    assert google_results_page.is_on_page() == False

@then('I type \'True Fit\' in the search box')
def type_search(google_page):
    google_page.set_search_box_text(TRUE_FIT)

@then('the displayed search box text matches what I typed')
def verify_search_text(google_page):
    actual_search_text = google_page.get_search_box_text()
    assert actual_search_text, TRUE_FIT

@then('click the search button')
def click_search(google_page):
    google_page.click_search()

@then('I arrive at the search results page')
def on_search_results_page(google_page, google_results_page):
    assert google_results_page.is_on_page() == True

@pytest.fixture("module")
def google_page(driver):
    base_url = "https://www.google.com"
    driver.get(base_url)
    yield GooglePage(driver)
    driver.close()

@pytest.fixture("function")
def google_results_page(driver):
    return GoogleSearchResultPage(driver)