from singleton.logger import Logger

def test_singleton():
    logger_1 = Logger("./singleton/log_file")
    logger_2 = Logger("./singleton/log_file")
    logger_1.write_info_message(f"{logger_1}\n{logger_2}")

    assert id(logger_1) == id(logger_2)
    assert logger_1 == logger_2

def test_logger():
    logger = Logger("./log_file")
    logger.write_debug_message("debug this part")
    logger.write_info_message("information")
    logger.write_debug_message(f"{logger}")