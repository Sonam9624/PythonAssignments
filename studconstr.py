
class Product:
    __code=None
    __name=None
    __price=None
    
    # constructor / initializer
    def __init__(self,code,name,price):
        self.__code=code
        self.__name=name
        self.__price=price
        
    def __str__(self):
        return f'code ={self.__code}, Name={self.__name} Price={self.__price}'
        
    
p1=Product(101,"Pen",50)
print(p1)

p2=Product(102,"Keyboard",999)
print(p2)
