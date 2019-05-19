import sys

x = [1,2,4,5,6,7,8,9]

filter_even = list(filter(lambda y : y%2==0,x))

print(filter_even) #filters out even numbers

print(all(filter_even))

print(all(list(filter(lambda y : y%2==0,x))))

print(all(filter(lambda y : y%2==0,x))) #No need to create a list if we are just filtering , it unnecessary consumes memory by storing the list

#getsizeof() returns size in bytes

print(sys.getsizeof([x * 10 for x in range(5000)])) # Size is very huge since we are creating a list unnecessarily
print(sys.getsizeof(x * 10 for x in range(5000))) # Size of generator expression is much lesser


