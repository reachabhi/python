#Find the number of occurrences of a substring in a string
#https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    count=0
    for i in range(0, len(string)-1):
        if(sub_string == string[i:len(sub_string)+i]):
            count+=1
    return count
  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)