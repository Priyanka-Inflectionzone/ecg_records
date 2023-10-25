import logging, coloredlogs
# from logging.handlers import RotatingFileHandler
from logging.handlers import SysLogHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

coloredlogs.install(level='INFO', fmt='%(asctime)s %(levelname)s %(message)s', milliseconds=True)