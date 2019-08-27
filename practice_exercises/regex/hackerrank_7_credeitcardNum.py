'''https://www.hackerrank.com/challenges/validating-credit-card-number/problem'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
ccnums = [input() for _ in range(n)] 
matched_ccnums = []
pattern = re.compile(r'^[465]\d{3}-?\d{4}-?\d{4}-?\d{4}$')
for i in ccnums:
    match = pattern.search(i)
    if match:
        matched_ccnums.append(match.group())
    else:
        matched_ccnums.append('None')
#below logic makes sure there are no 4 consecutive digits
for i in matched_ccnums:
    if '-' in i:
        i = ''.join(i.split('-'))
    s=set(i)
    if any([n*4 in i for n in s]) or i=='None': #like 51-67-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times
        print("Invalid")
    else:
        print("Valid")