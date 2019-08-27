#..12345678910111213141516171820212223
import re
n=input()

def findRepeated(groups):
    for group in groups:
        for i in range(len(group)-1):
            if group[i]==group[i+1]:
                return group[i]
        return -1
                

def regex(n):
    pattern = re.compile(r'([^.*__+@#]+)')
    match = pattern.search(n)
    groups = match.groups()
    print(findRepeated(groups))

regex(n)
