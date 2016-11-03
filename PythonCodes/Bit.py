def add (x,y):
    
    while(y):
        carry = x&y
        x = x^y
        y = carry << 1
        
    return x


def subtract(x,y):
    while(y):
        carry = (~x)&y
        x = x^y
        y = carry << 1
        
    return x

print subtract(3,2)


def setBit(val, index, bit):
    mask = 1 << index
    val &= ~mask
    if bit: # i.e. bit is 1 
        val |= mask
    
    return val

def getBit(val, index):
    mask = 1 << index
    if val & mask:
        return 1
    return 0

def pythonBit(val):
    # bit string:
    print bin(val)
    # non-zero bits:
    print bin(val).count("1")
    
    
def getAllNonZeroBitIndex(val):
    counter = 0
    
        
    
#print setBit(4, 1, 1)
#print getBit(4, 0)

getAllNonZeroBitIndex(6)

