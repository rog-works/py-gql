import os
import sys
import logging

sys.path.append(f'{os.getcwd()}/vendor')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def started():
    logger.debug('succeeded bootstraping!')
