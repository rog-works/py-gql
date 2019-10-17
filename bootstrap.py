import os
import sys
from log import logger

sys.path.append(f'{os.getcwd()}/vendor')


def started():
    logger.debug('succeeded bootstraping!')
