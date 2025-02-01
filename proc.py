from functools import singledispatchmethod


class Processor:

    @singledispatchmethod
    def process(self,x):
        raise TypeError("неподдерживаемый файл")

    @process.register(int)
    @process.register(float)
    def int_float_proces(self,x):
        return x * 2

    @process.register(str)
    def str_proces(self,x):
        return x.upper()

    @process.register(list)
    def list_proces(self,x):
        return x[::-1]

    @process.register(tuple)
    def tuple_proces(self,x):
        x = sorted(x, reverse=True)
        return tuple(x)
