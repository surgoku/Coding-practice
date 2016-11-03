def getUnbiasedOutputFromBiasedInput():
    # let's say coin generates 1 with 60% and 0s with 40%.
    # How to get unbiased o/p: Simply use two biased coins:
    # Example Prob of 10 = 0.6*0.4 =0.24 == P(01)
    
    out1 = biasedMethod() # returns 1: 60% and 0 40%
    out2 = biasedMethod()
    
    if out1 == 1 and out2 ==0:
        return 1
    if out2 == 0 and out1 == 1:
        return 0
    
    return getUnbiasedOutputFromBiasedInput()

def biasedMethod():
    pass