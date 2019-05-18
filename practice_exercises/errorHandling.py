def error(a, b):
	try:
		res = a / b
	except TypeError as err:
		print(" a and b must be valid ints or floats ") #custom error
		print(err) #actual python error
	except ZeroDivisionError:
		print("Please do not divide by zero")
	else:
		print(f"{a} divided by {b} results {res}")
	finally:
		#print('Always gets printed after every Error')
		pass

error(2,3)
error(2,'l')
error(2,0)
error('t','t')