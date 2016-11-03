'''
Created on Oct 31, 2016

@author: root
'''

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

def findDuplicateInArray(arr):
    exists = 0
    dup_arr = []
    
    for i in arr:
        bit_at_i = getBit(exists, i)
        if not bit_at_i:
            pass
        else:
            dup_arr.append(i)
        
        exists |= 1<<i
  
    return dup_arr

def findNonDuplicateInArray(arr):
    exists = 0
    non_duplicates = 0
    
    for i in arr:
        bit_at_i = getBit(exists, i)
        if not bit_at_i:
            non_duplicates = setBit(non_duplicates, i, 1)
        else:
            non_duplicates = setBit(non_duplicates, i, 0)
            
        exists |= 1<<i
    
    non_dup = []
    bit_str = bin(non_duplicates)
    bit_str = bit_str[::-1]
    index = 0
    for i in bit_str:
        if i=="1":
            non_dup.append(index)
        if i== "b":
            break
        index += 1
    
    return non_dup


def reversePolishNotation(input):
    # this is the problem to encode the numerical data with operations
    # for example 3 5 + 10 * implies add 3 and 5 (since + is followed by them),
    # then multiply 8 with 10
    # use stack
    stack = []
    for num in input.split():
        
        if num in ['-', '+', '*', '/']:
            num_1 = stack.pop()
            num_2 = stack.pop()
            if num == "-": stack.append(num_1 - num_2)
            if num == "+": stack.append(num_1 + num_2)
            if num == "*": stack.append(num_1 * num_2)
            if num == "/": stack.append(num_1 / num_2)
        else:
            stack.append(float(num))
    return stack.pop()



                
    
    
    

def run():
    arr = [1,1,2,3,4,4,5,3,6]
    
    print findDuplicateInArray(arr)
    print findNonDuplicateInArray(arr)
    
    expre = "3 5 + 10 *"
    print reversePolishNotation(expre)
    
run()
        