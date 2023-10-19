from core_package import log
from core_package.config.config import Config

core_config = Config()
logger = log.Logger(
    output_path=core_config.logging_path,
    file_name=core_config.logfile_name,
    write_mode="a")
