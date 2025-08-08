import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_collision(self, other):
        center_distance = self.position.distance_to(other.position)
        radii_distance = self.radius + other.radius
        return radii_distance >= center_distance

    def screen_wrap(self):
        # wrap the sprite around when they go off screen
        # without using radius in the calc, the animation looks odds - sprites
        # look like they are disapearing. Using radius allows the sprite to get
        # off the screen fully before wrapping around
        self.position.x = self.position.x % (SCREEN_WIDTH + self.radius)
        self.position.y = self.position.y % (SCREEN_HEIGHT + self.radius)
