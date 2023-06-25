import logging
import logging.config
import os
from datetime import datetime
from logging import Logger
from logging.handlers import TimedRotatingFileHandler

from notify.config import configs
from notify.constants import ROOT_DIR


def get_logger(logger_name: str = "root") -> Logger:
    ## Setup loggers
    logging.config.fileConfig("notify/logging.ini", disable_existing_loggers=False)

    ## get root logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)-7s] [%(module)s:%(lineno)-4s] - [Func: %(funcName)-18s] - Exception: %(exc_info)s - %(message)s"
    )

    # Create year and month folders
    current_year = datetime.now().strftime("%Y")
    current_month = datetime.now().strftime("%B")
    log_folder = ROOT_DIR / "logs" / current_year / current_month
    os.makedirs(log_folder, exist_ok=True)

    fileHandler = TimedRotatingFileHandler(
        log_folder / "notify.log", when="midnight", interval=1
    )
    fileHandler.suffix = "%Y-%m-%d"
    fileHandler.setLevel(logging.DEBUG if configs.is_debug else logging.WARNING)
    fileHandler.setFormatter(log_format)
    logger.addHandler(fileHandler)

    return logger
