n = '111122344666666644'
count = 0
char_count = {}
y = n[0]

for i in range(len(n)):
	if n[i]==y:
		count+=1
	else:
		y=n[i]
		count = 1
	char_count.update({y:count})

print(char_count)
