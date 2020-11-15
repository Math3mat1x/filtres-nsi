from PIL import Image
import random


def average_block_color(image, start_x, start_y, block_size):
    w, h = image.size
    blocks = list()

    for y in range(block_size):
        if y > 0:
            blocks.append(block)
        block = list()

        for x in range(block_size):
            block.append(image.getpixel((start_x+x-(block_size - w % block_size),\
                        start_y+x-(block_size - h % block_size))))

    color = [[], [], []]
    color_depth = len(blocks[0][0])

    for block in blocks:
        for i in range(block_size):
            for j in range(color_depth):
                color[j].append(block[i][j])

    color = tuple([round(sum(i)/len(i)) for i in color])

    return color

def draw(image, x, y, color, block_size):
    w, h = image.size

    for i in range(block_size):
        for j in range(block_size):
            if i + x <= w and j + y <= h:
                image.putpixel((i+x-(block_size - w % block_size), j+y-(block_size\
                        - h % block_size)), color)
    return image

def random_pixelisator(image, block_size, percentage_coverage):
    w, h = image.size

    block_size = int(block_size)
    if block_size == 1: block_size = 2
    percentage_coverage = int(percentage_coverage) / 100

    how_many = [int(w / block_size), int(h / block_size)] # on many squares available
    percentage = 1 / (int(w * h / (block_size ** 2)) + 1) # percentage of the total coverage of a square area

    to_draw = list()

    available = {l*block_size:[i*block_size for i in range(how_many[1] + 1)]\
                for l in range(how_many[0] + 1)}

    for _ in range(round(percentage_coverage / percentage)):
        while True:
            x = random.randint(0, how_many[0]) * block_size
            y = random.choice(available[x])

            if y:
                available[x].remove(y)
                to_draw.append((x, y))
                break

    for x, y in to_draw:
        color = average_block_color(image, x, y, block_size)
        image = draw(image, x, y, color, block_size)

    return image

if __name__ == "__main__":
    image = Image.open("trou_noir.png")
    image = random_pixelisator(image, 10, 50)
    image.save("test.png", "PNG")
