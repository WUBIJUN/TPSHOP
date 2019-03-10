import allure
import pytest
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    user_button = By.XPATH, "//*[@text='账号']"
    pw_button = By.XPATH, "//*[@text='密码']"
    user_word = 13830013806
    pw_word = 123456

    def input_name(self):
        self.input_keyword(self.user_word, self.user_word)

    def input_pw(self):
        self.click(self.pw_word, self.pw_word)
