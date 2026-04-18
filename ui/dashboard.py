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

    def draw_fuel_bar(self, screen, fuel):
        x = self.x
        y = self.y - 40

        width = self.width
        height = 10

        # Background
        pygame.draw.rect(screen, (60, 60, 60), (x, y, width, height))

        # Fuel level
        fill = (fuel / 100) * width

        color = (50, 200, 100) if fuel > 40 else (255, 200, 50) if fuel > 15 else (255, 80, 80)

        pygame.draw.rect(screen, color, (x, y, fill, height))

        # Label
        font = pygame.font.SysFont("Arial", 12)
        text = font.render(f"Fuel: {int(fuel)}%", True, (255, 255, 255))
        screen.blit(text, (x, y - 18))


    def draw_fuel_graph(self, screen, fuel_history):
        if len(fuel_history) < 2:
            return

        graph_x = self.x
        graph_y = self.y - 100
        graph_w = self.width
        graph_h = 50

        # Border
        pygame.draw.rect(screen, (80, 80, 80), (graph_x, graph_y, graph_w, graph_h), 1)

        # Draw line
        points = []
        for i, value in enumerate(fuel_history):
            px = graph_x + (i / len(fuel_history)) * graph_w
            py = graph_y + graph_h - (value / 100) * graph_h
            points.append((px, py))

        if len(points) > 1:
            pygame.draw.lines(screen, (0, 200, 255), False, points, 2)

    def draw_speed_graph_small(self, screen, x, y, width):
        if len(self.speed_history) < 2:
            return

        height = 60

        pygame.draw.rect(screen, (80, 80, 80), (x, y, width, height), 1)

        points = []
        for i, value in enumerate(self.speed_history):
            px = x + (i / len(self.speed_history)) * width
            py = y + height - (value / 120) * height
            points.append((px, py))

        if len(points) > 1:
            pygame.draw.lines(screen, (0, 200, 255), False, points, 2)


    def draw_fuel_graph_small(self, screen, x, y, width, history):
        if len(history) < 2:
            return

        height = 60

        pygame.draw.rect(screen, (80, 80, 80), (x, y, width, height), 1)

        points = []
        for i, value in enumerate(history):
            px = x + (i / len(history)) * width
            py = y + height - (value / 100) * height
            points.append((px, py))

        if len(points) > 1:
            pygame.draw.lines(screen, (255, 200, 0), False, points, 2)