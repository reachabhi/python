list_tup = [('x', 'y'), ('x', 'z'), ('w', 't'),('x', 's'),('r', 'd'),('w', 'v')]
list2 = [list(i) for  i in list_tup]
print(list2)
z,y=[],[]
for i in range(len(list2)):
	z.append(list2[i][0])
z=[list(i) for i in set(z)]
for i in range(len(z)):
	for j in list2:
		if j[0] in z[i]:
			z[i].append(list(j)[1])
z=[tuple(i) for i in z]
print(z)







