import typing
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from typing import Tuple, Optional


class BasePage:
    def __init__(self, setup):
        self.driver = setup
        self.wait = WebDriverWait(self.driver, 15)

    def click_action(self, locator: Tuple[str, str], locator_name=None) -> bool:
        """

        :param locator:
        :param locator_name:
        :return:
        """
        try:
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(ec.visibility_of_element_located(locator))
            element.click()
            if locator_name:
                actual_value = element.text
                if locator_name == actual_value:
                    return True
                else:
                    # self.logger.error(f"Click Element Mismatch, Expected: {locator_name}, Actual: {actual_value}")
                    return False
            return True
        except ElementClickInterceptedException as e:
            # self.logger.warning(f"Error: Element not clickable. Error: {e}, Locator: {locator}")
            return False
        except NoSuchElementException as e:
            return False
        except TimeoutException as e:
            # self.logger.error(f"Web element not available within the time: {e}")
            return False

    def set_string(self, locator: Tuple[str, str], user_input: [str], validation=False) -> Optional[bool]:
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(user_input)
            if validation:
                actual_value = element.get_attribute("value")
                if user_input == actual_value:
                    return True
                else:
                    # self.logger.error(f"Insert text Element Mismatch, Expected: {user_input}, Actual: {actual_value}")
                    return False
            return True
        except NoSuchElementException as e:
            # self.logger.error(f"Error: Unable to locate or click the element error: {e}, locator: {locator}")
            return False

