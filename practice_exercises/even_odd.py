#https://www.geeksforgeeks.org/rearrange-odd-and-even-values-in-alternate-fashion-in-ascending-input_order/

'''
Rearrange Odd and Even values in Alternate Fashion in Ascending Order

Given an array of integers (both odd and even), the task is to arrange them in such a way that odd and even values come in alternate fashion in non-decreasing order(ascending) respectively.

    If the smallest value is Even then we have to print Even-Odd pattern.
    If the smallest value is Odd then we have to print Odd-Even pattern.

Note: No. of odd elements must be equal to No. of even elements in the input array.

Examples:

    Input: arr[] = {1, 3, 2, 5, 4, 7, 10}
    Output: 1, 2, 3, 4, 5, 10, 7
    Smallest value is 1(Odd) so output will be Odd-Even pattern.

    Input: arr[] = {9, 8, 13, 2, 19, 14}
    Output: 2, 9, 8, 13, 14, 19
    Smallest value is 2(Even) so output will be Even-Odd pattern.

'''
n=int(input())
#integer_list = map(int, input().split())
integer_list=[]
for i in range(n):
	integer_list.append(int(input()))
#print(integer_list)

odd_list=[i for i in integer_list if i%2!=0]
odd_list.sort()
print(odd_list)
even_list=[i for i in integer_list if i%2==0]
even_list.sort()
print(even_list)
j=0

if min(even_list) < min(odd_list):
	if len(even_list) > len(odd_list): #PASS
		for i in range(1,len(odd_list)+3,2):
			even_list.insert(i,odd_list[j])
			j+=1
		print(even_list)

	else: #PASS
		for i in range(0,len(even_list)+2,2):
			odd_list.insert(i,even_list[j])
			j+=1
		print(odd_list)
	

else: 
	if len(even_list) > len(odd_list): #PASS
		for i in range(0,len(odd_list)+2,2):
			even_list.insert(i,odd_list[j])
			j+=1
		print(even_list)
	else: #PASS
		for i in range(1,len(even_list)+3,2):
			odd_list.insert(i,even_list[j])
			j+=1
		print(odd_list)
	


