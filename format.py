from functools import singledispatchmethod

class Fromatter:

    @singledispatchmethod
    def format(x):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int) 
    @format.register(float)
    def format_float(x):
        if isinstance(x,float):
            return f"Вещественное число: {x}"
        else:
            return f"Целое число: {x}"

    @format.register(dict)
    @format.register(list)
    @format.register(tuple)
    def format_tuple(x):
        if isinstance(x,tuple):
            result="Элементы кортежа: "

        elif isinstance(x,dict):
            result = "Пары словаря: "
            x=sorted(x.items())
            "Пары словаря: "
        else:
            result="Элементы списка: "

        for i in range(len(x)):
            if i==len(x)-1:
                result+=str(x[i])
            else:
                result+=str(x[i])+", "
        return result

