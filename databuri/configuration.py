import configparser
from pathlib import Path

USER_HOME = Path.home()
CACHE_DIR = '~/databuri'

CONFIGURATION_FILES = [
    '{}/databuri/config.ini'.format(USER_HOME),
    './.databuri/config.ini'
]


def read_config(additional_configs=[]):
    config = configparser.ConfigParser()
    config.read(CONFIGURATION_FILES + additional_configs)

    return config
