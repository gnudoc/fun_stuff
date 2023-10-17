
from PIL import Image
import colorsys
import math
import os

# lazy validation loop
while True:
    default = 1000 # takes about 40s on a typical laptop; 100 takes a couple of seconds, 10000 takes over an hour
    def_width = input("Enter desired width of frame - [default: 1000]: ").strip()
    if def_width.isdigit(): # is it a num?
        def_width = int(def_width)  # not an int?
        break
    else:
        if not def_width: # empty input?
            print("Defaulting to 1000...")
            def_width = default
            break
        else: # not a number?
            print("Input an integer for the width of the frame.")
        

# frame and basic conceptual limits
width = def_width
x = -0.66 # x-offset
y = 0
x_range = 3.3
frame_ratio = 4/3 

# iterations to test before concluding bound or unbound
precision = 500

height = round(width / frame_ratio)
y_range = x_range / frame_ratio
min_x = x - x_range / 2
max_x = x + x_range / 2
min_y = y - y_range / 2
max_y = y + y_range / 2

img = Image.new('RGB', (width, height), color = 'black')
pixels = img.load()

# could play with a log algorithm instead, which might be visually nicer
# probably a bit more computationally expensive - try it in C++ or lisp

def powerColor(dist, exp, const, scale):
    color = dist**exp
    rgb = colorsys.hsv_to_rgb(const + scale * color, 1 - 0.6 * color, 0.9)
    return tuple(round(i * 255) for i in rgb)

for row in range(height):
    for col in range(width):
        x = min_x + col * x_range / width
        y = max_y - row * y_range / height
        oldX = x
        oldY = y
        for i in range(precision + 1):
            a = x**2 - y**2 #real component of z^2
            b = 2*x*y #imaginary component of z^2
            x = a + oldX #real component of new z
            y = b + oldY #imaginary component of new z
            if x**2 + y**2 > 4:
                break
        if i < precision:
            distance = (i + 1) / (precision + 1)
            rgb = powerColor(distance, 0.2, 0.27, 1.0)
            pixels[col,row] = rgb
        index = row * width + col + 1
        print("{} / {}, {}%".format(index, width * height, round(index / width / height * 1000) / 10))

img.save('output.png')
os.system('xdg-open output.png')
