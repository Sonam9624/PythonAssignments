# Function with parameters

def addition(a,b):
    c=a+b
    return c

def substraction(a,b):
    c=a-b
    return c

def multiplication(a,b):
    c=a*b
    return c

def division(a,b):
    c=a/b
    return c

def modulus(a,b):
    c=a%b
    return c



x=int(input("Enter a number: "))
y=int(input("Enter second number: "))

sum=addition(x,y)
print("Addition is: ",sum)

sub=substraction(x,y)
print("substraction is: ",sub)

mul=multiplication(x,y)
print("multiplication is: ",mul)

div=division(x,y)
print("division is: ",div)

mod=modulus(x,y)
print("modulus is: ",mod)