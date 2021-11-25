#!/usr/bin/env python


import logging
import os
import sys

from logging.handlers import TimedRotatingFileHandler
from pprint import pformat


os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
appname = "krypton"

fmt = """
%(asctime)s  %(name)s  %(levelname)s  %(funcName)s:%(lineno)d  %(message)s
"""

FORMATTER = logging.Formatter(fmt)
LOG_DIR = os.path.join(pwd, "log")
LOG_FILE = os.path.join(LOG_DIR, "krypton.log")
# LOGLEVEL = logging.getLevelName('DEBUG')

if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)


def get_file_name(metric_name):
    return "{d}/{p}-{f}.log".format(
        d=LOG_DIR,
        p=appname,
        f=metric_name,
    )


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler(metric_name):
    file_handler = TimedRotatingFileHandler(get_file_name(metric_name), when="H")
    file_handler.setFormatter(FORMATTER)
    return file_handler


def get_logger(logger_name, metric_name="default"):
    logger = logging.getLogger(logger_name)

    # better to have too much log than not enough
    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(metric_name))

    logger.propagate = False

    return custom_log_methods(logger)


def logpp(data, log_header=None):
    """format msg and make it pretty"""
    formatted = pformat(data, indent=4)
    if log_header is None:
        msg = "{0}\n".format(type(data))
    else:
        msg = "{0}\n".format(repr(log_header))
    try:
        result = msg + formatted
    except:
        result = "{0}\n{1}".format(msg, formatted)
    return result


def custom_log_methods(logger):
    logger.i = logger.info
    logger.e = logger.error
    logger.w = logger.warning
    logger.d = logger.debug
    logger.pp = logpp
    return logger


# from functools import wraps

# def lop(func):
#     @wraps
#     def wrapper():
