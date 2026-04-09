import pygame
import math


class Speedometer:
    def __init__(self, x, y, radius=120):
        self.x = x
        self.y = y
        self.radius = radius

        # Angle range (semi-circle)
        self.start_angle = math.pi * 0.75
        self.end_angle = math.pi * 2.25

    def draw(self, screen, speed):
        # Clamp speed
        speed = max(0, min(120, speed))

        # Draw base arc
        pygame.draw.arc(
            screen,
            (80, 80, 80),
            (
                self.x - self.radius,
                self.y - self.radius,
                self.radius * 2,
                self.radius * 2
            ),
            self.start_angle,
            self.end_angle,
            8
        )

        # Draw colored zones
        self.draw_zone(screen, 0, 40, (220, 70, 70))    # slow
        self.draw_zone(screen, 40, 80, (220, 150, 50))  # medium
        self.draw_zone(screen, 80, 120, (50, 200, 100)) # fast

        # Draw ticks
        for v in range(0, 121, 20):
            angle = self.map_speed_to_angle(v)
            self.draw_tick(screen, angle, v)

        # Draw needle
        angle = self.map_speed_to_angle(speed)
        self.draw_needle(screen, angle, speed)

    def map_speed_to_angle(self, speed):
        # Map 0–120 → angle range
        ratio = speed / 120
        return self.start_angle + ratio * (self.end_angle - self.start_angle)

    def draw_zone(self, screen, start, end, color):
        pygame.draw.arc(
            screen,
            color,
            (
                self.x - self.radius,
                self.y - self.radius,
                self.radius * 2,
                self.radius * 2
            ),
            self.map_speed_to_angle(start),
            self.map_speed_to_angle(end),
            10
        )

    def draw_tick(self, screen, angle, value):
        inner = self.radius - 15
        outer = self.radius - 5

        x1 = self.x + inner * math.cos(angle)
        y1 = self.y + inner * math.sin(angle)

        x2 = self.x + outer * math.cos(angle)
        y2 = self.y + outer * math.sin(angle)

        pygame.draw.line(screen, (200, 200, 200), (x1, y1), (x2, y2), 2)

        # Draw numbers
        font = pygame.font.SysFont("Arial", 12)
        text = font.render(str(value), True, (200, 200, 200))

        tx = self.x + (self.radius - 30) * math.cos(angle)
        ty = self.y + (self.radius - 30) * math.sin(angle)

        screen.blit(text, (tx - 10, ty - 10))

    def draw_needle(self, screen, angle, speed):
        length = self.radius - 20

        x = self.x + length * math.cos(angle)
        y = self.y + length * math.sin(angle)

        # Color based on speed
        if speed < 45:
            color = (220, 70, 70)
        elif speed < 80:
            color = (220, 150, 50)
        else:
            color = (50, 200, 100)

        pygame.draw.line(screen, color, (self.x, self.y), (x, y), 4)

        # Center circle
        pygame.draw.circle(screen, (200, 200, 200), (self.x, self.y), 6)