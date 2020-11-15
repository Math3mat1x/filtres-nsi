from PIL import Image
import random

b_s = 5 # block size

bg = 0
c = 128

im = Image.open("lena.png")
im = im.convert("L")

new = Image.new("L", im.size, bg)
w, h = im.size

colors = list()

def draw(x, y, r_x, r_y, black_dots):
    available = list()
    for i in range(r_x):
        for j in range(r_y):
            available.append((i, j))

    print(black_dots)
    for i in range(black_dots):
        p = random.choice(available)
        available.remove(p)
        p = (p[0]+x, p[1]+y)
        new.putpixel(p, c)

def blocks(x, y):
    r_x = w - (x+1)
    r_y = h - (y+1)
    r_x = b_s if r_x > b_s else r_x
    r_y = b_s if r_y > b_s else r_y

    block = list()
    for i in range(r_x):
        for j in range(r_y):
            color = im.getpixel((x+i, y+j))
            block.append(color)

    try:
        average = sum(block) / len(block)
    except ZeroDivisionError:
        average = 0

    black_dots = round(average * r_x * r_y / 256)
    # compare = black_dots * 256 / (r_x * r_y)
    # print(average, black_dots)
    # input()

    draw(x, y, r_x, r_y, black_dots)
    return black_dots



for y in range(0, h, b_s):
    for x in range(0, w, b_s):
        blocks(x, y)


new.save("lena-nightsight.png", "PNG")
