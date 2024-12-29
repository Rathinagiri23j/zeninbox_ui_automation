from selenium.webdriver.common.by import By


class HomePage:
    login_option_btn = (By.XPATH, "//button[normalize-space()='Log in']")


class LoginPage:
    email_field = (By.XPATH, "//input[@id='email']")
    password_field = (By.XPATH, "//input[@id='password']")
    login_submit_btn = (By.XPATH, "//button[normalize-space()='Login']")


class LoggedInHomePage:
    create_workspace = (By.XPATH, "//button[contains(.,'Create Workspace')]")
    invalid_username_password = (By.XPATH, "(//p[normalize-space()='Invalid email or password'])")
