def unpack(*args):
	total = 0
	print(args)
	print(*args)
	for i in args:
		total+=i
	print(total)

unpack(1,2,3,4)
nums = [1,2,3,4]
#unpack(nums) #throws error because args in this case will be a list and we cannot add total + list.
unpack(*nums) #It works

def unpack(name, org):
	print(name, org)

info = {'name':'jill', 'org':'jil_org'}

unpack(name='jack', org='jack_org')
unpack(**info)


def method(a, b, c, **kwargs):
	print(a, b, c, kwargs)


data = dict(a=1, b=2, c=3, d=4, name2='method')
method(**data, name1='hello') #1 2 3 {'d': 4, 'name2': 'method', 'name1': 'hello'}
