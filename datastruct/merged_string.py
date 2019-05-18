#https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    # your code goes here
    string_length = len(string)
    groups=int(string_length/k)
    for i in range(0,string_length,k):
        group,l=string[i:i+k],[] #for repeated items
        [l.append(group[i]) for i in range(0,len(group)) if group[i] not in l]
        print(''.join(l))
        l.clear()



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)