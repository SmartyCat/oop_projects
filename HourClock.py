class HourClock:
    def __init__(self,hours):
        if isinstance(hours,int) and 0<hours<13:
            self.__hours=hours
        else:
            raise ValueError("Некорректное время")
    
    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self,h):
        self.__hours=h

