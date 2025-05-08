# create simple addition function to accept 2 number & display sum

def addition():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a+b
    print("Addition is: ", c)
    
def substraction():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a-b
    print("Substraction is: ", c)
    
def multiplication():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a*b
    print("Multiplication is: ", c)
    
def division():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a/b
    print("Division is: ", c)
    
def modulus():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a%b
    print("Modulus is: ", c)
    
    
    
# execute/call

addition()
substraction()
multiplication()
division()
modulus()
