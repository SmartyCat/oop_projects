class HourClock:
    def __init__(self, hours):
        if self.check(hours):
            self.__hours = hours
        else:
            raise ValueError("Некорректное время")

    @staticmethod
    def check(x):
        if isinstance(x, int) and 1 <= x <= 12:
            return True
        else:
            return False

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, h):
        if self.check(h):
            self.__hours = h
        else:
            raise ValueError("Некоректное время")
