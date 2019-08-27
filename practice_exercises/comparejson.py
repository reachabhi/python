import json

def compare_dict(x, y):
    if len(x) != len(y):
        result = 'different'
    else:
        for keys in x:
            result = compare(x[keys], y[keys])
            if result=='different':
                print(f'{keys} -  key are different ')
                break
    return result


def compare_list(x, y):
    if len(x) != len(y):
        result = 'different'
    else:   
        for i in range(len(x)):
            result = compare(x[i], y[i])
            if result=='different':
                print(f'{x[i]} and {y[i]} are different ')
                break
    return result


def compare_tuple(x, y):
    pass


def compare_set(x, y):
    pass


def compare(x, y):
    if type(x) == type(y):
        if type(x) == dict:
            result = compare_dict(x, y)
        elif type(x) == list:
            result = compare_list(x, y)
        elif type(x) == tuple:
            result = compare_tuple(x, y)
        elif type(x) == set:
            result = compare_set(x, y)
        elif x == y:
            result = 'same'
        else:
            result = 'different'
    else:
        result = 'different'
    return result


    # if any([type(x[keys]) in (dict,list,tuple,set) for keys in y.keys()]):
x = '/home/abhishek/python/practice_exercises/userPayload1.json'
y = '/home/abhishek/python/practice_exercises/userPayload.json'

if __name__ == '__main__':
    with open(x) as f1:
        f1_json = json.loads(f1.read())
    with open(y) as f2:
        f2_json = json.loads(f2.read())
    print(compare_dict(f1_json, f2_json))
