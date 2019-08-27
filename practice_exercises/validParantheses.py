'''
valid_parentheses("()") # True
valid_parentheses(")(()))") # False
valid_parentheses("(") # False
valid_parentheses("(())((()())())") # True
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False

'''

def valid_parentheses(x):
	openparantheses = [i[0] for i in enumerate(x) if i[1]=='(']
	print(openparantheses)
	closeparantheses = [i[0] for i in enumerate(x) if i[1]==')']
	print(closeparantheses)
	if len(openparantheses)==len(closeparantheses):
		return all([closeparantheses[i]>openparantheses[i] for i in range(len(closeparantheses))])
	return False


