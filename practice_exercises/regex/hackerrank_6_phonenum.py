#https://www.hackerrank.com/challenges/validating-the-phone-number/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
phoneList = [input() for _ in range(n)]
pattern = re.compile(r'(^[789][0-9]{9}$)')
for i in phoneList:
    match = pattern.search(i)
    if match:
        print('YES')
    else:
        print('NO')