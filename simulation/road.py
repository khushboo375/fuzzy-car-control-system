import pygame


class Road:
    def __init__(self, x, width, height):
        self.x = x
        self.width = width
        self.height = height
        self.offset = 0

        self.lanes = 3
        self.lane_width = width // self.lanes

    def update(self, speed):
        self.offset += speed * 0.5
        if self.offset > 40:
            self.offset = 0

    def draw(self, screen):
        # Road background
        pygame.draw.rect(screen, (25, 25, 25),
                         (self.x, 0, self.width, self.height))

        # Lane separators (vertical)
        for i in range(1, self.lanes):
            lane_x = self.x + i * self.lane_width

            pygame.draw.line(
                screen,
                (100, 100, 100),
                (lane_x, 0),
                (lane_x, self.height),
                2
            )

        # Center dashed lines (movement illusion)
        for lane in range(self.lanes):
            center_x = self.x + lane * self.lane_width + self.lane_width // 2

            for y in range(-40, self.height, 40):
                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    (center_x - 3, y + int(self.offset), 6, 20)
                )