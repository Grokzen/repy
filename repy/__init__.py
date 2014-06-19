# -*- coding: utf-8 -*-

""" repy """

__author_email__ = "Grokzen@gmail.com"
__author_name__ = "Johan Grok Andersson"
__author__ = '{} <{}>'.format(__author_name__, __author_email__)
__pkgname__ = "repy"
__version_info__ = (14, 6)
__version__ = "{}.{}".format(__version_info__[0], __version_info__[1] if __version_info__[1] >= 10 else "0{}".format(__version_info__[1]))

# Set to True to have revision from Version Control System in version string
__devel__ = True

# import sys
import os

# init python std logging
import logging
import logging.config


def init_logging():
    """
    Bootstraps the logging configuration.

    This method do not work with python 3.1
    """
    msg = "%(levelname)s - %(name)s:%(lineno)s - %(message)s" if "DEBUG" in os.environ else "%(levelname)s - %(message)s"

    # This logging config can only be used with python >= 3.2.0
    logging_conf = {
        "version": 1,
        "root": {
            "level": "DEBUG",
            "handlers": ["console"]
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            }
        },
        "formatters": {
            "simple": {
                "format": " {}".format(msg)
            }
        }
    }

    logging.config.dictConfig(logging_conf)
