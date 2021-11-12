import pygame

from .game_unit import GameUnit

class Enemy(GameUnit):
    def __init__(self, **kwargs) -> None:
        kwargs["speed"] = 20
        super().__init__(**kwargs)

    def draw_sprite(self, screen: pygame.Surface) -> None:
        radius = int((self.width + self.height)/ 4)
        pygame.draw.circle(screen, self.color, (self.x + radius, self.y + radius), radius)
