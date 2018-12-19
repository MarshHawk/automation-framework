from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# content of test_class.py
class TestFixtures(object):
    
    def test_google(self):
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = False
        driver = webdriver.Firefox(capabilities=firefox_capabilities)
        driver.get("https://www.google.com")
        driver.close()