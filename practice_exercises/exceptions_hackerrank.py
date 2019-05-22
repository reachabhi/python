#https://www.hackerrank.com/challenges/exceptions/problem
n = int(input())
instructions = []
for i in range(n):
    instructions.append(input().split())
for i in instructions:
    try:
        res = int(i[0])//int(i[1])
        print(res)
    except ZeroDivisionError as e:
        print('Error Code: {}'.format(e))
    except ValueError as e:
        print('Error Code: {}'.format(e))