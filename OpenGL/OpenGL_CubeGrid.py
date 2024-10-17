from pygame import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Initialize pygame and OpenGL
init()

# Set OpenGL attributes for multisampling (anti-aliasing) and VSync
display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
display.gl_set_attribute(GL_MULTISAMPLESAMPLES, 4)  # 4x MSAA
display.gl_set_attribute(GL_SWAP_CONTROL, 1)  # Enable VSync
display.gl_set_attribute(GL_DEPTH_SIZE, 24)  # Ensure 24-bit depth buffer precision

# Set up the screen to be fullscreen and 1440x900 resolution
width, height = 1440, 900
screen = display.set_mode((width, height), DOUBLEBUF | OPENGL | FULLSCREEN)

# Set up perspective
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0, 0, -20)  # Move camera back to see the cubes

# Enable depth testing and lighting
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHT1)

# Light properties for the first light (front light)
light_position_0 = [5, 5, 5, 1]  # Light from the front-top-right
light_ambient_0 = [0.1, 0.1, 0.1, 1.0]  # Lower ambient for more sharp highlights
light_diffuse_0 = [0.8, 0.8, 0.8, 1.0]  # Strong diffuse light
light_specular_0 = [1.0, 1.0, 1.0, 1.0]  # Strong specular highlight

# Light properties for the second light (side light)
light_position_1 = [-5, 5, 5, 1]  # Light from the left
light_ambient_1 = [0.1, 0.1, 0.1, 1.0]
light_diffuse_1 = [0.6, 0.6, 0.6, 1.0]  # Softer light on the side
light_specular_1 = [1.0, 1.0, 1.0, 1.0]

# Set the light properties for light 0
glLightfv(GL_LIGHT0, GL_POSITION, light_position_0)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient_0)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse_0)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular_0)

# Set the light properties for light 1
glLightfv(GL_LIGHT1, GL_POSITION, light_position_1)
glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient_1)
glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse_1)
glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular_1)

# Function to apply metallic material properties with very shiny specular highlights
def apply_metallic_material():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])  # Low ambient for shinier appearance
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.4, 0.4, 0.4, 1.0])  # Lower diffuse, focusing on specular reflection
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Strong white specular reflection
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 128.0)  # Maximum shininess for sharp highlights

# Function to draw a cube
def draw_cube(scale=1.0):
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]) * scale
    surfaces = [
        [0, 1, 2, 3], [4, 5, 6, 7],
        [0, 1, 5, 4], [2, 3, 7, 6],
        [0, 3, 7, 4], [1, 2, 6, 5]
    ]
    normals = [
        [0, 0, -1], [0, 0, 1], [0, -1, 0],
        [0, 1, 0], [-1, 0, 0], [1, 0, 0]
    ]

    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glNormal3fv(normals[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

# Create a grid of cubes (5x5)
class CubeGrid:
    def __init__(self, rows, cols, cube_size=2):
        self.rows = rows
        self.cols = cols
        self.cubes = []
        self.cube_size = cube_size
        self.gap = cube_size + 1  # Gap between cubes
        self.init_grid()

    def init_grid(self):
        # Initialize cubes in a grid pattern
        for row in range(self.rows):
            for col in range(self.cols):
                x = (col - self.cols // 2) * self.gap
                y = (row - self.rows // 2) * self.gap
                self.cubes.append({
                    "position": [x, y, 0],
                    "rotation": [0, 0, 0],
                    "rotation_speed": [np.random.uniform(0.2, 0.5), np.random.uniform(0.2, 0.5), np.random.uniform(0.2, 0.5)],
                })

    def update(self):
        for cube in self.cubes:
            cube["rotation"] = [(r + s) % 360 for r, s in zip(cube["rotation"], cube["rotation_speed"])]

    def draw(self):
        # Draw all cubes
        for cube in self.cubes:
            glPushMatrix()
            glTranslatef(*cube["position"])
            glRotatef(cube["rotation"][0], 1, 0, 0)
            glRotatef(cube["rotation"][1], 0, 1, 0)
            glRotatef(cube["rotation"][2], 0, 0, 1)
            apply_metallic_material()
            draw_cube(self.cube_size)
            glPopMatrix()

# Main loop to display and rotate the cubes
def run():
    grid = CubeGrid(5, 9)  # Create a 5x5 grid of cubes
    clock = time.Clock()
    running = True

    while running:
        for e in event.get():
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
                running = False

        # Clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLightfv(GL_LIGHT0, GL_POSITION, light_position_0)
        glLightfv(GL_LIGHT1, GL_POSITION, light_position_1)

        # Update and draw the cubes
        grid.update()
        grid.draw()

        # Swap buffers and tick the clock
        display.flip()
        clock.tick(60)

    quit()

# Run the script
run()
