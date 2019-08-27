#https://www.hackerrank.com/challenges/introduction-to-regex/problem
#Detect Floating Point Number
'''
Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff
------------------
Sample Output 0

False
True
True
False


'''
import re

n = int(input())
item = [input() for _ in range(n)]

def match(item):
    pattern = re.compile(r'^[+-]?\d*(\.\d+)$')
    match = [pattern.findall(i) for i in item]
    result = ['True' if i!=[] else 'False' for i in match]
    for i in result:
        print(i)

match(item)