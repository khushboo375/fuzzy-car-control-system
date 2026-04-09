import pygame
import random


class Rain:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.drops = []

        for _ in range(100):
            self.drops.append([
                random.randint(0, width),
                random.randint(0, height)
            ])

    def update(self, speed):
        for drop in self.drops:
            drop[1] += 5 + speed * 0.1  # rain falls faster with speed

            if drop[1] > self.height:
                drop[0] = random.randint(0, self.width)
                drop[1] = 0

    def draw(self, screen):
        for drop in self.drops:
            pygame.draw.line(
                screen,
                (100, 100, 255),
                (drop[0], drop[1]),
                (drop[0], drop[1] + 8),
                1
            )