from page.homepage import HomePage
from page.loginpage import LoginPage
from page.minepage import MinePage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def home_page(self):
        return HomePage(self.driver)

    @property
    def mine_page(self):
        return MinePage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)

