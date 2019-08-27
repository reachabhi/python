#rabcdeefgyYhFjkIoomnpOeorteeeeet
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re
n = input()
for i in range(len(n)):
    if n[i] not in 'aeiouAEIOU':
        n = n[i:]
        break
for i in range(len(n)):
    if n[len(n)-i-1] not in 'aeiouAEIOU':
        n = n[:len(n)-i]
        break
vowel_pattern = re.compile(r'([aeiouAEIOU]{2,})')
match = vowel_pattern.findall(n)
if not in match:
    print(-1)
else:
    for i in match:
        print(i)
