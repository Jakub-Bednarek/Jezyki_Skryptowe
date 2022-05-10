from enum import Enum
from datetime import datetime
from unittest.mock import DEFAULT

DEFAULT_LOG_FILE_NAME = "default.log"


class Severity(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4


class Logger:
    def init_logger(self, print_to_console=False, log_file_name=DEFAULT_LOG_FILE_NAME):
        self.__print_to_console = print_to_console
        self.__file_name = log_file_name
        self.__file_handle = open(log_file_name, "w+", encoding="utf-8")
        log_info(f'Successfully initialized logger for file: "{self.__file_name}"')

    def cleanup_logger(self):
        self.__file_handle.close()

    def set_logger_file(self, file_name):
        try:
            new_file_handle = open(file_name, "w+", encoding="utf-8")
            self.__file_handle.close()
            self.__file_handle = new_file_handle
            self.__file_name = file_name
            log_info(f"Succesfully set file for logger: {file_name}")
        except:
            self.file_handle = open(self.__file_name, "w+", encoding="utf-8")
            log_error(f"Failed to set file for logger: {file_name}")

    def log_msg(self, msg: str, severity: Severity):
        try:
            formatted_msg = self.__get_formatted_msg(msg, severity.name)
            self.__file_handle.write(formatted_msg)
            if self.__print_to_console:
                print(formatted_msg)
        except IOError as e:
            print(f"Failed to log msg to file: {self.__log_file_name}, error: {e}")

    def __get_formatted_msg(self, msg: str, prefix: str):
        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}][{prefix}] {msg}\n"


msg_logger = Logger()


def log_info(msg: str):
    msg_logger.log_msg(msg, Severity.INFO)


def log_debug(msg: str):
    msg_logger.log_msg(msg, Severity.DEBUG)


def log_warn(msg: str):
    msg_logger.log_msg(msg, Severity.WARN)


def log_error(msg: str):
    msg_logger.log_msg(msg, Severity.ERROR)


def log_critical(msg: str):
    msg_logger.log_msg(msg, Severity.CRITICAL)
