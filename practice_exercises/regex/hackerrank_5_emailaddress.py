import re, email.utils
n = int(input())
format_emaildata=[]
emaildata = [input() for _ in range(n)]
for i in emaildata:
	x = email.utils.parseaddr(i)
	format_emaildata.append(x) 

pattern = re.compile(r'(^[a-zA-Z][a-zA-Z0-9\-+._]+@[a-z]+\.[a-z]+$)')
print('\n')
for i in format_emaildata:
	match = pattern.search(i[1])
	#print(i, match)
	if match:
		print(email.utils.formataddr(i))