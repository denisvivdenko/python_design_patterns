from .screen import Point, ScreenSize
from .enemy import Enemy
from .player import Player
from .game_unit import GameUnit

class UnitCreator:
    def CreateUnit(self, type: str, respawn_point: Point, screen_size: ScreenSize) -> GameUnit:
        if type == "Player":
            return Player(*respawn_point, width=100, height=100, screen_size=screen_size)
        elif type == "Enemy":
            return Enemy(*respawn_point, width=100, height=100, screen_size=screen_size)
        raise Exception("Unknown game unit type.")