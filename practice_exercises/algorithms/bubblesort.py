''' 
 i  j--> 0 1 2 3 4 5 6 7 
 0       5 3 1 9 8 2 4 7
 1       3 5 1 9 8 2 4 7
 2       3 1 5 9 8 2 4 7
 3       3 1 5 9 8 2 4 7
 4       3 1 5 8 9 2 4 7
 5       3 1 5 8 2 9 4 7
 6       3 1 5 8 2 4 9 7
 7       3 1 5 2 8 4 7 9
'''

def bubblesort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


arr = [5, 3, 1, 9, 8, 2, 4, 7]
print(bubblesort(arr))
