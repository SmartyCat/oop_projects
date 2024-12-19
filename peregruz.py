class Snow:
    def __init__(self, n):
        self.count = n

    def __add__(self, number):
        return self.count + number

    def __sub__(self, number):
        return self.count - number

    def __mul__(self, number):
        return self.count * number

    def __truediv__(self, number):
        return round(self.count, number)

    def make_snow(self, num):
        check = self.count
        s = ""
        while True:
            check -= num
            s += "*" * num + "/"
            if check < num:
                if check > 0:
                    s += "*" * check
                    break
                else:
                    s = s[: len(s) - 1]
                    break

        return s

    def __call__(self, item):
        self.count = item
