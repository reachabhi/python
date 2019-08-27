'''
64 25 12 22 11
25 64 12 22 11
12 64 25 22 11
11 64 25 22 12

11 25 64 22 12
11 22 64 25 12
11 12 64 25 22

11 12 25 64 22
11 12 22 64 25

11 12 22 25 64 

'''

def selectionsort(arr):
	for i in range(len(arr)):
		minimum = arr[i]
		for j in range(i+1, len(arr)):
			if arr[j]<arr[i]:
				minimum=arr[j]
				arr[i], arr[j] = arr[j], arr[i]
	return arr

arr=[64, 25, 12, 22, 11]
print(selectionsort(arr))

