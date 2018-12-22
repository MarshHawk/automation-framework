##TODO: This is base conftest for now
import pytest

@pytest.fixture
def driver_bootstrapper(driver):
    return driver
    #firefox_capabilities = DesiredCapabilities.FIREFOX
    #firefox_capabilities['marionette'] = False
    #return webdriver.Firefox(capabilities=firefox_capabilities)

#TODO: page factory
#TODO: default driver, default driver generator