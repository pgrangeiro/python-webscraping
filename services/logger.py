import logging


class Logger:

    LOG_FILE = 'error.log'

    @classmethod
    def log(cls, message):
        logging.basicConfig(filename=cls.LOG_FILE)
        logging.error(message)
