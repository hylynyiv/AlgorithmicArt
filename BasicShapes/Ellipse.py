from pygame import *
from pygame.locals import *
from webcolors import *

init()

clock = time.Clock()

screen = display.set_mode((500,500))

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()

    draw.ellipse(screen, name_to_rgb("skyblue"), ( (200,200), (100,50) ) )

    display.update()

    clock.tick(30)
