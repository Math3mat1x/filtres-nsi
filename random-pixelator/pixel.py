from PIL import Image

im = Image.open("image.png")

w, h = im.size

block_size = 3

blocks = list()
x_current, y_current = -1, -1

blocks.append([list() for i in range(block_size)])

current_block = list()

for y in range(block_size):
    y_current += 1
    x_block = list()
    if y >= 0:
        current_block.append(x_block)
    for x in range(block_size):
        x_current += 1
        if w >= x_current + 1 or h >= y_current + 1:
            x_block.append(im.getpixel((x_current, y_current)))
        else:
            x_block.append((0,0,0))

print(current_block[0])
