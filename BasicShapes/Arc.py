import pygame
from math import pi

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
window_size = (800, 600)
window = pygame.display.set_mode(window_size)

# Colors
color = (180, 180, 110)  # White
background = (0, 0, 0)    # Black

# Arc properties
rect = pygame.Rect(200, 200, 400, 200)  # x, y, width, height for the arc
start_angle = 0
end_angle = pi
width = 2  # Thickness of the arc

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear screen with a black background
    window.fill(background)

    # Draw a semi-circle arc
    pygame.draw.arc(window, color, rect, start_angle, end_angle, width)

    # Update display
    pygame.display.update()

    # Tick the clock
    clock.tick(30)