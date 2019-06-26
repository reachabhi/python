num = '4444422222331111115'
l = list(num)
def gen(l):
	for i in l:
		yield(i)
x = gen(l)

final = []
con, c = 1, 1
y = next(x)
while con <= len(num):
	z = next(x)
	if y==z:
		c+=1
	else:
		c = 1
	y = next(x)
	con += 1
	
final.append((c, int(y)))
print(final)




		


