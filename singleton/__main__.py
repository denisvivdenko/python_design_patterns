from .logger import Logger


logger = Logger('./log_file')
logger.write_info_message("information")
