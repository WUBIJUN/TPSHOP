import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_add_address(self):
        # 判断是否登录
        # 点击我的
        self.page.home_page.click_mine()
        self.page.mine_page.click_setting()
        if not self.page.mine_page.is_login():
            self.page.login_page.input_name("13800138006")
            self.page.login_page.input_pw("123456")
            self.page.login_page.click_login()
            assert self.page.login_page.is_login_success("登录成功")

