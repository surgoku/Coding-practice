from boto.mws.response import Destination
from __builtin__ import True


def towerOfHanoi(n, source, buffer, destination):
    if n > 0:
        towerOfHanoi(n-1, source, destination, buffer)
        if len(source):
            destination.append(source.pop())
        
        towerOfHanoi(n-1, buffer, source, destination)
 


def minimumEditDistanceRecur(str1, str2):
    m = len(str1)
    n = len(str2)
    
    if str1== str2:
        return 0
    
    if (m==0 and n==0): return 0
    
    if (m==0): return n
    if (n==0): return m
    
    left = minimumEditDistanceRecur(str1[1:], str2) + 1
    right = minimumEditDistanceRecur(str1, str2[1:]) + 1
    
    #print left, right
    corner = minimumEditDistanceRecur(str1[1:], str2[1:]) + int(str1[0] != str2[0])
    
    return min(left, right, corner )
    
    

def minimumEditDistanceDP(str1, str2):
    m = len(str1) + 1
    n = len(str2) + 1
    
    matrix = [[0]*m for i in range(n)]
    
    if str1== str2:
        return 0
    
    for i in range(m):
        matrix[0][i] = i
    
    for j in range(n):
        matrix[j][0] = j
        
    
    for i in range(1,n):
        for j in range(1,m):
            if str1[j-1] == str2[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
    
    return matrix[n-1][m-1]
    


def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def powerset2(seq, out):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        out.append(seq)
        return seq
    else:
        for item in powerset2(seq[1:], out):
            out.append([seq[0]])
            out.append([seq[0]]+[item])
            out.append([item])
            #return [seq[0]]+item
            #yield item
            
def longestCommonSubstring(str1, str2):
    if str1 == str2:
        return str1
    
    # Since longest common string will be as big as the smaller one hence outer loop
    if len(str1) > len(str2):
        str1, str2 = str2,str1
    
    n = len(str1)
    m = len(str2)

    
    lcs = ""
    
    for i in range(n):
        local = ""
        for j in range(m):
            if i+j < n and str1[i+j] == str2[j]:
                local += str2[j]
            else:
                if len(lcs) < len(local):
                    lcs = local
                    local = ""
                    
    return lcs


def longestIncreasingSubsequence(input):
    
    if not input:
        return 0
    
    if len(input) ==1:
        return 1
    
    n = len(input)
    
    matrix = [1]*n
    
    for i in range(1,n):
        for j in range(0, i):
            if input[i] > input[j] and matrix[i] < matrix[j] + 1:
                matrix[i] = matrix[j] + 1
                
    return max(matrix)
        
    
def maxContiguousSubArraySUM(arr):
    matrix = [0]*len(arr)
    matrix[0] = arr[0]
    
    
    for i in range(1,len(arr)):
        #for j in matrix:
        if arr[i] + matrix[i-1] > matrix[i]:
            matrix[i] = arr[i] + matrix[i-1]
        #for j in range(i, len(arr)):
    
    return max(matrix)   
    
    



def maximumProductSubarray(arr):
    #  consecutive sub-array  with max product
    # partial code doesn't work for all
    matrix = [1]*len(arr)
    matrix[0] = matrix[0]*arr[0]
    for i in range(1,len(arr)):
        if arr[i]*matrix[i-1] > matrix[i]:
            matrix[i] = matrix[i-1]*arr[i]
            
    return max(matrix)
        
    
    
# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
def lps(str):
    n = len(str)
 
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
 
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1] 


def findSubArraySum(arr, val):
    subarr_map = {}
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum  == val:
            print "0 to ", str(i)
            return
        if (curr_sum - val) in subarr_map:
            print str(subarr_map[curr_sum - val]) + " to " + str(i)
            return
        
        subarr_map[curr_sum] = i
    
    print "Not found"
    
def findSubSetSumFromArrayExistsRecur(arr, val):
    # check whether subset with a given sum exist
    # time complexity exponential
    def helper(arr, val, n):
        if val==0:
            return True
        
        if n==0 and val !=0:
            return False
        
        if arr[n-1] > val:
            return helper(arr, val, n-1)
        
        return helper(arr, val-arr[n-1], n-1) or helper(arr, val, n-1)
    helper(arr,val, len(arr))  

    
def findSubSetSumFromArrayExistsDP(arr, val):
    # Time complexity: n*val
    m = val
    n = len(arr)
    
    matrix = [[False]*(m+1)]*(n+1)
    
    #If sum is 0, then answer is true
    for i in range(n+1):
        matrix[0][i] = True
        
    #If sum is not 0 and set is empty
    for j in range(1, m+1):
        matrix[j][0] = False  
    
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            matrix[i][j] = matrix[i][j-1] 
            if i>= arr[j-1]:
                matrix[i][j] = matrix[i][j] or matrix[i-arr[j-1]][j-1]
                
                
    
    return matrix[m][n]
            
    
def findSubsetSumFromArray(arr, val):
    def tsum(currentSum,total,input,record,n, val):
        if total==sum :
          for i in range(0,n):
           if record[i]:
            print input[i]
                        
           i = i+1
           for i in range(i,n):
            if record[i]:
             print input[i]
           print ""
           return
        i=currentSum
        for i in range(i,n):
         if total+input[i]>sum :
          continue
         if i>0 and input[i]==input[i-1] and not record[i-1] : 
          continue
         record[i]=1
         tsum(i+1,total+input[i],input,record,l, val)
         record[i]=0
    
    record = []
    l = len(arr)
    
    for i in range(0,l):
        record.append(0)
    print "From the array the elements equal to val are:"
    tsum(0,0,input,record,l,val)
    
    
    
def run():
    source = [1,2,3,4,5]
    buffer = []
    destination = []

    towerOfHanoi(len(source), source, buffer, destination)
    #print destination
    
    #print minimumEditDistanceDP("abc", "bc")
    source = [1,2]
    out = []
    powerset2(source, out)
    #print list(out)
    
    str1 = "chandra"
    str2 = "chand"
    #print longestCommonSubstring(str1, str2)
    
    arr = [6,2,8,-10,0,-4,10,100, -2]
    
    #print maxContiguousSubArraySUM(arr)
    #print maximumProductSubarray(arr)
    findSubArraySum(arr, 106)
run()