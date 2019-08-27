arr = [10, 10, 56, 48, 31, 11, 22, 12]

min_item = 25555
sec_min = 256646
for i in range(len(arr)):
	if arr[i] < min_item:
		sec_min = min_item
		min_item = arr[i]
	if arr[i] > min_item and arr[i] < sec_min:
		sec_min = arr[i]

print(min_item, sec_min)
