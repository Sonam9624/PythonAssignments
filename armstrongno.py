
num=int(input("Enter a number: "))
sum=0
x=num
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10
    
if x==sum:
    print(x, "is an armstrong  number")
else:
    print(x, "is not an armstrong number")

