
class Book:
    __id=None
    __name=None
    __author=None
    __price=None
    
    #Setters to assign value -code
    def setId(self,id):
        self.__id=id
        
    def setName(self,name):
        self.__name=name
        
    def setAuthor(self,author):
        self.__author=author
        
    def setPrice(self,price):
        self.__price=price
        
    #Getters to read a value -code
    def getId(self):
        return self.__id
   
    def getName(self):
        return self.__name
    
    def getAuthor(self):
        return self.__author
    def getPrice(self):
        return self.__price
    
b1=Book()
b1.setId(101)
b1.setName("Neha")
b1.setAuthor("Abc")
b1.price=(320)

b2=Book()
b2.setId(201)
b2.setName("Priya")
b2.setAuthor("Xyz")
b2.setPrice(650)

print(b1.getId(),b1.getName(), b1.getAuthor(),b1.getPrice())
print(b2.getId(),b2.getName(),b2.getAuthor(),b2.getPrice())
