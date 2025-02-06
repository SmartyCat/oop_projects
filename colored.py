class ColoredPoint:
    def __init__(self, x, y, color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-1 * self.x, -1 * self.y, self.color)

    def __invert__(self):
        result = []
        for i in self.color:
            result.append(255 - i)
        return ColoredPoint(self.y, self.x, tuple(result))


point = ColoredPoint(2, -3)
print(point)
print(-point)
print(~point)
