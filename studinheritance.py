
class Student:
    _id=None
    _name=None
    _maths=None
    _science=None
    _total=None

    def __init__(self,id,name,maths,science):
        self._id=id
        self._name=name
        self._maths=maths
        self._science=science
        
    def calculate(self):
        self._total=self._maths + self._science
        
    def __str__(self):
        return f"id: {self._id}, Name: {self._name}, total: {self._total}"
    
class EnggStudent(Student):
    __sub1=None
    __sub2=None
    __sub3=None
    __sub4=None
    __percentage=None
    
    def __init__(self,id,name,maths,science,sub1,sub2,sub3,sub4):
        super().__init__(id,name,maths,science)
        self.__sub1=sub1
        self.__sub2=sub2
        self.__sub3=sub3
        self.__sub4=sub4
        
    def calculate(self):
        self.__percentage=(self.__sub1 + self.__sub2 + self.__sub3 + self.__sub4)/4
        
    def __str__(self):
        return f"Sub1: {self.__sub1}, Sub2: {self.__sub2}, Sub3: {self.__sub3}, Sub4: {self.__sub4}, Percentage: {self.__percentage}"

s1=Student(101, "Neha", 92, 85)
s1.calculate()
print(s1)

e1=EnggStudent(102, "Sneha", 89, 85, 42, 69, 75, 85)
e1.calculate()
print(e1)
        
        
    