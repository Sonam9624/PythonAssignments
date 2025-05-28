
a=int(input("Enter a number"))
b=int(input("Enter a number"))

l1=[1,2,3,4,5]
try:
    c=a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
    
else:
        print("Division is :",c)
        
try:
    print(l1[10])
except IndexError as e:
    print(e)
    
print("value of a is: ",a)
print("value of b is: ",b)


        