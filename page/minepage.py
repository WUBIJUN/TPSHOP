import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_and_sign_up = By.XPATH, "//*[@text='登录/注册']"
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"
    title_bar = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"
    address_button = By.XPATH, "//*[@text='收货地址']"

    @allure.step(title='点击登录/注册')
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up)

    @allure.step(title='点击设置')
    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        try:
            assert self.get_title_bar() == "设置"
            return True
        except Exception as e:
            return False

    def get_title_bar(self):
        return self.find_element(self.title_bar).text

    def click_address(self):
        self.scroll_find_ele(self.address_button).click()
