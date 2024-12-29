from src.pages.basepage import BasePage
from src.locators import locators
from typing import Tuple, Optional, Any
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    def __init__(self, setup):
        super().__init__(setup)

    def click_on_login_btn_to_redirect(self):
        return self.click_action(locators.HomePage.login_option_btn)

    def enter_email(self, username: [str]):
        set_username = self.set_string(locators.LoginPage.email_field, username)
        assert set_username is True

    def enter_password(self, password: [str]):
        set_password = self.set_string(locators.LoginPage.password_field, password)
        assert set_password is True

    def click_on_login_btn(self):
        return self.click_action(locators.LoginPage.login_submit_btn)

    def is_login_success(self):
        workspace_object = self.wait.until(ec.visibility_of_element_located(locators.LoggedInHomePage.create_workspace))
        return workspace_object.is_displayed()

    def is_login_failed(self):
        workspace_object = self.wait.until(ec.visibility_of_element_located(locators.LoggedInHomePage.invalid_username_password))
        return workspace_object.is_displayed()
