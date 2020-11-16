from PIL import Image
import random


def draw(new, x, y, r_x, r_y, dots, color):
    """
    Draw black dots on the selected area.
    Args:
        new: the final image
        x, y: start coordinates of the area/block
        r_x, r_y: maximum width and height in pixels for the block
        dots: number of colored dots needed in the area
        color: average color of the block
    Returns:
        new: updated image
    """

    color = tuple([round(i/5) for i in color]) # the cloors are dimmed

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
    """
    Determine the dimensions of a block.
    Args:
        Image: PIL object of the image
        x, y: start coordinates of the block
    Returns:
        r_x, r_y: maximum width and height of the block
        dots: number of colored dots that need to be on the area.
        color: color of the dots
    """

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

    # get the average of each color
    if len(block) > 0:
        r = round(sum([i[0] for i in block]) / len(block))
        g = round(sum([i[1] for i in block]) / len(block))
        b = round(sum([i[2] for i in block]) / len(block))
        color = (r, g, b)
    else:
        color = (0, 0, 0)

    if len(block) == 0:
        average = 0
    else:
        average = sum(block_black) / len(block_black)

    dots = round(average * r_x * r_y / 256)

    return r_x, r_y, dots, color

def nightsight_color(image):
    """
    Main function for the nightsight filter.
    Args:
        image: PIL object of the image
    Retuns:
        new: image processed through the filter
    """

    # make sure the image is RGB
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
    new = nightsight_color(image)
    new.save("test.png", "PNG")
