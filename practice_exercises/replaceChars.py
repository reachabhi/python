'''
Given a string S, c1 and c2. Replace character c1 with c2 and c2 with c1.
Examples:

Input : str = 'grrksfoegrrks'
        c1 = e, c2 = r 
Output : geeksforgeeks 

Input : str = 'ratul'
        c1 = t, c2 = h 
Output : rahul
'''

def replace(text, c1, c2):
	print(f'Received text {text}')
	newchars=map(lambda x : x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2 ,text)
	print(''.join(list(newchars)))

replace('dbhiskek kumdr', 'd', 'a')