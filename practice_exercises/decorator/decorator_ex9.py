'''
should print the message "Waiting 3s before running say_hi" to the console
should then wait 3 seconds
finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(time):
    def inner(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(time,f.__name__))
            sleep(time)
            return f(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

say_hi()
