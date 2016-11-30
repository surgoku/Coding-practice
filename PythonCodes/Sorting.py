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



            
        



    
    
    


    
def HeapSort(arr):
     # nice video: https://www.youtube.com/watch?v=oAYtNV6vy-k
    # Rules to create the min heap:
        # 1 first heapify and then min-heapify i.e. start from zeroth index the child
        # of an index is 2*i+1 and 2*i + 2
        # 2. Always start with Flor(n/2) level or index in the array (i.e. second last layer) and iterate till 
        # index 0 i.e. beginning to check whether parent is smaller than the child if not
        # swap. 
        # 3. Once reached till the beginning iterate from beginning to leaves and check whether 
        # parent is smaller then children else swap
        
    def heapify(arr):
        start = (len(arr) - 2) / 2  # step 2
        while start >= 0:
            siftDown(arr, start, len(arr) - 1)
            start -= 1

    def siftDown(arr, start, end):
        #left_child = 2*parent + 1
        #right_child = 2*parent + 2
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            if child <= end and arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

    heapify(arr)
    end = len(arr) - 1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        siftDown(arr, 0, end - 1)
        end -= 1
        

# Median of medians to select the median
def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList)-1)/2)))
    med = select(Meds, int((len(Meds)-1)/2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j-len(L1)-len(L2))

def run():
    arr1 = [3,5,1,2,7,8,1,3,12,14,15]
    arr = [70, 120, 170, 200]
    #print quickSelect(arr1, 4)
    HeapSort(arr1)
    print arr1
    
run()
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 