from functools import singledispatchmethod


class Negator:

    @singledispatchmethod
    def neg(x):
        print("Базовая функция")

    @neg.register(int)
    @neg.register(float)
    def neg(x):
        if not isinstance(x, bool) and type(x) in (int, float):
            return -1 * x
        elif isinstance(x, bool):
            return True if x == False else False
        raise TypeError("Аргумент данных не поддерживается")


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(False))
print(Negator.neg(True))
