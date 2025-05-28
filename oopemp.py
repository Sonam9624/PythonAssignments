
class Employee:
    name:None
    id:None
    salary:None
    hra:None
    da:None
    pf:None
    
    def accept(self, name,id,salary,hra,da,pf):
        self.name=name
        self.id=id
        self.salary=salary
        self.hra=hra
        self.da=da
        self.pf=pf      
        
    def display(self):
            print(self.name,' ', self.id, '',self.salary,'', self.hra,'', self.da,'', self.pf)
            
            
emp1=Employee()
emp1.accept('Neha', 1, 50000, 520, 620, 2000)
emp1.display()


emp2=Employee()
emp2.accept('John',2, 60000,540,680,950)
emp2.display()
