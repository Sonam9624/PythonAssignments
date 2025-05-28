
class Product:
    __code=None
    __name=None
    __price=None
    
#Constructor/initializer

    def __init__(self,code,name,price):
        self.__code=code
        self.__name=name
        self.__price=price
        
    def display(self):
        print(self.__code)
        print(self.__name)
        print(self.__price)
        print()
        
        
p1=Product(1,"Neha",5000)
p1.display()

p2=Product(2,"sneha",6000)
p2.display()        