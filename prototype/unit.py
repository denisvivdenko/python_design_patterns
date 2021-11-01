from singleton.logger import Logger

from abc import ABC, abstractmethod
import json

class Unit(ABC):
    def __init__(self, level: str) -> None:
        self.logger = Logger()
        self.level = str(level)

    def read_properties_from_file(self, file_name: str):
        with open(file_name, 'r') as properties:
            return json.load(properties)

    @abstractmethod
    def clone(self):
        pass