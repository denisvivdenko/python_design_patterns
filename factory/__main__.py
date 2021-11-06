from typing import Tuple
from collections import namedtuple
from enum import Enum
import pygame

ScreenSize = namedtuple("ScreenSize", "width height")

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


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
    
    def move_unit(self, speed: int, direction: Direction, screen: pygame.Surface) -> None:
        if direction == Direction.UP:
            self.y -= speed
        elif direction == Direction.DOWN:
            self.y += speed
        elif direction == Direction.LEFT:
            self.x -= speed
        elif direction == Direction.RIGHT:
            self.x += speed

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
            unit.move_unit(speed, Direction.UP, screen)
        if pressed[pygame.K_DOWN]:
            unit.move_unit(speed, Direction.DOWN, screen)
        if pressed[pygame.K_LEFT]:
            unit.move_unit(speed, Direction.LEFT, screen)
        if pressed[pygame.K_RIGHT]:
            unit.move_unit(speed, Direction.RIGHT, screen)

        screen.fill((0, 0, 0))
        unit.draw_sprite(screen)

    pygame.display.flip()
