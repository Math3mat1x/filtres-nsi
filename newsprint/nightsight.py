from PIL import Image
import random

def draw(new, x, y, r_x, r_y, black_dots):
    available = list()
    for i in range(r_x):
        for j in range(r_y):
            available.append((i, j))

    for i in range(black_dots):
        p = random.choice(available)
        available.remove(p)
        p = (p[0]+x, p[1]+y)
        new.putpixel(p, 128)

    return new

def blocks(image, x, y):
    w, h = image.size

    r_x = w - (x+1)
    r_y = h - (y+1)
    r_x = 5 if r_x > 5 else r_x
    r_y = 5 if r_y > 5 else r_y

    block = list()
    for i in range(r_x):
        for j in range(r_y):
            color = image.getpixel((x+i, y+j))
            block.append(color)

    if len(block) == 0:
        average = 0
    else:
        average = sum(block) / len(block)

    black_dots = round(average * r_x * r_y / 256)

    return r_x, r_y, black_dots

def nightsight(image):
    image = image.convert("L")
    new = Image.new("L", image.size, 0)
    w, h = image.size

    for y in range(0, h, 5):
        for x in range(0, w, 5):
            r_x, r_y, black_dots = blocks(image, x, y)
            new = draw(new, x, y, r_x, r_y, black_dots)

    return new

# Test
if __name__ == "__main__":
    image = Image.open("lena.png")
    new = nightsight(image)

    new.save("lena-test.png", "PNG")
