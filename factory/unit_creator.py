from .screen import Point, ScreenSize
from .enemy import Enemy
from .player import Player
from .game_unit import GameUnit

class UnitCreator:
    def __init__(self, screen_size: ScreenSize) -> None:
        self.screen_size = screen_size

    def CreateUnit(self, type: str, respawn_point: Point) -> GameUnit:
        if type == "Player":
            return Player(x=respawn_point.x, y=respawn_point.y, width=100, height=100, screen_size=self.screen_size)
        elif type == "Enemy":
            return Enemy(x=respawn_point.x, y=respawn_point.y, width=100, height=100, screen_size=self.screen_size)

        raise Exception("Unknown game unit type.")