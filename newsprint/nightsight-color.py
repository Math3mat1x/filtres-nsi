from PIL import Image
import random

b_s = 5 # block size

bg = 0
c = 128

im = Image.open("lena.png")
im = im.convert("RGB")
im_black = im.convert("L")

new = Image.new("RGB", im.size, bg)
w, h = im.size

colors = list()

def draw(x, y, r_x, r_y, dots, color):
    available = list()
    for i in range(r_x):
        for j in range(r_y):
            available.append((i, j))

    for i in range(dots):
        p = random.choice(available)
        available.remove(p)
        p = (p[0]+x, p[1]+y)
        new.putpixel(p, color)

def blocks(x, y):
    r_x = w - (x+1)
    r_y = h - (y+1)
    r_x = b_s if r_x > b_s else r_x
    r_y = b_s if r_y > b_s else r_y

    block = list()
    block_black = list()
    for i in range(r_x):
        for j in range(r_y):
            color = im.getpixel((x+i, y+j))
            color_black = im_black.getpixel((x+i, y+j))

            block.append(color)
            block_black.append(color_black)

    r = round(sum([i[0] for i in block]) / len(block))
    g = round(sum([i[1] for i in block]) / len(block))
    b = round(sum([i[2] for i in block]) / len(block))

    color = (r, g, b)
    if len(block) == 0:
        average = 0
    else:
        average = sum(block_black) / len(block_black)

    dots = round(average * r_x * r_y / 256)

    draw(x, y, r_x, r_y, dots, color)
    return dots



for y in range(0, h, b_s):
    for x in range(0, w, b_s):
        blocks(x, y)


new.save("lena-nightsight.png", "PNG")
