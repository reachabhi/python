#purpose is ot ensure if all the arguments passed are of the type passed to the decorator , if not convert them instead
from functools import wraps

def enforce(*types): #types will take all type args as passed to @enforce decorator
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			newargs = []
			for (a,t) in zip(args, types):
				newargs.append(t(a)) #str(Hello), int('3')
			return fn(*newargs, **kwargs)
		return wrapper
	return inner

@enforce(str,int)
def repeat_msg(msg, times):
	for i in range(times):
		print(msg)

@enforce(float,float) #enforces the args passed t be floats
def divide(x, y):
	print(x/y)

repeat_msg('Hello',3) 
repeat_msg(3,'4') #If we remove the decorator it will throw error

divide('3', '4')
