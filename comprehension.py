
l1=[56,67,45,89,23,12]

res=[i**3 for i in l1]
print(res)

print("-------------------------")

#Print odd number from list

result=[i for i in l1 if i%2!=0]
print("Odd no are:" , result)

print("------------------------------")

result=[i for i in l1 if i%2==0]
print("Even nos are:", result)

print("------------------------------")

#labels=['even' if n%2==0 else 'odd' for n in range(l1)]
#print(labels)

print("------------------------------")

l2=[5,-2,8,-8]

# replace -ve value with 0
result=[n if n>0 else 0 for n in l2]
print(result)

print("------------------------------")

#lambda & map & filter
#map is used to iterate each element n manipulate
#filter is used to extract some value depending on conditions

nos=[1,2,3,4,5]
sq=list(map(lambda x:x**2, nos))
print(sq)

even=list(filter(lambda x:x%2==0, nos))
odd= list(filter(lambda x:x%2!=0, nos))
print(even)
print(odd)





