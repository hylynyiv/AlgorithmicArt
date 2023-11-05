from pygame import *
from pygame.locals import *
from webcolors import *

init()
clock = time.Clock()

offset = 0

screen = display.set_mode((400,400))
display.set_caption("Hello World!")

while True:

    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()

    draw.rect(screen, name_to_rgb("slateblue"), ( (100,100), (100,100) ) )

    #screen.fill((255,0,0))

    display.update()
    clock.tick(60)