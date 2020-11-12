from PIL import Image

im = Image.open("image.png")

w, h = im.size

block_size = 3 # TODO: other values don't work...

def average_block_color(start_x, start_y):
    blocks = list()
    for y in range(block_size):
        if y > 0:
            blocks.append(block)
        block = list()
        for x in range(block_size):
            if w >= start_x + x + 1 or h >= start_y + y + 1:
                block.append(im.getpixel((start_x+x-1, start_y+y-1)))
            else:
                block.append((0, 0, 0))

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
                    im.putpixel((i+x-1, j+y-1), color)
                except:
                    print(i+x, j+y)
                    input()

# main loop
for x in range(-1, w, block_size):
    for y in range(-1, h, block_size):
        # print(x,y)
        color = average_block_color(x, y)
        draw(x, y, color)

print(im.size)
im.save("test.png", "PNG")
