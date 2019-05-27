import itertools
n = int(input())
arr = input().split()
arr = arr[:n]
k = int(input())
tuples_list = list(map(lambda x: str(x),range(1,n+1)))
combinations_list = list(itertools.combinations(tuples_list, k))
print(combinations_list)
total_count = len(combinations_list)
#[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
count = 0
index_a = tuple(x+1 for x in range(len(arr)) if arr[x] == 'a')
for i in combinations_list: #make sure the map is accessed only once else we need to recreate map as in line 7
	for j in index_a:
		if str(j) in i:
			count += 1
			break

print(count)
print(total_count)
print(count/total_count)
print(index_a)

	

