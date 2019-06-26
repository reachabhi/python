#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fun(l):
        # complete the function
        newargs = list(map(lambda x: '+91 ' + str(x)[-10:-5] + ' ' + str(x)[-5:], l))
        return f(newargs)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 