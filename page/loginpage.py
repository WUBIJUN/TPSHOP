import allure
import pytest
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    user_button = By.ID, "com.tpshop.malls:id/mobile_et"
    pw_button = By.ID, "com.tpshop.malls:id/pwd_et"
    login_button = By.ID, "com.tpshop.malls:id/login_tv"
    user_word = 13830013806
    pw_word = 123456

    def input_name(self):
        self.input_keyword(self.user_word, self.user_word)

    def input_pw(self):
        self.input_keyword(self.pw_word, self.pw_word)

    def click_login(self):
        self.click(self.login_button)
