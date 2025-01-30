

class Account:
    def __init__(self,login,password):
        self.__login=login
        self.__password=self.hash_function(password)

    @staticmethod
    def hash_function(password):
        hash_value=0
        for char,index in zip(password,range(len(password))):
            hash_value+=ord(char)*index
        return hash_value % 10**9
    
    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,new_password):
        self.__password=self.hash_function(new_password)
    
a=Account("misha","1234")
