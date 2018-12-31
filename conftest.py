import sys
import pytest
from _pytest._code.code import ExceptionInfo
from _pytest.runner import runtestprotocol
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from verify import Verifier, VerificationError

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

def __verify(expected, actual):
    try:
        assert expected == actual
    except AssertionError:
        ve = sys.exc_info()
        assertion_errors.append((ve[1], ve[2]))

#Hooks:
#TODO: don't write failure in conftest.py
#def pytest_runtest_logstart()
#def pytest_runtest_call
#def pytest_make_collect_report(collector):   
#def pytest_runtest_makereport(item, call):

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

#Fixtures:

@pytest.fixture("function")
def verify():
    yield __verify

@pytest.fixture("module")
def driver_bootstrapper(request):
    driver_name = request.config.getoption("driver")
    #Need a default
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
