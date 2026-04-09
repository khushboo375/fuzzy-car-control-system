import pygame


RULE_TEXTS = [
    "IF close AND wet → slow",
    "IF close AND normal → slow",
    "IF close AND dry → slow",
    "IF medium AND wet → slow",
    "IF medium AND normal → medium",
    "IF medium AND dry → medium",
    "IF far AND wet → medium",
    "IF far AND normal → fast",
    "IF far AND dry → fast",
    "IF close → slow (override)"
]


def draw_rules_panel(screen, x, y, strengths):
    font = pygame.font.SysFont("Arial", 12)

    for i, (rule, strength) in enumerate(zip(RULE_TEXTS, strengths)):
        is_active = strength > 0.01

        # Background color
        if is_active:
            bg_color = (40, 80, 40)  # green highlight
            text_color = (150, 255, 150)
        else:
            bg_color = (50, 50, 50)
            text_color = (180, 180, 180)

        # Draw box
        pygame.draw.rect(screen, bg_color, (x, y + i * 30, 220, 25))

        # Rule text
        text_surface = font.render(rule, True, text_color)
        screen.blit(text_surface, (x + 5, y + i * 30 + 5))

        # Strength value
        strength_text = font.render(f"{strength:.2f}", True, text_color)
        screen.blit(strength_text, (x + 180, y + i * 30 + 5))