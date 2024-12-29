from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_driver(browser_name: [str] = "chrome", headless: [bool] = False) -> object:
    """
    :param browser_name: different browser option
    :param headless: running on headless mode or not
    :return: driver object, will be used for test cases
    """
    browser_name = browser_name.lower()
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options, service=ChromeService())

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options, service=FirefoxService())

    elif browser_name == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options, service=EdgeService())

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    return driver
