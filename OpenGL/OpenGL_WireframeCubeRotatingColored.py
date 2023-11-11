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
screen.fill((0,0,0))

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

surfaces = (
    (0,1,2,3),
    (0,1,4,5),
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
    glBegin(GL_LINES)
    for edge in edges:
        i = 0
        for vertex in edge: 
            i += 1          
            glColor3fv(colors[i])
            glVertex3fv(vertices[vertex])           
    glEnd()

glTranslatef(0.0,0.0, -5)

running = True
while running:
    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_q):
            running = False

    glRotatef(1,10,1,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cube()
    display.flip()

    clock.tick(30)


quit()
exit()