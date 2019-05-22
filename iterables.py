name = 'Abhi'
#next(name) #throws error as name is not iterable

it = iter(name) #it makes name iterable and returns and assigns a iterator object to it

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#Keep printing till it throws StopIteration Error
