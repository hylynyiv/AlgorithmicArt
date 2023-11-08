from pygame import *
from pygame.locals import QUIT
from sys import exit
from math import pi

# Initialize Pygame
init()
clock = time.Clock()
window_size = (800, 600)
window = display.set_mode(window_size)

# Colors
color = (180, 180, 110)  # Yellow
background = (0, 0, 0)    # Black

# Arc properties
rect = Rect(200, 200, 400, 200)  # x, y, width, height for the arc
start_angle = 0
end_angle = pi
width = 2  # Thickness of the arc

# Clear screen with a black background
window.fill(background)

# Draw a semi-circle arc
draw.arc(window, color, rect, start_angle, end_angle, width)

# Update display
display.update()

# Main loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 
    clock.tick(5) 

quit() 
exit() 


    