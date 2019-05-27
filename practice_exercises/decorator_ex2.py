def be_polite(fn):
	def wrapper():
		print('What a pleasure to meet you')
		fn()
		print('have a great day')
	return wrapper

@be_polite
def greet():
	print('My name is jack')

#greet = be_polite(greet) #function name passed as arg. can call greet() as fn() on line 4 from be_polite() func as well
greet()

#To avoid 'greet = be_polite(greet)' we can directly add decorator @be_polite which means be_polite