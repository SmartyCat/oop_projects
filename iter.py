import random 

class I:
    def __init__(self,count, dia):
        self.lst=[]
        self.count=count
        self.dia=dia

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst)!=self.count:
            x=random.randint(1,self.dia)
            self.lst.append(x)
            return x
        else:
            raise StopIteration

a=I(3,50)            
for i in a:
    print(i)