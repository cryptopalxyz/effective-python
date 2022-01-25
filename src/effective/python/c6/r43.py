# -*- coding: utf-8 -*-
import logging
from contextlib import contextmanager


def my_function():
    logging.debug('debug')
    logging.error('error log')
    logging.debug('more debug')

my_function()


@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger  #logger is being returned ...
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG) as logger:
    print('inside')
    logger.debug('haha')
    my_function()

print('after')
my_function()