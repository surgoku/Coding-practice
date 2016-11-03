


def coinChangeRecur(l, sum, count):
    def coinChange(i, subSum):
        if subSum == 0:
            return 1
        elif subSum < 0 or i < 0:
            return 0
        else:
            return coinChange(i-1, subSum) + coinChange(i, subSum-l[i])
    return coinChange(len(l)-1, sum)


# Dynamic Programming Python implementation of Coin Change problem
def coinChangeDP(l, sum):
    # We need n+1 rows as the table is consturcted in bottom up
    # manner using the base case 0 value case (n = 0)
    
    m = len(l)
    n = sum
    
    table = [[0 for x in range(m)] for x in range(n+1)]
    
    
 
    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - l[j]][j] if i-l[j] >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
 
    return table[n][m-1]


def coinChangeDP2():
    target = 200
    coins = [1,2,5,10,20,50,100,200]
    ways = [1]+[0]*target
    for coin in coins:
        for i in range(coin,target+1):
            ways[i]+=ways[i-coin]
    print(ways[target])

def minCoinChangeRecur(l, sum):
    def minCoin(i, subSum):
        
        if subSum == 0:
            return 0
        elif subSum < 0 or i < 0:
            return float('inf')
        else:
            return min(minCoin(i-1, subSum), 1+ minCoin(i, subSum-l[i]))
        
    return minCoin(len(l)-1, sum)


def minCoinChangeDP(l, sum):
    m = len(l) + 1
    n = sum + 1
    matrix = [[0]*n for i in range(m)]
    
    for i in range(1, n):
        matrix[0][i] = float('inf')
    
    for i in range(1,m):
        for j in range(1,n):
            temp = float('inf')
            if j >= l[i-1]:
                temp = matrix[i][j-l[i-1]]
            matrix[i][j] = min(matrix[i-1][j], temp+1)
            
    return matrix[m-1][n-1]
    
    
    def minCoin(i, subSum):
        
        if subSum == 0:
            return 0
        elif subSum < 0 or i < 0:
            return float('inf')
        else:
            return min(minCoin(i-1, subSum), 1+ minCoin(i, subSum-l[i]))
        
    return minCoin(len(l)-1, sum)


sum = 5
l = [1, 2, 3,4, 5]

print coinChangeDP(l, sum)
#coinChangeRecur(10, [1,2,3,4,5], 0)
    
    
    