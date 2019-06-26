#Pass functions in other functions
from random import choice
def sum(n, func):
	total = 0
	for num in range(1, n+1):
		total += func(num)
	return total

def square(x):
	return x*x

print(sum(6,square))


#Functions can return function as well
def make_laugh(person):
	def get_laugh():
		laugh = choice(('ROFL', 'hahhaha', 'lol'))
		return f'{laugh} {person}'  #didnt pass person to get_laugh() function but it knows the valus as its a prt od make_laugh()

	return get_laugh

laugh = make_laugh('Linda')
print(laugh())