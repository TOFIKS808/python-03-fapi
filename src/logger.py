""""
    Logging module
"""
import logging


def logger():
    """ Logging module """
    logging.basicConfig(filename='./var/application.log', level=logging.DEBUG)
    return logging
