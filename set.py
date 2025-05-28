# create an empty set in python

s1= set()

print(type(s1))

s2={1,2,3,4,5}
print(type(s2))

print(s2)

s3={100,200}

l1=[10,20,30]
s2.add(60)
s2.add(7)
print(s2)

s2.update(l1,s3)


# discard
# check if element is present then remove if not present
# then ignore
#s2.discard(9)

# removes the element if present, else show error message when 
# element not present

s2.remove(9)

s2.clear()
print(s2)

print("----------------------------------------")

# iterate the set using loop

for i in s2:
    print(i)
    
print("----------------------------------------")

# i want to remove duplicates from list

l1=[1,2,3,54,22,3,1,54,2,45,78,23,78,23,2,6,4]


s1=set(l1) # load the list in the set

print(s1)

print(len(s1))
print(max(s1))
print(min(s1))
print(sum(s1))

l2=list(s1) # conversion from set to list
print(l2)

l3=sorted(s1,reverse=True) # sort the collection returns the list
print(l3)

print("----------------------------------------")

# union, intersection, difference, symmetric_difference

s1={1,2,3,5}
s2={3,4,5,2}

s3=s1.union(s2)
print(s3)

print("----------------------------------------")

s3=s1.intersection(s2)
print(s3)

print("----------------------------------------")


s3=s1.difference(s2)


# unique from both the sets
s3=s1.symmetric_difference(s2)
print(s3)


# issubset()  , issuperset()

s1={1,2,7,3,4}
s2={1,2,3,4}

# if all elements from s1 are present in s2 return True else False
print(s1.issubset(s2))

# if all elements from s2 are preset in s1 returns True else False
print(s1.issuperset(s2))
