from functools import wraps
def shout(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		""" This is a wrapper function"""
		print(f'You are about to call {fn.__name__} method')
		print(f'Documnettaoin of the method is : {fn.__doc__} method')
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	"""Greets a person"""
	return f'Hi {name}, How r u ?'

print(greet('Todd'))

@shout
def order(name,pizza,side):
	""" Orders pizza """
	return f'Place an order of {pizza} and {side} for {name}'


print(order('Jack','Non veg pizza','breadsticks'))

#Now if we try to print name and doc of greet and order methods from outside you will get error since these metadatas are not preserved
print(greet.__doc__)
print(order.__name__) #It will print This is a wrapper function which is doc of wrapper() method inside shout()
#To preserve the metadata, we need to use @wraps decorator 


