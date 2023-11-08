from pygame import *
from pygame.locals import *
from sys import exit

init()
clock = time.Clock()

offset = 0

screen = display.set_mode((1000,1000))
display.set_caption("Hello World!")

color = (100,0,255)
position = (350,300)
size = (300,400)

draw.rect(screen, color, ( position, size ) )
display.update()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False 
    clock.tick(5) 

quit() 
exit() 
