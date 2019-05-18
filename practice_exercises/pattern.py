#for i in range(10):
#	print()
#

print('Enter the levels of pyramid')
levels = int(input())
for i in range(1,levels):
	print(' ' * (levels-i) , "\U0001f600" * i)