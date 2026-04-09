import pygame


class Car:
    def __init__(self, lane_x, y):
        self.x = lane_x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, (50, 200, 100),
                         (self.x, self.y, 40, 70), border_radius=8)

        pygame.draw.rect(screen, (30, 30, 30),
                         (self.x + 5, self.y + 10, 30, 20), border_radius=4)

        pygame.draw.circle(screen, (20, 20, 20), (self.x + 8, self.y + 65), 5)
        pygame.draw.circle(screen, (20, 20, 20), (self.x + 32, self.y + 65), 5)


class FrontCar:
    def __init__(self, lane_x):
        self.x = lane_x
        self.base_y = 100

    def get_position(self, distance):
        return self.base_y + (100 - distance) * 3

    def draw(self, screen, distance):
        y = self.get_position(distance)

        pygame.draw.rect(screen, (200, 50, 50),
                         (self.x, y, 40, 70), border_radius=8)

        pygame.draw.rect(screen, (30, 30, 30),
                         (self.x + 5, y + 10, 30, 20), border_radius=4)

        if distance < 20:
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 8, y + 65), 4)
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 32, y + 65), 4)