import logging
import os

# @todo #1 read config for loggin and level
ENV_LOG_LEVEL = os.getenv("DATABURI_LOG_LEVEL")
DATABURI_LOG_LEVEL = getattr(logging, ENV_LOG_LEVEL if ENV_LOG_LEVEL else 'INFO')

logging.basicConfig(
    format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=DATABURI_LOG_LEVEL
)

def getLogger(name):
    return logging.getLogger(name)