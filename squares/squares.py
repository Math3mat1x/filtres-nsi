from PIL import Image
import random


palette_colors = [(230, 57, 70), (241, 250, 238), (168, 218, 220),\
                  (69, 123, 157), (29, 53, 87)]

width, height = 1600, 1200

im = Image.new("RGB", (width, height), (0, 0, 0))

def draw_square(start_x, start_y, side_lenght, color):
    up_to = lambda pos, lenght, limit : pos + lenght + 1 \
                   if pos + lenght <= limit else limit + 1

    for x in range(up_to(start_x, width, side_lenght)):
        for y in range(up_to(start_y, height, side_lenght)):
            im.putpixel((x,y), color)


rd = lambda limit : random.randint(1, limit)

i, j = rd(width), rd(height)
square = rd(min(width, height))
color = random.choice(palette_colors)

draw_square(i, j, square, color)

im.save("square.png", "PNG")
