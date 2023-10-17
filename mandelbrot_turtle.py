import turtle
import math

def mandelbrot(z, c, n=20):
    if abs(z) > 10 ** 12:
        return float("nan")
    elif n > 0:
        return mandelbrot(z**2 + c, c, n - 1) 
    else:
        return z**2 + c

# screen size (in pixels)
screenx = 1600
screeny = 1200

# complex plane limits, don't really need more than this
complexPlaneX = (-2.0, 2.0)
complexPlaneY = (-1.0, 2.0)

# step-wise progression
step = 2

# turtle stuff, probably could be done better
turtle.tracer(0, 0)
turtle.setup(screenx, screeny)
turtle.bgcolor("#010a75")
screen = turtle.Screen()
mTurtle = turtle.Turtle()
mTurtle.penup()

# plot_x * pixelToX = x in complex plane coordinates
pixelToX, pixelToY = (complexPlaneX[1] - complexPlaneX[0])/screenx, (complexPlaneY[1] - complexPlaneY[0])/screeny

# plot
for plot_x in range(-int(screenx/2), int(screenx/2), int(step)):
    for plot_y in range(-int(screeny/2), int(screeny/2), int(step)):
        x, y = plot_x * pixelToX, plot_y * pixelToY
        m =  mandelbrot(0, x + 1j * y) # note the use of j!
        if not math.isnan(m.real):
            color = [abs(math.sin(m.imag)) for i in range(3)]
            mTurtle.color(color)
            mTurtle.dot(2.4, color)
            mTurtle.goto(plot_x, plot_y)
    turtle.update()

turtle.mainloop()
