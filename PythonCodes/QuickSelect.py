import math

def quickSelect (l,k):
    mid = len(l)/2
    pivot = l[mid]
    smaller = []
    larger = []
    
    for i in l:
        if i < pivot:
            smaller.append(i)
        if i > pivot:
            larger.append(i)
            
    m = len(smaller)
    n = len(larger)
    
    equal_to_k = len(l) - (m + n)
    
    if k >= m and k < m + equal_to_k:
        return pivot
    elif m > k:
        return quickSelect (smaller,k)
    else:
        return quickSelect(larger, k-m-equal_to_k)
    

def quickSelect3(lst, k):
    if len(lst) != 0:
        pivot = lst[(len(lst)) // 2]
        smallerList = []
        for i in lst:
            if i < pivot:
                smallerList.append(i)
        largerList = []
        for i in lst:
            if i > pivot:
                largerList.append(i)
        count = len(lst) - len(smallerList) - len(largerList)
        m = len(smallerList)
        if k >= m and k < m + count:
            return pivot
            print(pivot)
        elif m > k:
            return quickSelect(smallerList, k)
        else:
            return quickSelect(largerList, k-m-count)

def quickSelectBit(l,k):
    #doesn't work yet make it work'
    var = 0
    
    for i in l:
        var |= (1<<i)
    
    count = 0
    while var:
        bit = var /2
        var = var/2
        if bit:
            count+=1
        
        if count == k:
            return math.pow(2,count)


l = [8,9,1,2,3,3,3,4,5,10]

print quickSelect(l, 4)
print quickSelectBit(l,4)
print quickSelect3(l,4)
    
    
    
            
    
    
    

