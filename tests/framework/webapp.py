from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from data.config import settings
from urllib.parse import urljoin


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
            return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_driver(self):
        return self.driver

    def load_website(self):
        # Code for loading website
        self.driver.get(settings['url'])

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page))

    def verify_component_exists(self, component):
        # Simple implementation
        assert component in self.driver.find_element_by_tag_name('body').text, \
            "Component {} not found on page".format(component)

    def close_browser(self):
        return self.driver.quit()


webapp = WebApp.get_instance()
