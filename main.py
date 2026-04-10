import pygame
import sys

from config import *
from fuzzy.fuzzy_logic import FuzzyCarController
from ui.gauge import Speedometer
from ui.bars import draw_membership_panel
from ui.rules_panel import draw_rules_panel
from simulation.road import Road
from simulation.car import Car, FrontCar
from simulation.rain import Rain
from ui.dashboard import Dashboard
from utils.logger import DataLogger

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fuzzy Logic Car Speed Control")

clock = pygame.time.Clock()

controller = FuzzyCarController()

distance = 50
road = 5
smooth_speed = 60
is_night = False  
light = 8


# =========================
# DRAW FUNCTIONS
# =========================
def draw_layout():
    if is_night:
        bg = (10, 10, 30)
        panel = (20, 20, 50)
    else:
        bg = BG_COLOR
        panel = PANEL_COLOR

    screen.fill(bg)

    pygame.draw.rect(screen, panel, (0, 0, LEFT_PANEL_WIDTH, HEIGHT))
    pygame.draw.rect(screen, panel,
                     (WIDTH - RIGHT_PANEL_WIDTH, 0, RIGHT_PANEL_WIDTH, HEIGHT))

    pygame.draw.rect(screen, (60, 60, 60),
                     (LEFT_PANEL_WIDTH, 0,
                      WIDTH - LEFT_PANEL_WIDTH - RIGHT_PANEL_WIDTH, HEIGHT), 2)


def draw_text(text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.SysFont("Arial", size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def draw_headlights(screen, car_x, car_y):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    # Dark overlay
    overlay.fill((0, 0, 0, 180))

    # Headlight cone
    points = [
        (car_x + 20, car_y),
        (car_x - 120, car_y - 300),
        (car_x + 160, car_y - 300)
    ]

    pygame.draw.polygon(overlay, (0, 0, 0, 0), points)
    screen.blit(overlay, (0, 0))


# =========================
# INPUT
# =========================
def handle_input():
    global distance, road

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        distance = min(100, distance + 0.5)
    if keys[pygame.K_DOWN]:
        distance = max(0, distance - 0.5)

    if keys[pygame.K_w]:
        road = 1
    if keys[pygame.K_n]:
        road = 5
    if keys[pygame.K_d]:
        road = 9

    global light
    if keys[pygame.K_r]:
        light = 1   # red
    if keys[pygame.K_y]:
        light = 5   # yellow
    if keys[pygame.K_g]:
        light = 9   # green

def draw_mini_signal(screen, x, y, light):
    # Background box
    pygame.draw.rect(screen, (40, 40, 40), (x, y, 30, 70), border_radius=6)

    # Positions of lights
    positions = [
        (x + 15, y + 12),  # red
        (x + 15, y + 35),  # yellow
        (x + 15, y + 58)   # green
    ]

    colors = [
        (255, 0, 0),
        (255, 255, 0),
        (0, 255, 0)
    ]

    # Draw lights
    for i, (px, py) in enumerate(positions):
        active = (
            (i == 0 and light <= 3) or
            (i == 1 and 3 < light <= 6) or
            (i == 2 and light > 6)
        )

        if active:
            pygame.draw.circle(screen, colors[i], (px, py), 6)
        else:
            pygame.draw.circle(screen, (80, 80, 80), (px, py), 6)

# =========================
# MAIN LOOP
# =========================
def main():
    global smooth_speed, is_night

    running = True
    rain = Rain(WIDTH, HEIGHT)

    center_x = LEFT_PANEL_WIDTH
    center_width = WIDTH - LEFT_PANEL_WIDTH - RIGHT_PANEL_WIDTH

    # Road + lanes
    road_sim = Road(center_x, center_width, HEIGHT)
    lane_width = center_width // 3

    player_lane = 1
    player_x = center_x + player_lane * lane_width + lane_width // 2 - 20

    player_car = Car(player_x, HEIGHT - 120)
    front_car = FrontCar(player_x)

    gauge = Speedometer(WIDTH // 2, HEIGHT // 2)

    #  Move dashboard LOWER (fix overlap)
    dashboard = Dashboard(WIDTH // 2 - 150, HEIGHT - 60, 300)

    engine_sound = pygame.mixer.Sound("assets/sounds/engine.wav")
    beep_sound = pygame.mixer.Sound("assets/sounds/beep.wav")

    engine_sound.play(-1)  # loop forever
    beep_timer = 0

    logger = DataLogger()

    while running:
        clock.tick(60)
        dashboard.update(smooth_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # 🌙 Toggle day/night
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    is_night = not is_night

        handle_input()

        result = controller.compute(distance, road, light)
        target_speed = result["speed"]

        smooth_speed += (target_speed - smooth_speed) * 0.1

        logger.log(distance, road, light, smooth_speed)
        
        # Engine sound based on speed
        volume = min(1.0, smooth_speed / 120)
        engine_sound.set_volume(volume)
        # Brake warning sound
        if distance < 15:
            beep_timer += 1

            delay = 10 if distance < 8 else 30

            if beep_timer > delay:
                beep_sound.play()
                beep_timer = 0
        else:
            beep_timer = 0

        # Update simulation
        road_sim.update(smooth_speed)
        rain.update(smooth_speed)

        # =========================
        # DRAW
        # =========================
        draw_layout()

        # Simulation
        road_sim.draw(screen)
        front_car.draw(screen, distance)
        player_car.draw(screen)

        # Rain
        if road <= 2:
            rain.draw(screen)

        #  Headlights
        if is_night:
            draw_headlights(screen, player_car.x, player_car.y)

        # LEFT PANEL
        draw_text("INPUTS", 18, 20, 20)
        draw_text(f"Distance: {int(distance)} m", 16, 20, 70)

        road_label = "Wet" if road <= 2 else "Normal" if road <= 7 else "Dry"
        draw_text(f"Road: {road_label}", 16, 20, 110)
        draw_text("Signal:", 16, 20, 140)
        draw_mini_signal(screen, 200, 135, light)

        draw_text("Controls:", 14, 20, 160)
        draw_text("UP/DOWN → Distance", 12, 20, 190)
        draw_text("W/N/D → Road", 12, 20, 210)
        draw_text("T → Day/Night", 12, 20, 230)
        draw_text("R/Y/G → Signal", 12, 20, 250)

        draw_membership_panel(screen, 20, 300,
            result["distance_mf"], "Distance Membership")

        draw_membership_panel(screen, 20, 420,
            result["road_mf"], "Road Membership")

        # CENTER PANEL
        draw_text("OUTPUT", 18, WIDTH // 2 - 40, 20)

        gauge.draw(screen, smooth_speed)

        draw_text(f"{int(smooth_speed)}", 40,
                  WIDTH // 2 - 25, HEIGHT // 2 - 20)
        draw_text("km/h", 18,
                  WIDTH // 2 - 20, HEIGHT // 2 + 20)

        #  Dashboard (now BELOW car)
        dashboard.draw_speed_graph(screen)
        dashboard.draw_distance_bar(screen, distance)

        # Mode
        if smooth_speed < 45:
            mode = "SLOW"
            color = (220, 70, 70)
        elif smooth_speed < 80:
            mode = "MEDIUM"
            color = (220, 150, 50)
        else:
            mode = "FAST"
            color = (50, 200, 100)

        draw_text(mode, 24,
                  WIDTH // 2 - 50, HEIGHT // 2 + 50, color)

        # Brake warning
        if distance < 15:
            draw_text("⚠ BRAKE WARNING!", 20,
                      WIDTH // 2 - 100, HEIGHT // 2 + 100, (255, 50, 50))

        # RIGHT PANEL
        draw_text("RULES", 18, WIDTH - RIGHT_PANEL_WIDTH + 20, 20)

        draw_rules_panel(
            screen,
            WIDTH - RIGHT_PANEL_WIDTH + 10,
            80,
            result["rule_strengths"]
        )

        active_rules = sum(1 for r in result["rule_strengths"] if r > 0.01)
        rules_start_y = 60
        rule_height = 32
        num_rules_displayed = min(len(result["rule_strengths"]), 12)

        active_rules_y = rules_start_y + num_rules_displayed * rule_height + 20

        draw_text(f"Active Rules: {active_rules}", 14,
                WIDTH - RIGHT_PANEL_WIDTH + 20, active_rules_y)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()