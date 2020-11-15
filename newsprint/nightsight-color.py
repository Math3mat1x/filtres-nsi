from PIL import Image
import random


def draw(new, x, y, r_x, r_y, dots, color):
    available = list()
    for i in range(r_x):
        for j in range(r_y):
            available.append((i, j))

    for i in range(dots):
        p = random.choice(available)
        available.remove(p)
        p = (p[0]+x, p[1]+y)
        new.putpixel(p, color)

    return new

def blocks(image, x, y):
    w, h = image.size
    image_black = image.convert("L")
    r_x = w - (x+1)
    r_y = h - (y+1)
    r_x = 5 if r_x > 5 else r_x
    r_y = 5 if r_y > 5 else r_y

    block = list()
    block_black = list()
    for i in range(r_x):
        for j in range(r_y):
            color = image.getpixel((x+i, y+j))
            color_black = image_black.getpixel((x+i, y+j))

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

    return r_x, r_y, dots, color

def nightsight(image):
    image = image.convert("RGB")
    new = Image.new("RGB", image.size, 0)
    w, h = image.size

    for y in range(0, h, 5):
        for x in range(0, w, 5):
            r_x, r_y, dots, color = blocks(image, x, y)
            new = draw(new, x, y, r_x, r_y, dots, color)
    return new

if __name__ == "__main__":
    image = Image.open("lena.png")
    new = nightsight(image)
    new.save("test.png", "PNG")
