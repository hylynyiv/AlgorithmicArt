from pygame import *
from pygame.locals import *
from sys import exit

init()
clock = time.Clock()

offset = 0

screen = display.set_mode((1000,1000))
display.set_caption("Hello World!")

color = (10,0,255)
position = (350,300)
size = (300,400)

draw.rect(screen, color, ( position, size ) )
display.update()

while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            exit()
    clock.tick(30)
