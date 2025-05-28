

#\d -> for decimal numbers
#\s -> for space
#r -> raw string
# ^ -> start of pattern

import re

text= "Hello to all"
if re.match(r"^Hi", text):
    print("match found")
else:
    print("match not found")

print("----------------------------")


no= re.findall(r'\d+', 'my number is 12345 and alternate number is 6789')
print(no)


print("-----------------------")

#replace space with _

s1="Python is great programming"
result=re.sub(r'\s+','_',s1)
print(result)


print("------------------------")

# separated by , and ;
fruits=re.split(r'[,;]','orange,apple,banana')
print(fruits)
