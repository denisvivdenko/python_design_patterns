import pygame

from .game_unit import GameUnit

class Player(GameUnit):
    def draw_sprite(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))
    