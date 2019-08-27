import re
n = [''.join(input().split('\n')) for _ in range(2)]
pattern = re.compile(r'(?=('+n[1]+'))')
match = pattern.findall(n[0])
match_len = len(match)
pattern_length = len(n[1])
#print(match.start(), match.end())
print(type(n[0]), n[1], match, match_len, pattern_length, len(n[0]))
if not match:
	print(-1,-1)
else:
	for i in range(len(n[0])-pattern_length+1):
		if n[i:i+pattern_length]==match[0]:
			if i==len(n[0]-pattern_length):
				print(i,i+pattern_length-1)
			else:
				print(i,i+pattern_length)
