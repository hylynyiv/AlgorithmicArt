from pygame import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time as pytime

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

# Set up perspective and translation
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0, 0, -5)

# Enable lighting
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

# Enable depth test and smooth shading
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)

# Light and material properties (with stronger diffuse and specular values)
light_position = [2, 2, 2, 1]
light_ambient = [0.2, 0.2, 0.2, 1.0]  # Lower ambient to avoid flattening the object
light_diffuse = [1.0, 1.0, 1.0, 1.0]  # Strong diffuse light to brighten the object
light_specular = [1.0, 1.0, 1.0, 1.0]  # Strong specular light for reflective surfaces

# Set the light position and properties
glLightfv(GL_LIGHT0, GL_POSITION, light_position)
glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

# Function to apply metallic material properties with stronger reflection
def apply_metallic_material():
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Slightly lower ambient material
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])  # Brighter diffuse material
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])  # Strong specular reflection
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 100.0)  # High shininess for more prominent specular highlights

# Define cube vertices and manually set normals for each face
vertices = np.array([
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Back face
    [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]  # Front face
])

# Define surfaces with the associated normal vectors
surfaces = [
    ([0, 1, 2, 3], [0, 0, -1]),  # Back face
    ([4, 5, 6, 7], [0, 0, 1]),   # Front face
    ([0, 1, 5, 4], [0, -1, 0]),  # Bottom face
    ([2, 3, 7, 6], [0, 1, 0]),   # Top face
    ([0, 3, 7, 4], [-1, 0, 0]),  # Left face
    ([1, 2, 6, 5], [1, 0, 0])    # Right face
]

# Function to draw the cube with static normals
def draw_cube():
    apply_metallic_material()

    # Draw each face of the cube with a manually assigned normal
    glBegin(GL_QUADS)
    for surface, normal in surfaces:
        glNormal3fv(normal)  # Set the normal for the surface
        for vertex in surface:
            glVertex3fv(vertices[vertex])  # Draw each vertex
    glEnd()

# Set up rotation angles
rotation_angle = [0, 0, 0]
rotation_speed = [0.5, 0.3, 0.7]  # Rotation speed on each axis

# Main loop
running = True
clock = time.Clock()

while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reapply the light position every frame to ensure it's preserved
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Apply rotation
    glPushMatrix()
    glRotatef(rotation_angle[0], 1, 0, 0)
    glRotatef(rotation_angle[1], 0, 1, 0)
    glRotatef(rotation_angle[2], 0, 0, 1)

    # Draw the rotating cube with simple metallic effect
    draw_cube()

    # Restore the matrix
    glPopMatrix()

    # Update the rotation angles
    rotation_angle[0] += rotation_speed[0]
    rotation_angle[1] += rotation_speed[1]
    rotation_angle[2] += rotation_speed[2]

    # Swap buffers and tick the clock
    display.flip()
    clock.tick(60)  # Lock at 60 FPS

# Quit the program
quit()
