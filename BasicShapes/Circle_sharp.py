from pygame import *
from pygame.locals import QUIT
from sys import exit
from pygame import gfxdraw

# Initialize Pygame
init()

# Set up the clock for framerate control
clock = time.Clock()

# Define your screen dimensions
window_size = (400, 400)

# Create the window surface
screen = display.set_mode(window_size)

# Define the virtual screen (surface) size - make sure it's proportional to the window size to avoid distortion
virtual_screen_size = (800, 800)
virtual_screen = Surface(virtual_screen_size)

# Define colors
sky_blue = (135, 206, 235)  # Sky blue color
black = (0, 0, 0)           # Black color

# Fill the virtual screen with black
virtual_screen.fill(black)

# Calculate the center and radius based on virtual screen size
center = (virtual_screen_size[0] // 2, virtual_screen_size[1] // 2)
radius = virtual_screen_size[0] // 8  # Example radius size

# Draw an anti-aliased ellipse on the virtual screen
gfxdraw.filled_ellipse(virtual_screen, center[0], center[1], radius, radius, sky_blue)
gfxdraw.aaellipse(virtual_screen, center[0], center[1], radius, radius, sky_blue)

# Scale the virtual screen down to the window size and blit it to the window surface
transform.smoothscale(virtual_screen, window_size, screen)

# Update the display
display.update()

# Main game loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False # leave the game 
    clock.tick(30)  # limit framerate to 30 frames per second

quit() # uninitialise all Pygame modules, release all resources
exit() # exit program execution and Python interpreter

