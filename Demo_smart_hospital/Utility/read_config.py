import configparser
from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()

    config_file_path = os.path.join(os.path.dirname(__file__), '..', 'Configurations', 'config.ini')
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f"The configuration file was not found: {config_file_path}")

    config.read(config_file_path)
    return config.get(category, key)

try:
    browser = get_config('basic info', 'browser')
    print(f"Browser: {browser}")
except (configparser.NoSectionError, configparser.NoOptionError, FileNotFoundError) as e:
    print(e)
