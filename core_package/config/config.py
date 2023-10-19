"""
# Copyright (c) Umlaut Communication GmbH

Here the Config class which takes care of configuring the API, is defined
"""

import os
from core_package import constants


__author__ = "Max Hassani <max.hassani.dev@outlook.com>"


class Config:
    """
    the configuration class.
    it returns the required setting values from the environment variables.
    """

    @property
    def env(self):
        return os.getenv(constants.KEY_ENV, "TEST")

    @property
    def db_url(self):
        if self.platform == "EBS":
            if "RDS_HOSTNAME" in os.environ:
                return os.getenv("RDS_HOSTNAME")
        return os.getenv(constants.KEY_DB_URL)

    @property
    def db_user(self):
        if self.platform == "EBS":
            if "RDS_USER_NAME" in os.environ:
                return os.getenv("RDS_USER_NAME")
        return os.getenv(constants.KEY_DB_USER)

    @property
    def db_pass(self):
        if self.platform == "EBS":
            if "RDS_PASS" in os.environ:
                return os.getenv("RDS_PASS")
        return os.getenv(constants.KEY_DB_PASS)

    @property
    def db_port(self):
        if self.platform == "EBS":
            if "RDS_DB_PORT" in os.environ:
                return os.getenv("RDS_DB_PORT")
        return os.getenv(constants.KEY_DB_PORT)

    @property
    def db_type(self):
        return os.getenv(constants.KEY_DB_TYPE)

    @property
    def db_name(self):
        if self.platform == "EBS":
            if "RDS_DB_NAME" in os.environ:
                return os.getenv("RDS_DB_NAME")
        return os.getenv(constants.KEY_DB_NAME)

    @property
    def async_lib(self):
        return os.getenv(constants.KEY_DB_AYNC_LIB)

    @property
    def connection_string(self):
        if self.db_type == "sqlite":
            return f"{self.db_type}+{self.async_lib}:///{self.db_url}"
        else:
            return f"{self.db_type}+{self.async_lib}://" + \
                f"{self.db_user}:{self.db_pass}" + \
                f"@{self.db_url}:{self.db_port}/{self.db_name}"

    @property
    def secret_key(self):
        return os.getenv(constants.KEY_SECRET_KEY,
        "a_very_very_secret_key")

    @property
    def logging_path(self):
        return os.getenv(constants.KEY_LOG_PATH, os.path.dirname(__file__))

    @property
    def logfile_name(self):
        return os.getenv(constants.KEY_LOGFILE_NAME, "app.log")

    @property
    def api_host(self):
        return os.getenv(constants.KEY_API_HOST, "127.0.0.1")

    @property
    def api_port(self):
        return int(os.getenv(constants.KEY_API_PORT, 7000))

    @property
    def log_level(self):
        return os.getenv(constants.KEY_API_LOGLEVEL, "DEBUG")
    
    @property
    def platform(self):
        return os.getenv(constants.KEY_PLATFORM, "local")
    
    
