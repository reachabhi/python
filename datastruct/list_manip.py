def list_manipulation(lst, cmd, loc, val=None):
    if cmd=='remove' and loc=='end':
        print(lst[-1]    )
    elif (cmd=='remove' and loc=='beginning'):
    	print (lst[0])
        
    elif (cmd=='add' and loc=='end'):
        lst.append(val)
        print (lst)
    elif (cmd=='add' and loc=='beginning'):
    	lst.insert(0,val)
    	print (lst)

list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]