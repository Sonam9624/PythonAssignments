
class Employee:
    _empid=None
    _empname=None
    _hra=None
    _da=None
    _pf=None
    _basesalary=None
    _gross=None
    
# assign value to data member
    def __init__(self,empid,empname,basesalary):
        self._empid=empid
        self._empname=empname
        self._basesalary=basesalary
        
    def calculate(self):
        self._hra=self._basesalary*0.40
        self._da=self._basesalary*0.20
        self._pf=self._basesalary*0.12
        self._gross=(self._basesalary+ self._hra+self._da)-self._pf
        
    def __str__(self):
        return f"Emp Id:{self._empid}, Name : {self._empname}, Gross of emp: {self._gross}"
    
class Manager(Employee):
    __food=None
    __ta=None
    def __init__(self,empid,empname,basesalary,food,ta):
        super().__init__(empid,empname,basesalary)
        self.__food=food
        self.__ta=ta
        
    def calculate(self):
        self._hra=self._basesalary*0.40
        self._da=self._basesalary*0.20
        self._pf=self._basesalary*0.12
        self._gross=(self._basesalary + self._hra + self._da +self.__food + self.__ta)-self._pf
        
    def __str__(self):
        return f"Emp Id: {self._empid}, Name : {self._empname}, Gross : {self._gross}"
    
m1=Manager(101,"Amol",45000,4500,9000)
m1.calculate()
print(m1)

e1=Employee(102,"Rohan",24500)
e1.calculate()
print(e1)

        
        
        