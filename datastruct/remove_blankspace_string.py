def remove_space_and_create_list(string):
	x,y,z=[],[],[]
	#Create a list z of indices where spaces are present
	for i in range(len(string)):
		if string[i] == ' ':
			z.append(i)
	z.append(i+1)
    #Iterate through the length of the list of space indecs created above and slice the strings before and after space
	for i in range(len(z)):
		if i==0:
			x=string[:z[i]]
			y.append(x)	
		else:
			x=string[z[i-1]+1:z[i]]
			y.append(x)
	print(y)


remove_space_and_create_list('I am Abhishek')
remove_space_and_create_list('Hello Abhishek')
remove_space_and_create_list('It was nice talking to you')
remove_space_and_create_list('Bye')

