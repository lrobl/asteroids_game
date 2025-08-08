from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        # Watch for window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 1. Check for player inputs
        # 2. Update the game world
        # 3. Draw the game to the screen
        screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
