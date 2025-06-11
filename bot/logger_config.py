import sys
import logging


def setup_logger(name):
    logging.basicConfig(
            level=logging.INFO, 
            stream=sys.stdout, 
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    logger = logging.getLogger(name)
    return  logger
