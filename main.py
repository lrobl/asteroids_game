import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame

from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.init()

    # Build the screen with display settings
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Manage FPS
    clock = pygame.time.Clock()
    dt = 0

    # Create groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # Set sprite groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables

    # Instantiate sprites
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Watch for window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 1. Check for player inputs
        updatables.update(dt)
        # 2. Update the game world
        for asteroid in asteroids:
            if player.is_collision(asteroid):
                print("Game over!")
                sys.exit(1)
        # 3. Draw the game to the screen
        screen.fill(pygame.Color(0, 0, 0))

        # (Re)-Draw the player
        for drawable in drawables:
            drawable.draw(screen=screen)

        # Refresh the game screen
        pygame.display.flip()

        # Manage the clock (pauses the loop until 1/60th of second has passed)
        # .tick returns the amount of time that's passed since the last tick
        # (delta time). convert it to seconds from milliseconds
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
