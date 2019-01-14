import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

#Hooks:

def pytest_addoption(parser):
    parser.addoption(
        "--legacy", action="store", help="Whether or not locally installed version of Firefox is < 48"
    )

# Fixtures:

@pytest.fixture(scope="module",
                params=["chrome", "firefox"])
def driver_name(request):
    yield request.param

@pytest.fixture("module")
def driver(request, driver_name):
    use_legacy = request.config.getoption("legacy")
    if driver_name == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        #TODO: request logging fetchable config
        #chrome_capabilities = DesiredCapabilities.CHROME
        return webdriver.Chrome(options=chrome_options)
    elif driver_name == 'firefox':
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = False if use_legacy else True
        return webdriver.Firefox(capabilities=firefox_capabilities)
    else:
        raise pytest.UsageError("specified driver does not exist")
