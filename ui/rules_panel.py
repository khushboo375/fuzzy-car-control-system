import pygame


RULE_TEXTS = [

    #  RED
    "IF red AND far → slow",
    "IF red AND medium → slow",
    "IF red AND close → slow",
    "IF red AND wet → slow",

    #  YELLOW
    "IF yellow AND close → slow",
    "IF yellow AND medium AND wet → slow",
    "IF yellow AND medium AND normal → medium",
    "IF yellow AND far AND dry → medium",

    #  GREEN
    "IF green AND close → slow",
    "IF green AND medium AND wet → slow",
    "IF green AND medium AND normal → medium",
    "IF green AND medium AND dry → medium",
    "IF green AND far AND wet → medium",
    "IF green AND far AND normal → fast",
    "IF green AND far AND dry → fast",

    # 🌧 OVERRIDES
    "IF wet AND close → slow",
    "IF wet AND medium → medium",

    # DEFAULT
    "IF medium → medium"
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