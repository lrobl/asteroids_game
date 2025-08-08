import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self):
        # Defines a triangle by its verticies, circumscribed by the player circle
        # define unit vectors rotated in the direction of the points relative
        # to the center of the circle. Forward straight ahead, left and right 90
        # degress +-
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color="white",
            points=self.triangle(),
            width=2,
        )

    def move(self, dt):
        distance = pygame.Vector2(0, 1).rotate(self.rotation) * dt * PLAYER_SPEED
        self.position += distance

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        # update cooldowns
        self.shoot_cooldown -= dt

        # Manage player input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            # rotate right
            self.rotate(dt)
        if keys[pygame.K_a]:
            # rotate left
            self.rotate(-dt)
        if keys[pygame.K_w]:
            # move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # move backwards
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            # Shoot
            self.shoot()
