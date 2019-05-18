#https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#Identify the presence of alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters in a string.

if __name__ == '__main__':
    s = input()
    i=0
    char_arr=list(s)
    for char in char_arr:
        i+=1
        if char.isalnum():
            print('True---', i, char)
            break
        if i==len(char_arr):
            print('False----', char)
    i=0
    for char in char_arr:
        i+=1
        if char.isalpha():
            print('True---', i, char)
            break
        if i==len(char_arr):
            print('False----',i,  char)
    i=0
    for char in char_arr:
        i+=1
        if char.isdigit():
            print('True----',i,   char)
            break
        if i==len(char_arr):
            print('False----',i,  char)
    i=0
    for char in char_arr:
        i+=1
        if char.islower():
            print('True----',i,  char)
            break
        if i==len(char_arr):
            print('False----',i,  char)
    i=0
    for char in char_arr:
        i+=1
        if char.isupper():
            print('True----',i,  char)
            break
        if i==len(char_arr):
            print('False----',i,  char)
     
    

