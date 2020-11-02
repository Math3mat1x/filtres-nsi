from PIL import Image, ImageDraw
import random

# TODO:
# - use big squares when possible, maybe pick a minimum value for the size
#   of the sides of a square after doing some math knowing the width and
#   the height of the image and the number of squares that have to be in it?
# - determine a range of numbers to pick random values other than just the height
#   and the width of the image to make the code run faster for large values
# - make it a filter by making an effect of transparency wih the background

# Hints:
# - Rules are simple: choose a position, draw a square half as big as \
#   possible without colliding another square.
# - Optimize the algorithm with k-d tree

class Square():
    def __init__(self, image):
        self.colors = [(230, 57, 70), (241, 250, 238), (168, 218, 220),\
                       (69, 123, 157), (29, 53, 87)]
        self.borders = list()
        self._draw = ImageDraw.Draw(image)
        self.size = image.size

        # for _compute_borders
        self.up_to = lambda loc, t_dim, lenght: loc + lenght \
                            if loc + lenght <= t_dim else t_dim

        self.count = int() # number of drawn squares

    def check(self, xy, side):
        for x, y in self.borders:
            try:
                x1 = int(x.split("-")[0])
                x2 = int(x.split("-")[1])
                y1 = int(y.split("-")[0])
                y2 = int(y.split("-")[1])
                x = xy[0]
                y = xy[1]
            except:
                continue

            not_x_collision = False
            if x < x1 and x + side < x1:
                not_x_collision = True
            elif x > x1 and x < x2 and x + side < x2:
                not_x_collision = True
            elif x > x2:
                not_x_collision = True

            not_y_collision = False
            if y < y1 and y + side < y1:
                not_y_collision = True
            elif y > y1 and y < y2 and y + side < y2:
                not_y_collision = True
            elif y > y2:
                not_y_collision = True

            if not (not_x_collision and not_y_collision):
                return False

        return True

    def draw(self, xy, side):

        if not self.check(xy, side):
            return None

        self.count += 1
        # color = random.choice(self.colors)
        # Generate a truly random color instead of picking in the palette
        color = lambda : (random.randint(0, 255), random.randint(0, 255),\
                         random.randint(0, 255))

        self._draw.rectangle((xy, (xy[0] + side, xy[1] + side)), fill=color())

        self._compute_borders(xy, side)
        return self.borders

    def _compute_borders(self, xy, side):
        x, y = xy
        w, h = self.size
        border = f"{x}-{self.up_to(x, w, side-1)}",\
                 f"{y}-{self.up_to(y, h, side-1)}"

        self.borders.append(border)

width, height = 1920,1080
image = Image.new("RGB", (width, height), (0, 0, 0))

test = Square(image)

rd = lambda limit : random.randint(0, limit)

# random tests
to_reach = 50 # number of squares required in the final image
while test.count <= to_reach:
    print(str(round(test.count / to_reach * 100, 2)) + " %") # status
    xy = rd(width), rd(height)
    side = rd(min(width, height))
    borders = test.draw(xy, side) # kinda useless now to capture borders

image.save("test.png", "PNG")
