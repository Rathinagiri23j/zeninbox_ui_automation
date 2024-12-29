import pytest
from src.utils.driver_factory import get_driver
from src.utils.config_reader import env_reader
from src.utils.config_reader import yaml_reader


@pytest.fixture(autouse=True, scope="function")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()
