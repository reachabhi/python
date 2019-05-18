def generate_list(dimension):
    l=[]
    m=[]
    for i in range(1,dimension+1):
        m.clear()
        var=0
        for j in range(1,i+1):
            var+=1
            m.append(var)
        l.append(m)
    for x in l:
        print(l)




if __name__ == '__main__':
    dimension = int(input())
    generate_list(dimension)
