def isEven(num):
    return num % 2 == 0


def partition(collection, fn):
    return [[i for i in collection if isEven(i)], [i for i in collection if not isEven(i)]]
   

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
