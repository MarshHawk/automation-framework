#import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from driver_bootstrapper import web_driver

def test_fixtures(web_driver):
    web_driver.get("https://www.google.com")
    driver.close()