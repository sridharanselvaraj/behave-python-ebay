from framework.webapp import webapp
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
import time


class EbayPage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = EbayPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

    def verify_page_title(self):
        # Electronics, Cars, Fashion, Collectibles & More | eBay
        title = self.driver.title
        print(title)
        assert title == 'Electronics, Cars, Fashion, Collectibles & More | eBay'

    def enter_search_value(self, search_text):
        self.driver.find_element_by_xpath("//input[@id='gh-ac']").send_keys(search_text)

    def select_categories(self, slt_categories):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of(self.driver.find_element_by_xpath("//*[@name='_sacat']"))
        )
        select_categorie = Select(element)
        select_categorie.select_by_visible_text(slt_categories)

    def click_search_button(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of(self.driver.find_element_by_xpath("//*[@value='Search']"))
        )
        element.click()

    def search_result_match_search_value(self, search_text):
        time.sleep(5)
        element = WebDriverWait(self.driver, 90).until(
            ec.visibility_of(
                self.driver.find_element_by_xpath("//*[@class='srp-controls__count-heading']"))
        )
        search_results = element.text
        assert search_text in search_results

    def write_search_results(self):
        time.sleep(9)
        WebDriverWait(self.driver, 60).until(
            ec.visibility_of(
                self.driver.find_element_by_xpath(
                    "//*[@id ='srp-river-results-listing1']//span[@class='s-item__price']"))
        )
        search_results = 10
        ls = []
        for i in range(1, search_results):
            title = self.driver.find_element_by_xpath(
                "//*[@id ='srp-river-results-listing" + str(i) + "']//a[@class='s-item__link']").text
            price = self.driver.find_element_by_xpath(
                "//*[@id ='srp-river-results-listing" + str(i) + "']//span[@class='s-item__price']").text.strip()
            ls.append(title)
            ls.append(price)
        with open('test.json', mode='w') as file:
            json.dump(ls, file, indent=2)

    # title = //*[@id ='srp-river-results-listing1']//a[@class='s-item__link']
    # price = //*[@id ='srp-river-results-listing1']//span[@class='s-item__price']

ebayPage = EbayPage.get_instance()
