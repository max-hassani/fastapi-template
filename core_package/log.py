
__author__ = "Max Hassani <max.hassani.dev@outlook.com>"

import time
import os
import datetime
from core_package import core_config



class Logger:
    def __init__(self, output_path, file_name, log_level, write_mode="a"):
        self.map_log_priority = {
            "INFO": 1,
            "DEBUG": 2,
            "WARNING": 0,
            "ERROR": 0,
            "CRITICAL": 0
        }
        self.log_level = log_level
        self.output_path = output_path
        self.path_creation_if_needed()
        self.file_name = file_name
        self.write_mode = write_mode

    def DEBUG(self, message):
        self.write(message, "DEBUG")

    def INFO(self, message):
        self.write(message, "INFO")

    def WARNING(self, message):
        self.write(message, "WARNING")

    def ERROR(self, message):
        self.write(message, "ERROR")

    def write(self, message, log_mode="INFO"):
        if self._check_priority(log_mode):
            self.path_creation_if_needed()
            file_path = os.path.join(self.log_file_path, self.file_name)  
            with open(file_path, self.write_mode) as logFile:
                logFile.write(f"{time.strftime('%H:%M:%S',time.localtime())}"
                            f"--- {log_mode} --- {message}\n")

    def path_creation_if_needed(self):
        today = datetime.date.today()
        self.log_file_path = os.path.abspath(
            os.path.join(self.output_path, "logs")
        )
        if not os.path.exists(self.log_file_path):
            try:
                os.mkdir(self.log_file_path)
            except Exception as err_msg:
                print(f"log file path creation failed: {err_msg}")
                raise RuntimeError(f"log file path creation failed: {err_msg}")
        if not os.path.exists(
            os.path.join(self.log_file_path, today.strftime('%Y-%m-%d'))
        ):
            try:
                self.log_file_path = os.path.join(self.log_file_path, today.strftime('%Y-%m-%d'))
                os.mkdir(self.log_file_path)
            except Exception as err_msg:
                print(f"log file path creation failed: {err_msg}")
                raise RuntimeError(f"log file path creation failed: {err_msg}")
        else:
            self.log_file_path = os.path.join(self.log_file_path, today.strftime('%Y-%m-%d'))

    def _check_priority(self, log_mode):
        if self.map_log_priority[log_mode] > self.map_log_priority[self.log_level]:
            return False
        return True


class StreamToLogger:
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger: Logger, level):
        self.logger = logger
        self.level = level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.write(line.rstrip(), self.level)

    def flush(self):
        pass
