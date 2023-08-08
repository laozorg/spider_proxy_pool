import sys
import logging

from settings.settings import LOG_FMT,LOG_DATEFMT,LOG_FILENAME,LOG_LEVEL


class Logger(object):

    def __init__(self):
        self._logger = logging.getLogger()
        self.formatter = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATEFMT)
        self._logger.addHandler(self._get_file_handler(LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(LOG_LEVEL)

    def _get_file_handler(self, filename):
        file_handler = logging.FileHandler(filename=filename, encoding='UTF-8')
        file_handler.setFormatter(self.formatter)
        return file_handler

    def _get_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def log(self):
        return self._logger

logger = Logger().log
