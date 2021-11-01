from .baracks import Baracks
from singleton.logger import Logger 

if __name__ == '__main__':
    logger = Logger("prototype/log_file")
    baracks = Baracks()
    knight = baracks.generate_unit("knight", 1)
    wizard = baracks.generate_unit("wizard", 2)

    logger.write_info_message(str(knight))
    logger.write_info_message(str(wizard))