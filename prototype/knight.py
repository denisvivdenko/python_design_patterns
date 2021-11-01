from __future__ import annotations
from .unit import Unit
from copy import deepcopy

class Knight(Unit):
    def __init__(self, level: int) -> None:
        super().__init__(str(level))

        properties_file = "prototype/knight_properties.json"
        level_properties = self.read_properties_from_file(properties_file)['knight_levels']
        self.logger.write_debug_message(f"properties: {str(level_properties)}")
        self.logger.write_debug_message(f"level: {self.level}")

        self.power = level_properties[self.level]['power']
        self.agility = level_properties[self.level]['agility']

    def clone(self) -> Knight:
        return deepcopy(self)

    def __str__(self) -> str:
        return f"\nknight:\npower: {self.power}\nagility: {self.agility}\n"