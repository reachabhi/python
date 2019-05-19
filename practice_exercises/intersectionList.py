'''
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

Input:  ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output: [80, 20]

Input:  ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]
Output: [5, 5]

'''

def common(l1, l2, l3):
	l1_common_l2 = list(filter(lambda x : x in l2, l1))
	l1_common_l2_common_l3 = list(filter(lambda x : x in l3 ,l1_common_l2))
	print(l1_common_l2_common_l3)

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

common(ar1, ar2, ar3)

