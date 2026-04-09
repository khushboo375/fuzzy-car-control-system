import pygame


class Dashboard:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width

        self.speed_history = []
        self.max_points = 100

    def update(self, speed):
        self.speed_history.append(speed)

        if len(self.speed_history) > self.max_points:
            self.speed_history.pop(0)

    def draw_speed_graph(self, screen):
        if len(self.speed_history) < 2:
            return

        max_speed = 120
        graph_height = 80

        points = []

        for i, speed in enumerate(self.speed_history):
            px = self.x + i * (self.width / self.max_points)
            py = self.y + graph_height - (speed / max_speed) * graph_height
            points.append((px, py))

        pygame.draw.rect(screen, (50, 50, 50),
                         (self.x, self.y, self.width, graph_height), 2)

        pygame.draw.lines(screen, (50, 200, 255), False, points, 2)

    def draw_distance_bar(self, screen, distance):
        bar_width = self.width
        bar_height = 15

        # Background
        pygame.draw.rect(screen, (60, 60, 60),
                         (self.x, self.y + 100, bar_width, bar_height))

        # Fill
        fill_width = int((distance / 100) * bar_width)

        # Color based on safety
        if distance < 20:
            color = (255, 50, 50)
        elif distance < 50:
            color = (255, 150, 50)
        else:
            color = (50, 200, 100)

        pygame.draw.rect(screen, color,
                         (self.x, self.y + 100, fill_width, bar_height))

        # Label
        font = pygame.font.SysFont("Arial", 12)
        text = font.render(f"Distance: {int(distance)}", True, (200, 200, 200))
        screen.blit(text, (self.x, self.y + 120))