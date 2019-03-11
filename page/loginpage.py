from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):
    user_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    pw_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_name(self,text):
        self.input_keyword(self.user_button, text)

    def input_pw(self,text):
        self.input_keyword(self.pw_button, text)

    def click_login(self):
        self.click(self.login_button)

    def is_login(self,key_word):
        try:
            self.find_toast(key_word)
            return True
        except Exception as e:
            return False