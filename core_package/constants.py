from enum import Enum


#environment variables
APP_NAME = "CORE_PACKAGE"

# the key defining the environment; whether DEV, TEST, PROD
KEY_ENV = f"{APP_NAME}_ENVIRONMENT"

# the path to Log file
KEY_LOG_PATH = f"{APP_NAME}_LOG_PATH"
KEY_LOGFILE_NAME = f"{APP_NAME}_LOGFILE_NAME"

KEY_SECRET_KEY = f"{APP_NAME}_SECRET_KEY"

KEY_API_HOST = f"{APP_NAME}_HOST"
KEY_API_PORT = f"{APP_NAME}_PORT"
KEY_API_LOGLEVEL = f"{APP_NAME}_LOGLEVEL"
KEY_DB_URL = f"{APP_NAME}_DB_URL"
KEY_DB_USER = f"{APP_NAME}_DB_USER"
KEY_DB_PASS = f"{APP_NAME}_DB_PASS"
KEY_DB_PORT = f"{APP_NAME}_DB_PORT"
KEY_DB_TYPE = f"{APP_NAME}_DB_TYPE"
KEY_DB_NAME = f"{APP_NAME}_DB_NAME"
KEY_DB_AYNC_LIB = f"{APP_NAME}_DB_ASYNC_LIB"



class ValidActions(Enum):
    """
    the valid actions for the resources
    """
    read = "read"
    create = "create"
    delete = "delete"
    update = "update"

KEY_PLATFORM = f"{APP_NAME}_PLATFORM"