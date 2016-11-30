'''
Created on Nov 3, 2016

@author: root
'''
from operator import itemgetter

def EuclDist(point1, point2):
    pass

# Facebook
def findKNearest(coordinates,k):
    # coordinates are tuples
    
    dist_map = {}
    origin = (0,0)
    
    
    # this loop is O(N), N is number of cordinates
    for point in list(coordinates):
        coord = ",".join(point)
        dist = EuclDist(point, origin) #assuming constant time
        if coord not in dist_map:
            dist_map[coord] = dist
    
    # N points: sorting Nlog(N) 
    # O(N) : convert to O(N) : Given K, quickSelect/MinHeap I can find which what is the distance for K
    # QuickSelect: Average_case of QuickSelect is O(N) worst is O(N^2)
    # MinHeap can be used to O(N)
    # list of distances: find kth smallest using quickSelect: O(N)
    # Now iterate through all the points and see whether dist < dist(k). O(N)
    nearest_k_points = sorted(dist_map.items(), key=itemgetter(1))[:k]
    
    # using quick select
    distances = dist_map.values()
    coordinate_points = dist_map.keys()
    
    kth_distance = quickSelect(distances, k)
    
    distances_less_than_or_equal_to_k = []
    for (dist,idx) in enumerate(distances):
        if dist <= kth_distance:
            distances_less_than_or_equal_to_k.append(dist, idx)
    
    selected_points = []
    
    for dist, idx in distances_less_than_or_equal_to_k:
        chosen_point = coordinate_points[idx]
        selected_points.append(chosen_point.split(','))
        # string format coordiates
    
    
    output_points = [point[0].split(',') for point in nearest_k_points] # string format coordiates
    
    return output_points, selected_points


def quickSelect(distance_list, k):
    # Returns the distance which is on position k-1 if sorted in increasing order
    # O(N) + O(n/2)... 
    # Worst performance O(N^2), Average: O(N)
    # Use MinHeap for most optimal
    if not distance_list:
        return -1 # assuming distances is not less than 0
    
    n = len(distance_list)
    pivot = distance_list[n//2]
    
    smaller = []
    greater = []
    
    # O(N)
    for dist in distance_list:
        if dist < pivot:
            smaller.append(dist)
        elif dist > pivot:
            greater.append(dist)
            
    # number of points which are equal to pivot
    equal_counts = n - len(smaller) - len(greater)
    
    if len(smaller) > k:
        return quickSelect(smaller, k)
    elif k > len(smaller) and k < len(smaller)+ equal_counts:
        return pivot
    else:
        return quickSelect(greater, k-len(smaller) - equal_counts)
    
    