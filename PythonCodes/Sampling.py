'''
Created on Nov 2, 2016

@author: root
'''

import math
import random
import numpy as np

def coin():
    out = int(random.choice([True, False]))
    return np.random.rand() > .5
    #return out
    

def findRandomUsingCoin(begin, n):
    # if 1 then b/w 0 to n/2 else n/2 to n
    # and so on
    # Doesn't completely work yet
    
    if n-begin == 0 :
        return begin
    
    mid = int(round((begin+n)/2.))
    dice_out = coin()
    
    if not dice_out:
        if begin <= mid:
            return findRandomUsingCoin(begin, mid)
        else:
            return begin
    else:
        if mid <=n:
            return findRandomUsingCoin(mid, n)
        else:
            return mid
       

def findRandomUsingCoin2(n):
    out = [0]*n
    
    for i in range(1,n):
        if  coin():
            out[i] += out[i-1] 
            out[i] = out[i] % n
        else:
            out[i] -= (out[i-1] + n) % n
        
    return out


def findRandomUsingDice(n):
    pass


def findUnbiasedCoinUsingBiasedCoin():
    pass

def prob10(half):
    if half >= 10:
        return 0    
    #f1 can be replaced by this rd.randint(0, 1)
    toss_value = coin() 
    # check if toss falls in this current half and then change the half for next recursion. 
    # we change half from 1, 2, 4, 8, 16, 36, 64, 128
    result = toss_value*half + prob10(half<<1)
    if result > 10:
        return prob10(1)
    else:
        return result


def generateRandomNumber(n,k):

    def helper(n):
        tmp_num = []
        for i in range(20):
            tmp_num.append(coin())
        # tmp_num =[0,1,1,0,....0] with 20 elements
        
        tmp_num = [str(int(x)) for x in tmp_num]
        tmp_num = ''.join(tmp_num)  #'0110...0'
        rand_num = int(tmp_num, 2)  # if rand_num is large enought
        rand_num = rand_num % (n+1)  # this will be uniformly distributed from 0 to n+1
    
    result = []
    for i in range(k):
        result.append(helper(n))
    
    return result


def run():
    out_map = {}
    count = 0
    """
    for i in range(100000):
        out = findRandomUsingCoin(1,10)
        if out not in out_map:
            out_map[out] = 0
        out_map[out] += 1
        count += 1
    
    for i in out_map:
        print i, out_map[i]*100./count
    #print out_map
    """
    count = 0
    for i in range(0, 100000):
        out = prob10(1)
        if out not in out_map:
            out_map[out] = 0
        out_map[out] += 1
        count += 1
    
    #for i in out_map:
    #    print i, out_map[i]*100./count
        
        
    print generateRandomNumber(1000, 5)
    #print findRandomUsingCoin2(10)
run()
