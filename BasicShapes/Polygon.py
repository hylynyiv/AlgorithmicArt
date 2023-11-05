from pygame import *
from pygame.locals import *

init()
clock = time.Clock()
window = display.set_mode((500,500))

draw.polygon(window, (100,134,234), ((0,0),(39,142), (221,350), (423,242)))

while True:

    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()

        elif e.type == KEYDOWN:
            if e.key == K_q:
                quit()
                exit()



    display.update()

    clock.tick(30)
