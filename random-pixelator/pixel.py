from PIL import Image
import random

im = Image.open("image.png")

w, h = im.size

def average_block_color(start_x, start_y):
    blocks = list()

    for y in range(block_size):
        if y > 0:
            blocks.append(block)
        block = list()

        for x in range(block_size):
            block.append(im.getpixel((start_x+x-(block_size - w % block_size),\
                        start_y+x-(block_size - h % block_size))))
    color = [[], [], []]
    color_depth = len(blocks[0][0])

    for block in blocks:
        for i in range(block_size):
            for j in range(color_depth):
                color[j].append(block[i][j])

    color = tuple([round(sum(i)/len(i)) for i in color])

    return color

def draw(x, y, color):
    for i in range(block_size):
        for j in range(block_size):
            if i + x <= w and j + y <= h:
                try:
                    im.putpixel((i+x-(block_size - w % block_size),\
                        j+y-(block_size - h % block_size)), color)
                except: # if it doesn't work
                    im.putpixel((i+x-1, j+y-1), color)

# main loop
block_size = int(input("Block size: "))
if block_size ==  1: block_size = 2
percentage_coverage = int(input("Percentage coverage: ")) / 100

how_many = [int(w / block_size), int(h / block_size)]
percentage = 1 / (int(w * h / (block_size ** 2)) + 1) # square's percentage

to_draw = list()

available = {l*block_size:[i*block_size for i in range(how_many[1] + 1)]\
            for l in range(how_many[0] + 1)}

for i in range(round(percentage_coverage / percentage)):
    while True:
        x = random.randint(0, how_many[0]) * block_size
        y = random.choice(available[x])

        if y:
            available[x].remove(y)
            to_draw.append((x,y))
            break

for x, y in to_draw:
    color = average_block_color(x, y)
    draw(x, y, color)

im.save("test.png", "PNG")
