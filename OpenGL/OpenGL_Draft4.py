from pygame import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from random import uniform, randint
import time as pytime

# Initialize pygame and OpenGL
init()

# Set OpenGL attributes for multisampling (anti-aliasing) and VSync
display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
display.gl_set_attribute(GL_MULTISAMPLESAMPLES, 4)  # 4x MSAA
display.gl_set_attribute(GL_SWAP_CONTROL, 1)  # Enable VSync
display.gl_set_attribute(GL_DEPTH_SIZE, 24)  # Ensure 24-bit depth buffer precision

# Set up display to be fullscreen
width = 1440
height = 900
screen = display.set_mode((width, height), DOUBLEBUF | OPENGL | FULLSCREEN)

# Set up perspective and translation
gluPerspective(45, (width / height), 1.0, 120.0)  # Adjust near and far clipping planes
glTranslatef(0, 0, -30)  # Move the camera back to view the scene

# Set a fixed frame rate
fps = 30
clock = time.Clock()

# Function to generate a random color
def random_color():
    return [uniform(0.4, 1.0), uniform(0.4, 1.0), uniform(0.4, 1.0)]

# Function to interpolate between two colors
def lerp_color(current, target, t):
    return [(1 - t) * c + t * tc for c, tc in zip(current, target)]

class Background:
    def __init__(self, transition_duration=3.0):
        self.corners = [{'current_color': random_color(), 'target_color': random_color(), 'color_step': [0, 0, 0]} for _ in range(4)]
        self.frames_to_transition = int(transition_duration * 30)  # Assuming 30 FPS
        self.current_frame = 0
        self.calculate_color_steps()

    def calculate_color_steps(self):
        """ Calculate the color step per frame based on the current and target colors. """
        for corner in self.corners:
            corner['color_step'] = [(tc - cc) / self.frames_to_transition for cc, tc in zip(corner['current_color'], corner['target_color'])]

    def update_colors(self):
        """ Update the current colors for each corner, gradually moving toward the target. """
        for corner in self.corners:
            for i in range(3):  # For R, G, B values
                corner['current_color'][i] += corner['color_step'][i]

        # After completing the transition, set new target colors
        self.current_frame += 1
        if self.current_frame >= self.frames_to_transition:
            for corner in self.corners:
                corner['target_color'] = random_color()
            self.calculate_color_steps()  # Recalculate the steps for the next transition
            self.current_frame = 0

    def draw(self):
        """ Draw the background quad with gradient corners. """
        glPushMatrix()
        glTranslatef(0, 0, -70)  # Push the background further back
        glBegin(GL_QUADS)

        # Top-left
        glColor3fv(self.corners[0]['current_color'])
        glVertex3f(-100, 100, 0)

        # Top-right
        glColor3fv(self.corners[1]['current_color'])
        glVertex3f(100, 100, 0)

        # Bottom-right
        glColor3fv(self.corners[2]['current_color'])
        glVertex3f(100, -100, 0)

        # Bottom-left
        glColor3fv(self.corners[3]['current_color'])
        glVertex3f(-100, -100, 0)

        glEnd()
        glPopMatrix()


class Shape3D:
    def __init__(self, transition_duration=3.0):
        self.vertices = self.generate_random_vertices()  # Generate random vertices
        self.edges = self.generate_edges()  # Generate edges connecting vertices
        self.surfaces = self.generate_surfaces()  # Generate random surfaces connecting vertices

        self.current_color = self.random_neon_color()  # Initial color for each surface
        self.target_color = self.random_neon_color()  # Target color to transition to
        self.color_step = [[0, 0, 0] for _ in range(len(self.surfaces))]  # Step values for color transition

        self.frames_to_transition = int(transition_duration * 30)  # 3-second transition at 30 FPS (90 frames)
        self.current_frame = 0
        self.calculate_color_steps()

        # Randomized rotation speed for each axis
        self.rotation_speed_x = uniform(0.1, 1.0)
        self.rotation_speed_y = uniform(0.1, 1.0)
        self.rotation_speed_z = uniform(0.1, 1.0)

        self.rotation_angle_x = 0  # Initial rotation angle for X-axis
        self.rotation_angle_y = 0  # Initial rotation angle for Y-axis
        self.rotation_angle_z = 0  # Initial rotation angle for Z-axis

        # Position drift parameters (increased variation)
        self.position = [uniform(-5, 5), uniform(-5, 5), uniform(-15, -8)]  # Initial position
        self.drift_direction = [uniform(-0.05, 0.05), uniform(-0.05, 0.05), uniform(-0.05, 0.05)]  # Initial drift
        self.last_direction_change = pytime.time()  # Time for tracking direction change


    def generate_random_vertices(self, num_vertices=randint(10, 25)):
        """ Generate random 3D vertices for the shape. """
        vertices = []
        for _ in range(num_vertices):
            x = uniform(-4, 4)
            y = uniform(-4, 4)
            z = uniform(-4, 4)
            vertices.append((x, y, z))
        return vertices

    def generate_edges(self):
        """ Generate edges by connecting adjacent vertices. """
        edges = []
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if uniform(0, 1) < 0.5:  # Randomly connect vertices
                    edges.append((i, j))
        return edges

    def generate_surfaces(self):
        """ Generate random surfaces connecting vertices. """
        surfaces = []
        num_vertices = len(self.vertices)
        num_surfaces = randint(5, num_vertices)  # Random number of surfaces
        for _ in range(num_surfaces):
            surface = []
            for _ in range(randint(3, 4)):  # Randomly choose between 3 (triangle) or 4 (quad)
                surface.append(randint(0, num_vertices - 1))
            surfaces.append(surface)
        return surfaces

    def random_neon_color(self):
        """ Generate random neon-like colors for each face. """
        return [random_color() for _ in range(len(self.surfaces))]

    def calculate_color_steps(self):
        """ Calculate the color step per frame based on the current and target colors. """
        self.color_step = [
            [(tc - cc) / self.frames_to_transition for cc, tc in zip(current, target)]
            for current, target in zip(self.current_color, self.target_color)
        ]

    def update_colors(self):
        """ Update the current colors for each surface, gradually moving toward the target. """
        for i in range(len(self.current_color)):
            for j in range(3):  # For R, G, B values
                self.current_color[i][j] += self.color_step[i][j]

        # After completing the transition, set new target colors and recalculate the steps
        self.current_frame += 1
        if self.current_frame >= self.frames_to_transition:
            self.target_color = self.random_neon_color()
            self.calculate_color_steps()  # Recalculate the steps for the next transition
            self.current_frame = 0

    def update_position(self):
        """ Update the position of the object with slow drifting movement and occasional direction changes. """
        current_time = pytime.time()
        time_since_change = current_time - self.last_direction_change

        # Change direction every 1 to 4 seconds
        if time_since_change > uniform(1, 4):
            # Randomize drift direction (increased variation for direction changes)
            self.drift_direction = [uniform(-0.05, 0.05), uniform(-0.05, 0.05), uniform(-0.05, 0.05)]
            self.last_direction_change = current_time  # Reset the timer for the next direction change

        # Update position based on the drift direction
        for i in range(3):  # Iterate over x, y, z coordinates
            self.position[i] += self.drift_direction[i]

        # Keep the objects from drifting too far away
        self.position[0] = max(min(self.position[0], 40), -40)  # Limit x-axis
        self.position[1] = max(min(self.position[1], 10), -10)  # Limit y-axis
        self.position[2] = max(min(self.position[2], -8), -20)  # Limit z-axis (closer to camera)

    def rotate(self):
        """ Apply independent slow rotation with random strength on all axes. """
        self.rotation_angle_x += self.rotation_speed_x  # Increment angle for X-axis
        self.rotation_angle_y += self.rotation_speed_y  # Increment angle for Y-axis
        self.rotation_angle_z += self.rotation_speed_z  # Increment angle for Z-axis

        glRotatef(self.rotation_angle_x, 1, 0, 0)  # Rotate along the X-axis
        glRotatef(self.rotation_angle_y, 0, 1, 0)  # Rotate along the Y-axis
        glRotatef(self.rotation_angle_z, 0, 0, 1)  # Rotate along the Z-axis

    def draw(self):
        glPushMatrix()  # Save the current matrix

        self.update_position()  # Update the position of the object
        glTranslatef(*self.position)  # Move the object to its current position

        self.rotate()  # Apply individual rotation for each object
        self.update_colors()  # Gradually update the color

        # Enable polygon offset to reduce z-fighting between surfaces
        glEnable(GL_POLYGON_OFFSET_FILL)
        glPolygonOffset(1.0, 1.0)

        # Draw the surfaces
        glBegin(GL_QUADS if len(self.surfaces[0]) == 4 else GL_TRIANGLES)
        for surface in self.surfaces:
            color = self.current_color[self.surfaces.index(surface)]  # Get the current color for the surface
            glColor3fv(color)  # Apply the interpolated color to the surface
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        # Draw transparent edges (almost fully transparent)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glLineWidth(1.5)
        glBegin(GL_LINES)
        glColor4f(0.0, 0.0, 0.0, 0.01)  # Completely transparent black for edges
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        glDisable(GL_BLEND)

        # Disable polygon offset after drawing surfaces
        glDisable(GL_POLYGON_OFFSET_FILL)

        glPopMatrix()  # Restore the previous matrix after rotating and drawing

# Create the gradient background
background = Background()

# Create random shapes
shapes = [Shape3D() for _ in range(10)]  # Create 10 random shapes

# Main event loop
running = True
while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):  # Close window with Q
            running = False

    # Clear both color and depth buffers before rendering
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Update and draw the gradient background
    background.update_colors()
    background.draw()

    # Draw all shapes
    for shape in shapes:
        shape.draw()

    # Update display and manage framerate
    display.flip()
    clock.tick(fps)  # Maintain 30 FPS for smoother animation

quit()
exit()
