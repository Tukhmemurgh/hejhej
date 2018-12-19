import pygame as pg
import math

def Mandelbrot(x, y, x0, y0, n_max):
    Re = x
    Im = y
    Re_temp = 0
    Im_temp = 0

    n = 0
    while n < n_max and Re**2 + Im**2 < 4:
        Re_temp = Re**2 - Im**2 + x0
        Im = 2*Re*Im + y0
        Re = Re_temp
        n += 1
    return colorgen(n, n_max)

def draw(screen, x, y, color, w, h):
    #screen.set_at((x, y), color)
    if(x > w or y > h):
        return
    pg.draw.rect(screen, color, pg.Rect(x-1, y-1, 1, 1))
def colorgen(n, n_max):
    red = round(255*n/n_max)
    green = round(255*n/n_max)
    blue = 0
    return (red, green, blue)

def main():
    (width, height) = (800, 600)
    pg.display.set_caption('Mandelbrot')
    screen = pg.display.set_mode((0,0), pg.FULLSCREEN | pg.DOUBLEBUF)
    dim = pg.display.Info()
    screen.set_alpha(None)
    w = dim.current_w*2
    h = dim.current_h*2
    for x in range(w+1):
        for y in range(round(h/2)+1):
            color = Mandelbrot(0, 0, 3*x/w-2, 2*y/h-1, 50)
            draw(screen, x, y, color, w, h)
            draw(screen, x, (h-y), color, w, h)

    running = True
    while running:
        running = not user_quit()
        pg.display.flip()

def user_quit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                return True
    return False



if __name__ == '__main__':
    main()
