#https://www.hackerrank.com/contests/pycode2015/challenges/dictionary-assignment
n = int(input())
str_lists, unique_chars, hist=[],[],{}
for i in range(n):
    str_lists.append(input())
for strings in str_lists:
    l=list(set(strings))
    unique_chars.append(''.join(l))
for i in range(len(unique_chars)):
    for j in unique_chars[i]:
        hist[j]=str_lists[i].count(j)
    hist={k:hist[k] for k in sorted(hist.keys())}
    for k,v in hist.items():
        print('Letter {}  appears  {}  time/s'.format(k,v))
    print('\n')
    hist={}