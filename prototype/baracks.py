from typing import Dict
from prototype.knight import Knight
from prototype.wizard import Wizard
from .unit import Unit

class Baracks:
    def __init__(self) -> None:
        self.available_units: Dict[Dict[str, Unit]] = {
            "knight": {
                "1": Knight(1),
                "2": Knight(2)
            },
            "wizard": {
                "1": Wizard(1),
                "2": Wizard(2)
            }
        }

    def generate_unit(self, unit_type: str, unit_level: int) -> Unit:
        return self.available_units[unit_type][str(unit_level)].clone()