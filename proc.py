from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    def process(x):
        raise TypeError("Eror")

    @process.register(int)
    @process.register(float)
    def int_float_proces(x):
        return x * 2

    @process.register(str)
    def str_proces(x):
        return x.upper()

    @process.register(list)
    def list_proces(x):
        return x[::-1]

    @process.register(tuple)
    def tuple_proces(x):
        x = sorted(x, reverse=True)
        return tuple(x)

print("xuy")