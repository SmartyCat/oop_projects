class QauadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, x):
        return cls(x[0], x[1], x[2])

    @classmethod
    def from_str(cls, s):
        s = s.split()
        s = list(map(lambda x: float(x), s))
        return cls(s[0], s[1], s[2])
