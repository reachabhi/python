'''

3 8 7 4 5 1 6 9 2  - i

3 7 8 4 5 1 6 9 2    1
3 7 8 4 5 1 6 9 2    2
3 4 7 8 5 1 6 9 2    3
3 4 5 7 8 1 6 9 2    4
1 3 4 5 7 8 6 9 2    5
1 3 4 5 6 7 8 9 2    6
1 2 3 4 5 6 7 8 9    7

'''

def insertionSort(arr):
	arr_len = len(arr)

	for i in range(1,arr_len):
		ele = arr[i]
		j = i-1
		while j >=0 and arr[j]>ele:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=ele

	print(arr)

arr = [3, 8, 7, 4, 5, 1, 6, 9, 2]
insertionSort(arr)





