def var_args(*args):
	print(args)

var_args(12,34,56,'fdfdf',99.44) #returns a tuple

def var_kwargs(**kwargs):
	print(kwargs)
	print(kwargs.items())
	print(kwargs.keys())
	print(kwargs.values())
 
var_kwargs(name='Jack', sex='male', age=98, type='employee') #returns a dictionary with key value pairs as mentioned in the argument
