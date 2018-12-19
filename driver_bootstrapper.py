import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def web_driver():
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = False
    return webdriver.Firefox(capabilities=firefox_capabilities)