from .screen import ScreenSize
from .direction import Direction
from .unit import Unit
from .enemy import Enemy
import pygame


if __name__ == "__main__":
    pygame.init()
    screen_size = ScreenSize(width=800, height=600)
    screen = pygame.display.set_mode(screen_size)
    player = Unit(x=10, y=10, width=100, height=100, screen_size=screen_size)
    enemy = Enemy(x=400, y=400, width=100, height=100, screen_size=screen_size)
    has_quit = False
    speed = 20

    while not has_quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                has_quit = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                player.move_unit(speed, Direction.UP)
                enemy.move_unit(-speed, Direction.UP)
            if pressed[pygame.K_DOWN]:
                player.move_unit(speed, Direction.DOWN)
                enemy.move_unit(-speed, Direction.DOWN)
            if pressed[pygame.K_LEFT]:
                player.move_unit(speed, Direction.LEFT)
                enemy.move_unit(-speed, Direction.LEFT)
            if pressed[pygame.K_RIGHT]:
                player.move_unit(speed, Direction.RIGHT)
                enemy.move_unit(-speed, Direction.RIGHT)

            screen.fill((0, 0, 0))
            player.draw_sprite(screen)
            enemy.draw_sprite(screen)

        pygame.display.flip()
