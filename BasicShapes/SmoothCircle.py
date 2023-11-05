import pygame
from pygame import gfxdraw

# Initialize Pygame
pygame.init()

# Set up the clock for framerate control
clock = pygame.time.Clock()

# Define your screen dimensions
window_size = (400, 400)

# Create the window surface
screen = pygame.display.set_mode(window_size)

# Define the virtual screen (surface) size - make sure it's proportional to the window size to avoid distortion
virtual_screen_size = (800, 800)
virtual_screen = pygame.Surface(virtual_screen_size)

# Define colors
sky_blue = (135, 206, 235)  # Sky blue color
black = (0, 0, 0)           # Black color

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the virtual screen with black
    virtual_screen.fill(black)

    # Calculate the center and radius based on virtual screen size
    center = (virtual_screen_size[0] // 2, virtual_screen_size[1] // 2)
    radius = virtual_screen_size[0] // 8  # Example radius size

    # Draw an anti-aliased ellipse on the virtual screen
    gfxdraw.filled_ellipse(virtual_screen, center[0], center[1], radius, radius, sky_blue)
    gfxdraw.aaellipse(virtual_screen, center[0], center[1], radius, radius, sky_blue)

    # Scale the virtual screen down to the window size and blit it to the window surface
    pygame.transform.smoothscale(virtual_screen, window_size, screen)

    # Update the display
    pygame.display.update()

    # Cap the framerate
    clock.tick(30)