import random

def mergeSort(x):
    if len(x) < 2:
        return x
    result = []          # moved!
    mid = int(len(x)/2)
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])
    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
    result += y
    result += z
    return result


def quickSort(x):
    if len(x) < 2:
        return x
        
    smaller = []
    equal = []
    greater = []

    rand = random.randint(0, len(x)-1)
    item = x[rand]
    for i in x:
        if i < item:
            smaller.append(i)
        elif i==item:
            equal.append(i)
        else:
            greater.append(i)

    return quickSort(smaller) + equal + quickSort(greater)