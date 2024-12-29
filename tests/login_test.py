import pytest
from src.pages.login_page import LoginPage
from src.utils.config_reader import env_reader
from src.utils.config_reader import yaml_reader


class TestLogin:
    @pytest.fixture(autouse=True)
    def login_setup(self, setup):
        #
        self.driver = setup
        self.login = LoginPage(setup)
        read = yaml_reader()
        self.username = read['staging']['login']['email']
        self.password = read['staging']['login']['password']

    @pytest.mark.parametrize("username,password,valid_user", [("anacooonda@outlook.co", "Testing1234", True),
                                                              ("giri23j@gmail.com", "test1234", False)])
    def test_login(self, username, password, valid_user):
        self.driver.get(env_reader("staging"))
        # self.login.click_on_login_btn_to_redirect()
        self.login.enter_email(username)
        self.login.enter_password(password)
        self.login.click_on_login_btn()
        if valid_user:
            assert self.login.is_login_success() is True
        elif not valid_user:
            assert self.login.is_login_failed() is True
