def swap_case(s):
    l=[]
    for i in s:
        #print(ord(i))
        if ord(i) <=122 and ord(i) >=97 :
            l.append(chr(ord(i)-32))
        else:
            if ord(i) <=90 and ord(i) >=65 :
                l.append(chr(ord(i)+32))
            else:
                l.append(i)

    return ''.join(l)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)