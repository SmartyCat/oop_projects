from math import pi 

class Cylinder:
    @staticmethod
    def make_area(d,h):
        circle=pi*d**2/4
        side=pi*d*h
        return round(circle*2+side,2)
    def __init__(self,di,hi):
        self.di=di
        self.hi=hi
    def show_area(self):
        return  self.make_area(self.di,self.hi) 

a=Cylinder(1,2)
a.di=8
print(a.show_area())