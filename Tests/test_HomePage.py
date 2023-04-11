from Pages.HomePage import HomePage
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_BasePage import BaseTest


class TestHome(BaseTest):
    def test_home_page_title(self):
        """ We need to log in first """
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        """ User is now logged in """
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_settings_icon_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.does_settings_icon_exist()
        assert flag





