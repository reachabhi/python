
from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3 or len(kwargs) >= 3:
            return 'Too many arguments!'
        else:
            return fn(*args, **kwargs)
    
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"
