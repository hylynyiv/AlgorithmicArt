from pygame import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import *
import time as pytime

# Initialize pygame and set up the OpenGL context
init()

# Set display mode for a 1440x900 fullscreen window
width = 1440
height = 900
screen = display.set_mode((width, height), DOUBLEBUF | OPENGL | FULLSCREEN)

# Set up basic OpenGL settings
gluOrtho2D(-1, 1, -1, 1)  # Set up orthographic projection (2D view)

# Function to generate a random vibrant color with more variance in lightness
def random_color():
    return [uniform(0.4, 1.0), uniform(0.4, 1.0), uniform(0.4, 1.0)]

# Function for linear interpolation between two colors
def lerp_color(current, target, t):
    return [(1 - t) * c + t * tc for c, tc in zip(current, target)]

class QuadColorTransition:
    def __init__(self, transition_time=3.0, fps=60):
        # Each corner has its own current, target, and color step
        self.corners = [{'current_color': random_color(), 'target_color': random_color(), 'color_step': [0, 0, 0]} for _ in range(4)]
        self.transition_time = transition_time  # Transition duration in seconds
        self.fps = fps  # Frames per second
        self.frames_to_transition = int(self.transition_time * self.fps)  # Total frames for transition

        # Calculate the initial color step for each corner
        for corner in self.corners:
            self.calculate_color_step(corner)

    def calculate_color_step(self, corner):
        """ Calculate the color step per frame based on the current and target colors. """
        corner['color_step'] = [(tc - cc) / self.frames_to_transition for cc, tc in zip(corner['current_color'], corner['target_color'])]

    def update_colors(self):
        """ Update the current colors by adding a small step towards the target color for each corner. """
        for corner in self.corners:
            corner['current_color'] = [cc + step for cc, step in zip(corner['current_color'], corner['color_step'])]

            # If we're close enough to the target color, generate a new distinct target color
            if all(abs(tc - cc) < 0.01 for cc, tc in zip(corner['current_color'], corner['target_color'])):
                # Ensure that the new color is distinct from the other corners
                new_color = random_color()
                while any(new_color == other['target_color'] for other in self.corners):
                    new_color = random_color()
                corner['target_color'] = new_color
                self.calculate_color_step(corner)

    def draw_quad(self):
        """ Draw a quad with independent colors for each corner. """
        glBegin(GL_QUADS)

        # Top-left
        glColor3fv(self.corners[0]['current_color'])
        glVertex2f(-1.0, 1.0)  # Top-left corner

        # Top-right
        glColor3fv(self.corners[1]['current_color'])
        glVertex2f(1.0, 1.0)  # Top-right corner

        # Bottom-right
        glColor3fv(self.corners[2]['current_color'])
        glVertex2f(1.0, -1.0)  # Bottom-right corner

        # Bottom-left
        glColor3fv(self.corners[3]['current_color'])
        glVertex2f(-1.0, -1.0) # Bottom-left corner

        glEnd()

# Create an instance of the quad color transition with 3 seconds for each transition
quad_transition = QuadColorTransition(transition_time=3.0, fps=60)

# Main loop
running = True
clock = time.Clock()  # To maintain the refresh rate

while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    # Update the quad's color gradually for each corner
    quad_transition.update_colors()

    # Draw the quad with the current colors in the four corners
    quad_transition.draw_quad()

    # Update the display
    display.flip()

    # Maintain 60 FPS
    clock.tick(60)

quit()
