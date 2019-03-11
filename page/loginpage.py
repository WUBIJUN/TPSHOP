import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    user_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    pw_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title='输入用户名')
    def input_name(self,text):
        self.input_keyword(self.user_button, text)

    @allure.step(title='输入密码')
    def input_pw(self,text):
        self.input_keyword(self.pw_button, text)

    @allure.step(title='点击登录')
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title='登录成功判定')
    def is_login_success(self, expect):
        try:
            self.find_toast(expect)
            return True
        except Exception as e:
            return False

    @allure.step(title='点击登录按钮')
    def is_enabled(self):
        return self.find_element(self.login_button).get_attribute('enabled')=='true'