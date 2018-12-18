from selenium import webdriver

# content of test_class.py
class TestGoogle(object):

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
    
    def test_google(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")
        driver.close()