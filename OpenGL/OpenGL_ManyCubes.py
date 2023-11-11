# from pygame import *
# from pygame.locals import *
# from sys import exit

# from OpenGL.GL import *
# from OpenGL.GLU import *

# from random import *

# init()
# clock = time.Clock()

# width = 800
# height = 800
# screen = display.set_mode((width, height), DOUBLEBUF|OPENGL)

# # foV = 45
# # aspectRatio = width/height
# # clipping_near = 0.1
# # clipping_far = 50
# # gluPerspective(foV, aspectRatio, clipping_near, clipping_far)

# fieldOfView = 45
# aspectRatio = (width/height)
# clippingPlane_near = 0.1
# clippingPlane_far = 50

# gluPerspective(fieldOfView, aspectRatio, clippingPlane_near, clippingPlane_far)


# glTranslatef(0,0,-5)

# def set_vertices(max_distance):
#         x_value_change = randrange(-10, 10)
#         y_value_change = randrange(-10, 10)
#         z_value_change = randrange(-max_distance, -20)

#         new_vertices = []

#         for vertex in vertices:
#             new_vertex = []

#             new_x = vertex[0] + x_value_change
#             new_y = vertex[1] + y_value_change
#             new_z = vertex[2] + z_value_change

#             new_vertex.append(new_x)
#             new_vertex.append(new_y)
#             new_vertex.append(new_z)

#             new_vertices.append(new_vertex)

#         return new_vertices


# vertices = (
#     (0,0,0),
#     (0,0,1),
#     (0,1,0),
#     (0,1,1),
#     (1,0,0),
#     (1,0,1),
#     (1,1,0),
#     (1,1,1)
#     )


# edges = (
#     (0,1),
#     (0,2),
#     (0,4),
#     (1,3),
#     (1,5),
#     (2,3),
#     (2,6),
#     (3,7),
#     (4,5),
#     (4,6),
#     (5,7),
#     (6,7)
#     )

# surfaces = (
#     (0,1,2,3),
#     (0,1,4,5),
#     (0,2,6,4),
#     (7,3,1,5),
#     (7,6,4,5),
#     (7,6,2,3)
# )

# colors = (
#     (0.5,0.5,1),
#     (0,0.5,0.5),
#     (1,0,1),
#     (1,0.5,1),
#     (0.5,1,1),
#     (0.5,1,1)
# )

# def Cube(vertices):

#     glBegin(GL_QUADS)

#     for surface in surfaces:
#         i = 0

#         for vertex in surface:
#             i += 1
#             glColor3fv(colors[i])
#             glVertex3fv(vertices[vertex])

#     glEnd()


# max_distance = 100

# cube_dict = {}

# xmove, ymove = 0, 0

# for i in range(20):
#     cube_dict[i] = set_vertices(max_distance)

# while True:
#     for e in event.get():
#         if e.type == QUIT:
#             quit()
#             exit()

#         if e.type == KEYDOWN:
#             if e.key == K_q:
#                 quit()
#                 exit()

#         if e.type == KEYDOWN:
#             if e.key == K_LEFT:
#                 glTranslatef(-0.5,0,0)
#             if e.key == K_RIGHT:
#                 glTranslatef(0.5,0,0)

#             if e.key == K_UP:
#                 glTranslatef(0,1,0)
#             if e.key == K_DOWN:
#                 glTranslatef(0,-1,0)

#         if e.type == MOUSEBUTTONDOWN:
#             if e.button == 4:
#                 glTranslatef(0,0,1.0)

#             if e.button == 5:
#                 glTranslatef(0,0,-1.0)

#     # x = glGetDoublev(GL_MODELVIEW_MATRIX)
#     # print(x)
#     #
#     #
#     # camera_x = x[3][0]
#     # camera_y = x[3][1]
#     # camera_z = x[3][2]

#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glTranslatef(xmove, ymove, 0.1)

#     for cube in cube_dict:
#         Cube(cube_dict[cube])

#     for key in list(cube_dict.keys()):
#         cube_dict[key] = [(x, y, z + 0.1) for x, y, z in cube_dict[key]]
#         if any(z > 1 for x, y, z in cube_dict[key]):
#             cube_dict[key] = set_vertices(max_distance)

#     display.flip()
#     clock.tick(60)


from pygame import *
from pygame.locals import *
from sys import exit

from OpenGL.GL import *
from OpenGL.GLU import *

from random import *

init()
clock = time.Clock()

width = 800
height = 800
screen = display.set_mode((width, height), DOUBLEBUF | OPENGL)

gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0, 0, -5)

vertices = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
)

edges = (
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (0, 1, 4, 5),
    (0, 2, 6, 4),
    (7, 3, 1, 5),
    (7, 6, 4, 5),
    (7, 6, 2, 3)
)

colors = (
    (0.5, 0.5, 1),
    (0, 0.5, 0.5),
    (1, 0, 1),
    (1, 0.5, 1),
    (0.5, 1, 1),
    (0.5, 1, 1)
)

def set_vertices(max_distance):
    x_value_change = randrange(-10, 10)
    y_value_change = randrange(-10, 10)
    z_value_change = randrange(-max_distance, -20)
    
    new_vertices = []
    for vertex in vertices:
        new_vertex = (vertex[0] + x_value_change, vertex[1] + y_value_change, vertex[2] + z_value_change)
        new_vertices.append(new_vertex)
    
    return new_vertices

def Cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glColor3fv(colors[i])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

max_distance = 100
cube_dict = {i: set_vertices(max_distance) for i in range(20)}

while True:
    for e in event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()

        if e.type == KEYDOWN:
            if e.key == K_q:
                pygame.quit()
                exit()

            if e.key == K_LEFT:
                glTranslatef(-0.5, 0, 0)
            if e.key == K_RIGHT:
                glTranslatef(0.5, 0, 0)

            if e.key == K_UP:
                glTranslatef(0, 1, 0)
            if e.key == K_DOWN:
                glTranslatef(0, -1, 0)

        if e.type == MOUSEBUTTONDOWN:
            if e.button == 4:
                glTranslatef(0, 0, 1.0)

            if e.button == 5:
                glTranslatef(0, 0, -1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for cube in cube_dict.values():
        Cube(cube)

    # Update the cubes' positions.
    for key in list(cube_dict.keys()):
        cube_dict[key] = [(x, y, z + 0.1) for x, y, z in cube_dict[key]]
        if any(z > 1 for x, y, z in cube_dict[key]):
            cube_dict[key] = set_vertices(max_distance)

    display.flip()
    clock.tick(60)
