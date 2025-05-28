
class Employee:
    __id=None
    __name=None
    __addr=None
    __salary=None
    
    def __init__(self,id,name,addr,salary):
        self.__id=id
        self.__name=name
        self.__addr=addr
        self.__salary=salary
        
    def display(self):
        print("id: ",self.__id)
        print("Name: ",self.__name)
        print("Address: ",self.__addr)
        print("Salary: ",self.__salary)
        print()
        
e1=Employee(101,"Neha","Pune",20000)
e1.display()

e2=Employee(102,"Sneha","Mumbai",40000)
e2.display()    
