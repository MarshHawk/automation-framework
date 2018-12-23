import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture("module")
def driver_bootstrapper(request):
    driver_name = request.config.getoption("driver")
    if driver_name is None:
        raise pytest.UsageError("no default driver specified")
    driver_name= driver_name.lower()
    if (driver_name == 'firefox-legacy'):
        #For legacy firefox ESR and version < 48
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = False
        return webdriver.Firefox(capabilities=firefox_capabilities)
    elif (driver_name == 'chrome'):
        webdriver.Chrome()
    elif driver_name == 'firefox':
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        return webdriver.Firefox(capabilities=firefox_capabilities)
    else:
        #need default
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        return webdriver.Firefox(capabilities=firefox_capabilities)