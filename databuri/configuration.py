import configparser
import os
from pathlib import Path

USER_HOME = Path.home()
CACHE_DIR = '~/databuri'

CONFIGURATION_FILES = [
    '{}/databuri/config.ini'.format(USER_HOME),
    './.databuri/config.ini',
]

DATABURI_CONFIG_ENV = os.getenv('DATABURI_CONFIG')
if DATABURI_CONFIG_ENV:
    CONFIGURATION_FILES.append(DATABURI_CONFIG_ENV)

def read_config(additional_configs=[]):
    config = configparser.ConfigParser()
    config.read(CONFIGURATION_FILES + additional_configs)

    return config
