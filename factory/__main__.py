from typing import Tuple
from collections import namedtuple
import pygame

ScreenSize = namedtuple("ScreenSize", "width height")

class Unit:
    def __init__(self, x: int, y: int, width: int, height: int, screen_size: ScreenSize) -> None:
        self.screen_size = screen_size
        self.width = width
        self.height = height
        self.color = (255, 0, 30)
        self._x = x
        self._y = y

    def draw_sprite(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        if self.screen_size.width > (value + self.width) and value >= 0:
            self._x = value 

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        if self.screen_size.height > (value + self.height) and value >= 0:
            self._y = value

pygame.init()
screen_size = ScreenSize(width=800, height=600)
screen = pygame.display.set_mode(screen_size)
unit = Unit(x=10, y=10, width=100, height=100, screen_size=screen_size)
has_quit = False
speed = 20

while not has_quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            has_quit = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            unit.y -= speed
        if pressed[pygame.K_DOWN]:
            unit.y += speed
        if pressed[pygame.K_LEFT]:
            unit.x -= speed
        if pressed[pygame.K_RIGHT]:
            unit.x += speed

        screen.fill((0, 0, 0))
        unit.draw_sprite(screen)

    pygame.display.flip()
