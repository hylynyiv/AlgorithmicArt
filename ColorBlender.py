from pygame import *
from pygame.locals import *
from sys import exit

screen = display.set_mode((640,480),0,32)

init()
clock = time.Clock()


color1  = (200,0,255)
color2 = (100,30,255)
factor = 0


def blend_color(col1, col2, fact):
    red1, green1, blue1 = col1
    red2, green2, blue2 = col2
    red = red1 +(red2-red1) * fact
    green = green1 + (green2-green1) * fact
    blue = blue1 + (blue2-blue1) * fact
    return int(red), int(green), int(blue)

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    screen.fill((255, 255, 255))

    tri = [ (0,200), (640,100), (640,200) ]
    draw.polygon(screen, (0,0,0), tri)
    draw.circle(screen, (0,0,0), (int(factor * 640.), 120), 10)

    x,y = mouse.get_pos()
    if mouse.get_pressed()[0]:
        factor = x/640.
        display.set_caption("Pygame Color Blend Test - %.3f" %factor)

    color = blend_color(color1, color2, factor)
    draw.rect(screen, color, (0,240,640,240))

    display.update()
    clock.tick(60)


quit()
exit()