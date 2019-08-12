import configparser
from pathlib import Path

USER_HOME = Path.home()
CACHE_DIR = '~/databuri'

CONFIGURATION_FILES = [
    f'{USER_HOME}/databuri/config.ini',
    './.databuri/config.ini'
]


def read_config(additional_configs=[]):
    config = configparser.ConfigParser()
    config.read(CONFIGURATION_FILES + additional_configs)

    return config
