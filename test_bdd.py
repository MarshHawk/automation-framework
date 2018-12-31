import pytest
import logging
from pytest_bdd import scenario, given, when, then
from google_page import GooglePage

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('')

@scenario('bdd.feature', 'BDD')
def test_publish():
    pass
    
@given("I BDD")
def i_b():
    log.info('given')

@when('I BDD')
def i_d():
    log.info('when')

@then('I BDD')
def log_is_displayed():
    log.info('then')

@then('I BDD again')
def search_box_is_displayed():
    log.info('and')