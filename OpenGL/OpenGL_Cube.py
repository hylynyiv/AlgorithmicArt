from pygame import *
from pygame.locals import *
from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *

init()
clock = time.Clock()
width = 1000
height = 800
screen = display.set_mode((width,height), DOUBLEBUF | OPENGL)


fieldOfView = 45
aspectRatio = (width/height)
clippingPlane_near = 0.1
clippingPlane_far = 50

gluPerspective(fieldOfView, aspectRatio, clippingPlane_near, clippingPlane_far)


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
    (0,1),
    (0,2),
    (0,4),
    (1,3),
    (1,5),
    (2,3),
    (2,6),
    (3,7),
    (4,5),
    (4,6),
    (5,7),
    (6,7)
    )


def draw_Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

glTranslatef(0.0,0.0, -5)

running = True
while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False

    glRotatef(4,1,1,1)
    #glRotatef(1,10,1,1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_Cube()

    display.flip()

    clock.tick(30)

quit()
exit()