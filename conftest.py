import sys
import chromedriver_binary
import pytest
from _pytest._code.code import ExceptionInfo
from _pytest.runner import runtestprotocol
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from verify import Verifier, VerificationError

#Hooks:

def pytest_addoption(parser):
    parser.addoption(
        "--legacy", action="store", help="Whether or not locally installed version of Firefox is < 48"
    )

def pytest_runtest_protocol(item, nextitem):
    item.ihook.pytest_runtest_logstart(nodeid=item.nodeid, location=item.location)
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            del assertion_errors[:]
    item.ihook.pytest_runtest_logfinish(nodeid=item.nodeid, location=item.location)
    return True

def pytest_runtest_makereport(item, call):
    if call.when == 'call':
        if len(assertion_errors) > 0:
            if call.excinfo is not None:
                value = call.excinfo.value
                tb = call.excinfo.tb
                assertion_errors.append((value, tb))
            ve = VerificationError(build_errors_message())
            info_tuple = (type(ve), ve, assertion_errors[0][1])
            call.excinfo = ExceptionInfo(tup=info_tuple)

# Fixtures:

@pytest.fixture("function")
def verify():
    yield _verify

@pytest.fixture(scope="module",
                params=["chrome", "firefox"])
def driver_name(request):
    yield request.param

@pytest.fixture("module")
def driver(request, driver_name):
    use_legacy = request.config.getoption("legacy")
    if (driver_name == 'chrome'):
        return webdriver.Chrome()
    elif driver_name == 'firefox':
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = False if use_legacy else True
        return webdriver.Firefox(capabilities=firefox_capabilities)
    else:
        raise pytest.UsageError("specified driver does not exist")

# Verify

assertion_errors = []

def build_error_message():
    pass

def build_error_traceback():
    pass

def build_errors_message():
    m = "Multiple failures ({})\n".format(len(assertion_errors))
    for i, e in enumerate(assertion_errors, 1):
        m = m +"({}) ".format(i) + type(e[0]).__name__ + ": " + e[0].args[0] + "\n"
    return m

def build_errors_traceback():
    return assertion_errors[0][1]

def _verify(expected, actual):
    try:
        assert expected == actual
    except AssertionError:
        # TODO: don't write failure in conftest.py
        __tracebackhide__ = True
        ve = sys.exc_info()
        assertion_errors.append((ve[1], ve[2]))
