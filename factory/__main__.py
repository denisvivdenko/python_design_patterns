import pygame

from .screen import Point, ScreenSize
from .direction import Direction
from .unit_creator import UnitCreator

if __name__ == "__main__":
    pygame.init()
    screen_size = ScreenSize(width=800, height=600)
    screen = pygame.display.set_mode(screen_size)

    unit_creator = UnitCreator(ScreenSize(width=800, height=600))
    unit = unit_creator.CreateUnit("Player", respawn_point=Point(10, 10))

    has_quit = False
    while not has_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                has_quit = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_1]:
                unit = unit_creator.CreateUnit("Player", respawn_point=unit.current_point)
            elif pressed[pygame.K_2]:
                unit = unit_creator.CreateUnit("Enemy", respawn_point=unit.current_point)

            if pressed[pygame.K_UP]:
                unit.move_unit(Direction.UP)
            if pressed[pygame.K_DOWN]:
                unit.move_unit(Direction.DOWN)
            if pressed[pygame.K_LEFT]:
                unit.move_unit(Direction.LEFT)
            if pressed[pygame.K_RIGHT]:
                unit.move_unit(Direction.RIGHT)

            screen.fill((0, 0, 0))
            unit.draw_sprite(screen)

        pygame.display.flip()
