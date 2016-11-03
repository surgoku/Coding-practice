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

def quickSelect(x, k):
    if not x:
        return -1
    pivot = x[len(x)/2]
    smaller = []
    greater = []
    
    for i in x:
        if i < pivot:
            smaller.append(i)
        elif i> pivot:
            greater.append(i)
    
    similar_count = len(x) - len(smaller) - len(greater)
    
    if len(smaller) > k:
        return quickSelect(smaller, k)
    elif k > len(smaller) and k < len(smaller) + similar_count:
        return pivot
    else:
        return quickSelect(greater, k-len(smaller)-similar_count)


def run():
    arr1 = [3,5,1,2,7,8,1,3,12,14,15]
    arr = [70, 120, 170, 200]
    print quickSelect(arr1, 4)
    
    
run()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 