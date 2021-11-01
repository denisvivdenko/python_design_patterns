from __future__ import annotations
from .unit import Unit
from copy import deepcopy

class Wizard(Unit):
    def __init__(self, level: int) -> None:
        super().__init__(str(level))

        properties_file = "prototype/wizard_properties.json"
        level_properties = self.read_properties_from_file(properties_file)['wizard_levels']

        self.power = level_properties[self.level]['power']
        self.max_distance = level_properties[self.level]['power']

    def clone(self) -> Wizard:
        return deepcopy(self)

    def __str__(self) -> str:
        return f"\nwizard:\npower: {self.power}\nmax distance: {self.max_distance}"