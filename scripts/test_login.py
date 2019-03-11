import time,pytest
from base.base_analyze import analyze_file_values
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file_values("login_data", "test_login"))
    def test_login(self,args):
        phone = args["phone"]
        password = args["password"]
        expect = args["expect"]
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_page.input_name(phone)
        self.page.login_page.input_pw(password)
        self.page.login_page.click_login()
        assert self.page.login_page.is_login_success(expect)

    @pytest.mark.parametrize("args", analyze_file_values("login_data", "test_login_null"))
    def test_login_null(self, args):
        phone = args["phone"]
        password = args["password"]
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_and_sign_up()
        self.page.login_page.input_name(phone)
        self.page.login_page.input_pw(password)
        self.page.login_page.click_login()
        assert not self.page.login_page.is_enabled()
#
#
