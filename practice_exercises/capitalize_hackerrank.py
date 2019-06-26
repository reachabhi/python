def solve(s):
    x = list(map(lambda x : x.capitalize() , s.split(' ')))
    return ' '.join(x)

s = input()
print(solve(s))