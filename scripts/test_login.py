import time

import pytest

from base.base_action import BaseAction
from base.base_driver import init_driver
from page.page import Page


class TestLogin(BaseAction):
    def setup(self):
        self.drive = init_driver()
        self.page = Page(self.drive)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()
    def test_login(self):
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_page.input_name()
        self.page.login_page.input_pw()
