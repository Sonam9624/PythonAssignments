
sq=lambda a:a*a
print(sq(4))

add=lambda a,b: a+b
print(add(5,7))

maximum= lambda a,b: a if a>b else b
print(maximum(54,78))

iseven= lambda x: x%2==0
print(iseven(5))

cube=lambda a: a**3
print(cube(6))


# Immediate call to lambda expression

print((lambda x:x*2)(4))
