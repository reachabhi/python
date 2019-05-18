def find_repeated(w):
    l=[] #for repeated items
    for i in range(len(w)):
        j=i+1
        #for k in range(j,len(w)):
        if w[i] not in l:
            l.append(w[i])
                      
    print(''.join(l))
        

if __name__=='__main__':
    w='ABSSWAB'
    find_repeated(w)
