import os
import logging
from logging.handlers import TimedRotatingFileHandler


# Input Files

INPUT_FILE = 'input.json'
SCHEMA_CONF_FILE = 'schema-conf.json'


# Logging configuratons

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs/')
LOG_FILENAME = 'taxfixlog.log'
LOG_FORMAT = '%(asctime)s (%(name)s) %(levelname)s - %(message)s'
LOGGING_LEVEL = logging.INFO
WHEN = 'midnight'
BACKUP_COUNT = 3

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)


formatter = logging.Formatter(LOG_FORMAT)

logger = logging.getLogger(__name__)

handler = TimedRotatingFileHandler(
    LOG_DIR + LOG_FILENAME, when=WHEN, backupCount=BACKUP_COUNT
)
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(LOGGING_LEVEL)
