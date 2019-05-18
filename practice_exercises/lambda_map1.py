x = [1, 2, 3, 4]

print(list(map(lambda y: y**2 , x)))

def square(y): return y**2

print(tuple(map(square, x))) 

z = set(map(square, (9,8,4)))
print(z)

square = map(lambda i: i**2, x)
print(square) #map object
print(list(square)) #[1, 4, 9, 16]
print(list(square)) # [] map objects can only be iterated once, we need to assign again to print the result like below

square = map(lambda i: i**2, x)
print(square) #map object
print(list(square)) #[1, 4, 9, 16]
