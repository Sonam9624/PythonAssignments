
class Student:
    #data members
    __name:None
    __rollno=None
    __eng=None
    __sci=None
    __maths=None
    __total=None
    __percentage=None
    
    #self will point to data members self.rollno
    #rollno will be a local variable
    
    def accept(self,rollno,name,eng,sci,maths):
        self.__rollno=rollno
        self.__name=name
        self.__eng=eng
        self.__maths=maths
        self.__sci=sci
        
    def calculate(self):
          self.__total=self.__eng+self.__sci+self.__maths
          self.__percentage=self.__total/3
        
    def display(self):
        print(self.__rollno, self.__name, self.__eng, self.__sci, self.__maths, "Total is:" ,self.__total, 
              "Percentage is: ", self.__percentage)
        
#create object of class
stud1=Student()  # first object
stud1.accept(1,'Amol',48,75,89)
stud1.calculate()
stud1.display()

stud2=Student()   #second object
stud2.accept(2,'Seema', 84,86,98)
stud2.calculate()
stud2.display()




# __ private data member


    