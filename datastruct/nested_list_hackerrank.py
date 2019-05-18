x,y,z=[],[],[] #https://www.hackerrank.com/challenges/nested-list/problem
for _ in range(int(input())):
    name = input()
    score = float(input())
    x.append(name)
    x.append(score)
    y.append(x)
    x=[]
#print(y)

y.sort(key = lambda a:a[1])
print(y)
found=True
for i in range(len(y)):
	if i<len(y):
		if y[i][1]==y[i+1][1]:
			pass
		else:
			second_lowest=y[i+1][1]
			break

print(second_lowest)

z=[[i[0],i[1]] for i in y if i[1]==second_lowest]

print([a[0] for a in z])

#z=[i[1] for i in y]
#z.sort()
#print([i[0] for i in y if z[-2] is i[1]])


