rows=4
row=1
current=1

while row<rows:
    for i in range(row*2-1):
        print(current, end=" ")
        current+=1
    print()
    row+=1
    
        
     