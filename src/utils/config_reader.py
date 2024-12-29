import yaml
from dotenv import load_dotenv
import os

# to load the .env file
load_dotenv()


def yaml_reader(file_path: [str] = "D:\zeninboxai_web_automation\config\config.yaml"):
    with open(file_path, "r") as yaml_file:
        return yaml.safe_load(yaml_file)


def env_reader(env_key: [str]) -> str:
    """
    :param env_key: key from .env
    :return: value of str:
    """
    return os.getenv(env_key)
