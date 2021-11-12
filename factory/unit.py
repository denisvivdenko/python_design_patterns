from abc import ABC, abstractmethod
import pygame

from .screen import ScreenSize
from .direction import Direction

class Unit(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, screen_size: ScreenSize) -> None:
        self.screen_size = screen_size
        self.width = width
        self.height = height
        self.color = (255, 0, 30)
        self._x = x
        self._y = y

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
            
    @abstractmethod
    def draw_sprite(self, screen: pygame.Surface) -> None:
        pass

    def move_unit(self, speed: int, direction: Direction) -> None:
        if direction == Direction.UP:
            self.y -= speed
        elif direction == Direction.DOWN:
            self.y += speed
        elif direction == Direction.LEFT:
            self.x -= speed
        elif direction == Direction.RIGHT:
            self.x += speed
