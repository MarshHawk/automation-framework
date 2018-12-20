class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def is_on_page(self):
        return False

    def is_page_loaded(self):
        return False