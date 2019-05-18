def extract_commands(command): #https://www.hackerrank.com/challenges/python-lists/problem
    x,y,z=[],[],[]
    #Create a list z of indices where spaces are present
    for i in range(len(command)):
        if command[i] == ' ':
            z.append(i)
    z.append(i+1)
    #Iterate through the length of the list of space indecs created above and slice the strings before and after space
    for i in range(len(z)):
        if i==0:
            x=command[:z[i]]
            y.append(x) 
        else:
            x=command[z[i-1]+1:z[i]]
            y.append(x)
    print(y)

    return y


if __name__ == '__main__':
    N = int(input())
    command_collection, collection = [], []
    for i in range(N):
    	command = input()
    	command_collection.append(command)
    print(command_collection)
    command_list_collection = [extract_commands(x) for x in command_collection]
    print(command_list_collection)
    for x in command_list_collection:
        if (x[0]=='insert' and x[1] and x[2]):
            collection.insert(int(x[1]),int(x[2]))
        elif (x[0]=='append' and x[1]):
            collection.append(int(x[1]))
        elif (x[0]=='remove' and x[1]):
            collection.remove(int(x[1]))
        elif x[0]=='pop':
            collection.pop()
        elif x[0]=='sort':
            collection.sort()
        elif x[0]=='reverse':
            collection.reverse()
        elif x[0]=='print':
            print(collection)

    print(collection)



