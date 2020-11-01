from PIL import Image, ImageDraw
import random

class Square():
    def __init__(self, image):
        self.colors = [(230, 57, 70), (241, 250, 238), (168, 218, 220),\
                       (69, 123, 157), (29, 53, 87)]
        self.borders = list()
        self._draw = ImageDraw.Draw(image)
        self.size = image.size

        # for _compute_borders
        self.up_to = lambda loc, t_bonsoir, lenght: loc + lenght \
                            if loc + lenght <= t_bonsoir else t_bonsoir

    def draw(self, xy, side):
        for x, y in self.borders:
            x1 = int(x.split("-")[0])
            x2 = int(x.split("-")[1])
            y1 = int(y.split("-")[0])
            y2 = int(y.split("-")[1])
            x = xy[0]
            y = xy[1]

            # partially right.
            x_collision  = (x <= x1 and x + side >= x1) or\
                           (x > x1 and x <= x2 and x + side >= x2)

            y_collision  = (y <= y1 and y + side >= y1) or\
                           (y > y1 and y <= y2 and y + side >= y2)

            if x_collision and y_collision:
                # do not draw the square then
                return None

        color = random.choice(self.colors)
        test = lambda  : random.randint(0,255)
        color = (test(), test(), test())

        self._draw.rectangle((xy, (xy[0] + side, xy[1] + side)), fill=color)

        self.borders.append(self._compute_borders(xy, side))
        # return this for further optimization?
        return self.borders

    def _compute_borders(self, xy, side):
        x, y = xy
        w, h = self.size
        border = f"{x}-{self.up_to(x, w, side-1)}",\
                 f"{y}-{self.up_to(y, h, side-1)}"
        return border


width, height = 1920,1080
image = Image.new("RGB", (width, height), (0, 0, 0))

test = Square(image)

rd = lambda limit : random.randint(0, limit)

# random tests
for i in range(1000):
    xy = rd(width), rd(height)
    side = rd(min(width, height))
    borders = test.draw(xy, side)

# xy = 0,0
# side = 10
# test.draw(xy, side)

# xy = 9,9
# side = 10
# test.draw(xy, side)

image.save("test.png", "PNG")
