import re
'''
n = int(input())
input_string = [''.join(input().split('\n')) for _ in range(n)]
pattern = re.compile(r'(?=(\s\|{2}\s|\s\&{2}\s))')
replace = {' && ':' and ',' || ':' or '}
match = pattern.findall(''.join(input_string))
m = pattern.search(''.join(input_string))
print(m, m.group(1), m.group(2))
#replaced = re.sub('(?=(\s\|{2}\s|\s\&{2}\s))',lambda x:replace[x.groups()],str(input_string))
#print(replaced)
'''
import re

regex = r"(?=(\s\|{2}\s|\s\&{2}\s))"

test_str = ("a = 1;\n"
	"b = input();\n\n"
	"if a + b > 0 && a - b < 0:\n"
	"    start()\n"
	"elif a*b > 10 || a/b < 1:\n"
	"    stop()\n"
	"print set(list(a)) | set(list(b))\n"
	"#Note do not change &&& or ||| or & or |\n"
	"#Only change those '&&' which have space on both sides.\n"
	"#Only change those '|| which have space on both sides.\n")

matches = re.finditer(regex, test_str, re.MULTILINE)
print(matches)
for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))