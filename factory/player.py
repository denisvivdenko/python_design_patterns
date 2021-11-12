from .unit import Unit
import pygame

class Player(Unit):
    def draw_sprite(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))
    