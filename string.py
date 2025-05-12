
s1="Hello my age is 25 my id is abc@gmail.com"

#chars, numbers, special symbols, space  isalpha() isdigit() isspace()

char_count=0
num_count=0
symbol_count=0
space_count=0

for s in s1:
    if s.isalpha():
        char_count+=1
    elif s.isdigit():
        num_count+=1
    elif s.isspace():
        space_count+=1
    else:
        symbol_count+=1
        
print("chars count: ", char_count)
print("number count: ",num_count)
print("space count: ", space_count)
print("symbol count: ",symbol_count)