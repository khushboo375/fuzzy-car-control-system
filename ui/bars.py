import pygame


def draw_bar(screen, x, y, width, height, value, color, label):
    # Background bar
    pygame.draw.rect(screen, (60, 60, 60), (x, y, width, height))

    # Fill bar
    fill_width = int(width * value)
    pygame.draw.rect(screen, color, (x, y, fill_width, height))

    # Label
    font = pygame.font.SysFont("Arial", 12)
    text = font.render(f"{label}: {int(value*100)}%", True, (200, 200, 200))
    screen.blit(text, (x, y - 15))


def draw_membership_panel(screen, x, start_y, data, title):
    font = pygame.font.SysFont("Arial", 14)
    screen.blit(font.render(title, True, (220, 220, 220)), (x, start_y))

    y = start_y + 25
    for key, value in data.items():
        if key == "close" or key == "wet":
            color = (220, 70, 70)
        elif key == "medium" or key == "normal":
            color = (220, 150, 50)
        else:
            color = (50, 200, 100)

        draw_bar(screen, x, y, 180, 10, value, color, key)
        y += 30