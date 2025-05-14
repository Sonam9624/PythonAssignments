# Program to remove repeated characters from string

string="geeks for geeks"
c=""

for char in string:
     if char not in c:
        c = c + char
        
print(c)

