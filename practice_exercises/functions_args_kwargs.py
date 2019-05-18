#Parameters ordering
# 1. Parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs

def info(a, b, *args, name='Abhishek', **kwargs):
	print(type(kwargs))
	print(type(args))
	print(kwargs) #converts key value pairs passed like fav_game and fav_player to a dictionary using **kwargs
	print(args) #takes any data_struct after a and b
	print(name) #overwrites name as Anil
	print(*args)


info(1, 2, ('Cricket', 'Football', {'games':['Cricket','Football']}) , name='Anil', fav_game='Cricket', fav_player='Sachin') #If we do provide name =Anil and just 'Anil', it will be considered as *args




