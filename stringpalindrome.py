# string is palindrome or not

str1=input("Enter a string: ")

if str1==str1[::-1]:                 #negative index
    print(str1, "is palindrome")
else:
    print(str1, "is not a palindrome")