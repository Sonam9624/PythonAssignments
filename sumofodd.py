
#Write a Python program to find sum of all odd numbers between 1 to n.

n=int(input("Enter the range of number: "))

x=1
sum=0

while x<=n:
    if x%2!=0:
        sum=sum+x
        print(x, "is odd number")
    x+=1
print("Addition of all odd numbers is: ", sum)