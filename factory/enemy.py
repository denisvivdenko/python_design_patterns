import pygame

from .game_unit import GameUnit

class Enemy(GameUnit):
    def draw_sprite(self, screen: pygame.Surface) -> None:
        radius = int((self.width + self.height)/ 4)
        pygame.draw.circle(screen, self.color, (self.x + radius, self.y + radius), radius)
