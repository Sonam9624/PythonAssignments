# WAP to find sum of all even numbers between 1 to n.

n=int(input("Enter range of number : "))

x=1
sum=0
while x<=n:
    if x%2==0:
        sum=sum+x
        print(x, "is even")
    x+=1
print("Addition of even numbers is:", sum)


