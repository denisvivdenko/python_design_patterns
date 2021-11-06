from .unit import Unit
import pygame

class Enemy(Unit):
    def draw_sprite(self, screen: pygame.Surface) -> None:
        radius = int((self.width + self.height)/ 4)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
