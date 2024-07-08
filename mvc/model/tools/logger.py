import logging
import sys


class Logger:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)5s - %(message)s",
        encoding="UTF-8",
        handlers=[
            # logging.FileHandler("d:/logging.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    @classmethod
    def info(cls, message):
        logging.info(message)

    @classmethod
    def error(cls, message):
        logging.error(message)

    @classmethod
    def debug(cls, message):
        logging.error(message)
