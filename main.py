import os
import argparse
from configs.get_logger import init_logger
from test_script import test_logger
from module_a.test_script_2 import test_logger_2

logger = init_logger(os.path.splitext(os.path.basename(__file__))[0])


def main():
    print("Hello World!")
    logger.info(f"Hello Information from {__file__}!")
    logger.error(f"Hello Error from {__file__}!")
    logger.warning(f"Hello Warning from {__file__}!")
    logger.debug(f"Hello Debug from {__file__}!")

    test_logger()
    test_logger_2()


if __name__ == "__main__":
    main()
