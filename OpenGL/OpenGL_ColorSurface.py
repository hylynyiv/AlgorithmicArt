from pygame import *
from pygame.locals import *
from sys import exit
import pygame.time
from OpenGL.GL import *
from OpenGL.GLU import *

init()
clock = time.Clock()
width = 1000
height = 800
screen = display.set_mode((width, height), DOUBLEBUF | OPENGL)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -15)
rotation = 0

vertices = (
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1)
    )

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

surfaces = (
    (0,2,3,1),
    (0,1,5,4),
    (0,2,6,4),
    (7,3,1,5),
    (7,6,4,5),
    (7,6,2,3)
)

colors = (
    (0.5,0.5,1),
    (0,0.5,0.5),
    (1,0,1),
    (1,0.5,1),
    (0.5,1,1),
    (0.5,1,1)
)

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(colors[i % len(colors)])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glLineWidth(1)
    glEnable(GL_POLYGON_OFFSET_LINE)
    glPolygonOffset(-1, -1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    glDisable(GL_POLYGON_OFFSET_LINE)


z_position = -15

running = True
while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False
    
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset the view
    gluPerspective(45, (width / height), 0.1, 50.0)


    # Update the cube position
    # glRotatef(rotation,0,0,1)
    glTranslatef(-0.5, -0.5, z_position)

    rotation += 1
    z_position += 0.1
    if z_position > 1:
        z_position = -15

    # Render the cube
    Cube()

    display.flip()
    clock.tick(20)

quit()
exit()