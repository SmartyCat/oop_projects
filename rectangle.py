class Rectanle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def primeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

rect=Rectanle(5,5)
print(rect.area())
print(rect.primeter())
print(rect.is_square())