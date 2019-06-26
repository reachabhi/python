from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any(item for item in args if type(item)!=int):
        	return "Please only invoke with integers."
        else:
        	return fn(*args, **kwargs)
            
    
    return wrapper

@only_ints
def add(x,y):
	return x+y

print(add(1,2))
print(add("1","2"))
