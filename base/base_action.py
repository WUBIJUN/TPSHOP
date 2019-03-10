import yaml
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return ele

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        by, value = feature
        ele = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return ele

    def click(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).click()

    def input_keyword(self, feature, key_word, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).send_keys(key_word)

    def find_toast(self,feature, timeout, poll):
        self.find_element(feature, timeout, poll)

