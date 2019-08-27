#https://www.hackerrank.com/challenges/new-year-chaos/problem

import math
import os
import random
import re
import sys

''' q 		   q1
1 2 3 4 5  	2 1 5 3 4
1 2 3 5 4
1 2 5 3 4			
2 1 5 3 4			

1 2 3 4 5 6 7 8		1 2 5 3 4 7 8 6

'''

# Complete the minimumBribes function below.
def minimumBribes(q):
	count=0
	q1 = q.copy()
	q.sort()
	print(q1, ' ----> ', q)
	bribe_dict = {}.fromkeys(q1,0)
	
	for i in range(1,len(q)+1):
			while(q1[-i]!=q[-i]):
				j=q.index(q1[-i])
				steps = len(q)-i-j
				if steps>2:
					print('Too chaotic')
					return
				for _ in range(steps):
					q[j],q[j+1]=q[j+1],q[j]
					count+=1
					j+=1

			

	print(q, count)


	



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
