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
        # TODO: check if we can draw first
        color = random.choice(self.colors)
        self._draw.rectangle((xy, (xy[0] + side, xy[1] + side)), fill=color)

        self.borders.append(self._compute_borders(xy, side))
        return self.borders

    def _compute_borders(self, xy, side):
        x, y = xy
        w, h = self.size
        border = f"{x}-{self.up_to(x, w, side-1)}",\
                 f"{y}-{self.up_to(y, h, side-1)}"
        return border


width, height = 100, 100
image = Image.new("RGB", (width, height), (0, 0, 0))

test = Square(image)
borders = test.draw((0,0),70)
print(borders)

image.save("test.png", "PNG")
