from selenium.webdriver.common.by import By
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

    def find_toast(self, content):
        feature = By.XPATH, "//*[contains(@text,'" + content + "')]"
        return self.find_element(feature, 5, 0.1).text

    def scorll_page_time(self, dir="down"):
        """
        滑动半屏，从3/4到1/4
        :param dir: 方向
        up：从上到下
        down：从下到上
        left：从左到右
        right：从右到左
        :return:
        """
        x = self.driver.get_windows_size()["width"]
        y = self.driver.get_windows_size()["height"]
        top_x = x * 0.5
        top_y = y * 0.75
        bottom_x = top_x
        bottom_y = y * 0.75
        left_x = x * 0.25
        left_y = y * 0.5
        right_x = x * 0.75
        right_y = left_y
        if dir == "down":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif dir == "up":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif dir == "left":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        elif dir == "right":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        else:
            raise Exception("请传入正确参数 up/down/left/right")

    def scroll_find_ele(self,feature,dir="down"):
        """
        边划边找
        :param feature:
        :return: 元素
        """
        while True:
            page_source = self.driver.page_source
            try:
                return self.find_element(feature)
            except Exception:
                self.scorll_page_time(dir="down")
                if page_source == self.driver.page_source:
                    raise Exception("滑动已到最后")
