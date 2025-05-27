
l1=[10,20,30,40,20]

print(l1)

# Append
l1.append(60)
print(l1)
print("----------------------")


# index,value  Insert
l1.insert(2,5)
print(l1)
print("--------------------")


# remove based on index
l1.pop(2)
print(l1)
print("--------------------")

# remove using element
l1.remove(40)
print(l1)
print("--------------------")



# Frequency of element
print("freq", l1.count(10))


#  value, index(start search from given index)
# index is optional , if not provided then returns the
# first match element index
print(l1.index(20,2))


l2=[78,45,99,234,786,231,7,14,89]
l2.sort()
l2.reverse()
print(l2)

print("--------------------")


l2.sort(reverse=True)


# Common functions with collections

print("length: ",len(l2))
print("Max: ", max(l2))
print("Min: ", min(l2))
print("sum: ", sum(l2))





l1=[]   # empty list

l1.append(10)
l1.append(20)

print(l1)










