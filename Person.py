class Person:
    def __init__(self,name,surname):
        if self.check(name) and self.check(surname):
            self.__name=name.title()
            self.__surname=surname.title()
        else:
            raise ValueError("Некорректные данные")
    
    @staticmethod
    def check(x):
        if isinstance(x,str) and x.isalpha():
            return True
        else:
            return False
    
    @property
    def fullname(self):
        return self.__name+" "+self.__surname
    
    @fullname.setter
    def fullname(self,info):
        n,s=info.split()
        if self.check(n) and self.check(s):
            self.__name=n.title()
            self.__surname=s.title()
        else:
            raise ValueError("Некорректные данные")
        
p=Person("misha","maly")
print(p.fullname)
p.fullname="stas Taran"
print(p.fullname)
