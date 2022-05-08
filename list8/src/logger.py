from enum import Enum
from datetime import datetime

DEFAULT_LOG_FILE_NAME = "default.log"


class Severity(Enum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4


class Logger:
    def __init__(self, log_file_name=DEFAULT_LOG_FILE_NAME):
        try:
            self.__file_name = log_file_name
            self.__file_handle = open(log_file_name, "w+", encoding="utf-8")
            self.log_info(
                f'Successfully initialized logger for file: "{self.__file_name}"'
            )
        except:
            print(f"Failed to create log file handle")

    def __del__(self):
        self.__file_handle.close()

    def log_info(self, msg: str):
        self.__log_msg(msg, Severity.INFO)

    def log_debug(self, msg: str):
        self.__log_msg(msg, Severity.DEBUG)

    def log_warn(self, msg: str):
        self.__log_msg(msg, Severity.WARN)

    def log_error(self, msg: str):
        self.__log_msg(msg, Severity.ERROR)

    def log_critical(self, msg: str):
        self.__log_msg(msg, Severity.CRITICAL)

    def __log_msg(self, msg: str, severity: Severity):
        try:
            self.__file_handle.write(self.__get_formatted_msg(msg, severity.name))
        except IOError as e:
            print(f"Failed to log msg to file: {self.__log_file_name}, error: {e}")

    def __get_formatted_msg(self, msg: str, prefix: str):
        time = datetime.now().strftime("%H:%M:%S")
        return f"[{time}][{prefix}] {msg}\n"
