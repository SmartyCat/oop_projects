class Rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width

    def get_area(self):
        return self.__length*self.__width
    def get_perimetr(self):
        return 2*(self.__length+self.__width)
    
    perimeter=property(get_perimetr)
    area=property(get_area)

