import pygame


RULE_TEXTS = [
    "RED → slow",
    "YELLOW + close → slow",
    "YELLOW + medium → medium",
    "YELLOW + far → medium",
    "GREEN + close → slow",
    "GREEN + medium + wet → slow",
    "GREEN + medium + normal → medium",
    "GREEN + medium + dry → medium",
    "GREEN + far + wet → medium",
    "GREEN + far + normal → fast",
    "GREEN + far + dry → fast",
    "School Zone → slow",
    "City + far → medium",
    "Highway + far → fast"
]

def draw_rules_panel(screen, x, y, strengths):
    font = pygame.font.SysFont("Arial", 12)
    panel_width = 280
    max_rules = 12

    for i, (rule, strength) in enumerate(zip(RULE_TEXTS[:max_rules], strengths[:max_rules])):
        is_active = strength > 0.01

        if is_active:
            bg_color = (40, 80, 40)
            text_color = (150, 255, 150)
        else:
            bg_color = (50, 50, 50)
            text_color = (180, 180, 180)

        pygame.draw.rect(screen, bg_color, (x, y + i * 32, panel_width, 26))

        text_surface = font.render(rule, True, text_color)
        screen.blit(text_surface, (x + 5, y + i * 32 + 5))

        strength_text = font.render(f"{strength:.2f}", True, text_color)
        screen.blit(strength_text, (x + panel_width - 40, y + i * 32 + 5))